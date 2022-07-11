import json
import boto3
import sys
import logging
import psycopg2

# logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

config ={'dbname'   : 'database_name',
         'host'     : 'redshoft_endpoint',
         'port'     : 'redshift_port',
         'user'     : 'usr_name',
         'password' : 'user_password'}


s3 = boto3.client('s3')


def create_conn(*args, **kwargs):
    config = kwargs['config']
    try:
        conn = psycopg2.connect(dbname=config['dbname'],
                                host=config['host'],
                                port = config['port'],
                                user = config['user'],
                                password = config['password'])
    except Exception as err:
        print (err.code, err)
    return conn

def lambda_handler(event, context):

    bucket = 'my_project_bucket'
    key = 'sample_payload.json'

    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body']
    jsonObject = json.loads(content.read())

    logger.info(jsonObject)

    conn = create_conn(config=config)
    cursor = conn.cursor()
    cursor.execute("""SELECT count(*) FROM Mytable where User_Guid = '{0}' ;""".format(jsonObject['User\'s Object ID']))

    rows = cursor.fetchall()

    for row in rows:
        logger.info(f'rowcount is : {row}' )
        if row == 0 :
            cursor.execute(
                """Insert into mytable (
                         APP_ID,
                         BIRTH_MONTH_YEAR,
                         CITY,
                         COUNTRY_AND_REGION,
                         DISPLAY_NAME,
                         EMAIL,
                         GENDER,
                         GIVEN_NAME,
                         IDENTITY_PROVIDER,
                         JOB_TITLE,
                         FIRST_NAME,
                         LAST_NAME,
                         LEGAL_AGE_GROUP_CLASSIFICATION,
                         POSTAL_CODE,
                         STATE,
                         STREET_ADDRESS,
                         SURNAME,
                         USER_IS_NEW,
                         USER_OBJECT_ID
                   ) values (
                         '{0}',
                         '{1}',
                         '{2}',
                         '{3}',
                         '{4}',
                         '{5}',
                         '{6}',
                         '{7}',
                         '{8}',
                         '{9}',
                         '{10}',
                         '{11}',
                         '{12}',
                         '{13}',
                         '{14}',
                         '{15}',
                         '{16}',
                         '{17}',
                         '{18}'
                   );""".format(jsonObject['AppID'],jsonObject['Birth Month Year'],jsonObject['City'],
                                jsonObject['Country/Region'],jsonObject['Display Name'],jsonObject['Email Address'],
                                jsonObject['Gender'],jsonObject['Given Name'],jsonObject['Identity Provider'],
                                jsonObject['Job Title'],jsonObject['Kana First Name'],jsonObject['Kana Last Name'],
                                jsonObject['Legal Age Group Classification'],jsonObject['Postal Code'],jsonObject['State/Province'],
                                jsonObject['Street Address'],jsonObject['Surname'],jsonObject['User is new'],
                                jsonObject['User\'s Object ID']
                                )
            )

            logger.info(f'inserted data')
        else:
            cursor.execute(
                """Update mytable 
                   Set APP_ID ='{0}',
                     BIRTH_MONTH_YEAR='{1}',
                     CITY='{2}',
                     COUNTRY_AND_REGION='{3}',
                     DISPLAY_NAME='{4}',
                     EMAIL='{5}',
                     GENDER='{6}',
                     GIVEN_NAME='{7}',
                     IDENTITY_PROVIDER='{8}',
                     JOB_TITLE='{9}',
                     FIRST_NAME='{10}',
                     LAST_NAME='{11}',
                     LEGAL_AGE_GROUP_CLASSIFICATION='{12}',
                     POSTAL_CODE='{13}',
                     STATE='{14}',
                     STREET_ADDRESS='{15}',
                     SURNAME='{16}',
                     USER_IS_NEW='{17}'
                   Where USER_OBJECT_ID ='{18}';""".format(jsonObject['AppID'], jsonObject['Birth Month Year'], jsonObject['City'],
                                jsonObject['Country/Region'], jsonObject['Display Name'], jsonObject['Email Address'],
                                jsonObject['Gender'], jsonObject['Given Name'], jsonObject['Identity Provider'],
                                jsonObject['Job Title'], jsonObject['Kana First Name'], jsonObject['Kana Last Name'],
                                jsonObject['Legal Age Group Classification'], jsonObject['Postal Code'],
                                jsonObject['State/Province'],
                                jsonObject['Street Address'], jsonObject['Surname'], jsonObject['User is new'],
                                jsonObject['User\'s Object ID']
                                )
            )

            logger.info(f'updated data')
        cursor.close()
        conn.close()