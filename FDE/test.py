
import logging
import redshift_connector


# logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

config ={'dbname'   : 'jjdcamericaanalytics',
         'host'     : 'capturedev.cvyjwlx4kha5.us-east-1.redshift.amazonaws.com',
         'port'     : '5439',
         'user'     : 'jjvcservacct',
         'password' : 'R!VFctweq2pJ'}


def create_conn(*args, **kwargs):
    config = kwargs['config']
    try:
        conn = redshift_connector.connect(database=config['dbname'],
                                host=config['host'],
                                user = config['user'],
                                password = config['password'],
                                ssl = True,
                                port = 5439
                                )
    except Exception as err:
        print (err.code, err)
    return conn

def main():
    try:
        conn = create_conn(config=config)
        cursor = conn.cursor()
        logger.info (f"Refershing view warehouse_t.mv_fact_na_fsa_hob_extract")
        cursor.execute("""REFERSH MATERIALIZED VIEW  warehouse_t.mv_fact_na_fsa_hob_extract;""")
        cursor.close()
        conn.close()
        logger.info(f"Successfully Refershed View warehouse_t.mv_fact_na_fsa_hob_extract")
    except Exception as err:
        print (err.code, err)
        logger.error(f"{err}")


if __name__ == '__main__' :
    main()