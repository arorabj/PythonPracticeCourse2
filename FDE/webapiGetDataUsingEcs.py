import boto3
import logging
import requests
import json
import os
import datetime
import io

from botocore.exceptions import ClientError

#Initiate Logging
Format= '%(asctime)-15s %(message)s'
logging.basicConfig(Format=Format)

logger = logging.getLogger(__name__)
logger.setLevel (logging.INFO)

#Initiate clients, proxies and config
ssm_client = boto3.client("ssm",os.environ['AWS_REGION'])
ddb_client = boto3.client("dynamodb",os.environ['AWS_REGION'])
s3_client = boto3.client("s3",os.environ['AWS_REGION'])

proxies = {'http': 'http://app-proxy.localendpoint.banksvcs.net:8080',
          'https': 'https://app-proxy.localendpoint.banksvcs.net:8080'}


def get_ssm(key : str):

    """
    Retrieves parameter for SSM parameter store

    Description:
    This will be a boto3 SSM apito retreieve the value of an SSM parameter.
    This will only return keys that lambda policy has access today

    :param key: Name of SSM parameter including path and leading slash
    :return:Value of parameter

    """

    try:
        secret=ssm_client.get_parameter(Name=key, WithDecryption=True)
    except ClientError as e :
        logger.error(f"Error:{e}")
        raise Exception ("Unable to retrieve ssm parameter :" + key )
    else:
        return secret.get("Parameter").get("Value")


def get_token ():
    """
    Retrieves tokens

    Description:
    Description here

    :param key: None
    :return:tokens

    """

    logger.info("Connect to catalog endpoint lambda trigger")
    url = get_ssm('webapi_odin_auth_url')

    r = requests.post(url,
                      data={
                          'client_id' :get_ssm('webapi_odin_client_id'),
                          'username'  :get_ssm('webapi_odin_username'),
                          'passowrd'  :get_ssm('webapi_odin_password'),
                          'grant_type':'password'

                      },
                      headers={
                          'Content-Type':'applicaction/x-www-form-urlencoded'
                      },
                      proxies=proxies
    )
    data_token= json.loads(r.text)

    tokens = {
        'access_token':data_token["access_token"],
        'refresh_token':data_token['refresh_token']
    }

    return tokens


def get_catalog(token : str):
    """
    Gets Catalog data

    Description:
    Gets the catalog data from data endpoint

    :param key: CAPI token string
    :return: catalog data

    """

    try:
        pagination_from = 0
        pagination_size = 3
        response_json =[{'init_value' :'init_value'}]
        cumulated_response = []

        while len(response_json) != 0:
            logger.info(f"from : {pagination_from}, size : {pagination_size}")
            query_string=f"?q=*&from={pagination_from}&size={pagination_size}&index=gb_flood"
            pagination_from += pagination_size
            logger.info(f"Query : {query_string}")

            r_catalog = requests.get(
                get_ssm('webapi_odin_search_url')+ query_string,
                headers={
                    'Authorization':'Bearer' + token
                },
                proxies=proxies
            )

            response_json = json.loads (r_catalog.text)

            cumulated_response.extend(response_json)

    except ClientError as e :
        logger.error(f"Error:{e}")
        raise Exception (f"weapiConnectToEndPoint :Catalog Query failed" )
    else:
        return cumulated_response

def download_data_file(path, token):
    try:
        data = requests.get(
            'https://api.apps.dtp.airbusds-cint.com/api/v1/data' + path,
            stream = True,
            headers = {
                'Authorization': 'Bearer ' + token
            },
            proxies=proxies
        )

        logger.info(f"=-=-=- 1")

        filesize= int(data.headers['Content-Length'])

        if filesize < 20000:
            newfile = open('/tmp/odin_test_file_'+str(filesize),'wb')
            newfile.write(data.content)
            logger.info(f"after write")
        else:
            logger.info(f"file size is bigger : {filesize}")

        object = io.BytesIO(data.content)
        res = s3_client.upload_fileobj(object, 'recp-data-codl-dev-snowflake-staging-s3','esg/' + path )

        logger.info(f"====== after write: {res}")

    except Exception as e:
        logger.error(f"Error:{e}")
        raise Exception(f"data download failed")
    else:
        return True


def create_one_record (element,token):
    key = element['key']
    path = key['groupId'] + "/"+ key['ownerId'] + "/"+ key['typeId'] + "/"+ key['itemId']+ "/"+ key['versionId']

    logger.info(f"PATH = {path}")

    download_data_file(path,token)

    return {
        'catalogue_id' : {'S':path},
        'file_path': {'S': path},
        'checksum':{'S', element['checksum']},
        'date_added':{'S':datetime.datetime.now().isoformat()},
        'date_processed':{'S':''},
        'processed_ok':{'BOOL':False}
    }

def insert_one_record_db (element):
    """
    Insert element in dynamodb

    Description:
    Insert the record in dynamodb if not exists

    :param key: element to be inserted basis on attribute_not_exists
    :return: String with Record inserted for {path}

    """
    try:
        file_path = element["file_path"]
        ddb_client.put_item(
            TableName= 'awswebapi_Table',
            Item = element,
            ConditionExpression='attribute_not_exists(file_path)'
        )
    except ClientError as e :
        logger.error(f"Error:{e}")
        if e.reponse['Error']['Code']=='ConditionalCheckFailedException':
            logger.error(f"Attribute already exists")
            return f"Record not for {file_path}"
        else:
            raise Exception (f"Data file metadata insertion query failed for {file_path}" )
    else:
        return f"Record inserted for {file_path}"

def lambda_handler (event, context):
    logger(f"=-=-=- lambda handler 1 ")
    token = get_token()
    logger(f"=-=-=- lambda handler 2 ")
    data_catalog = get_catalog(token["access_token"])
    logger(f"=-=-=- lambda handler 3 ")
    records = [create_one_record(n, token["access_token"]) for n in data_catalog]
    for n in records:
        insert_one_record_db(n)
    return ""