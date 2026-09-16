import pytest
from sqlalchemy import create_engine
import pymysql
import oracledb
from commonUtilities.utility import BaseUtility
from testConfigurations.config import *
baseUtility = BaseUtility()


@pytest.fixture(scope="module")
def connect_to_mysqldb():
    try:
        baseUtility.log_info("connecting to mysql server...")
        mysql_conn = create_engine(F"mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}")
        connection=mysql_conn.connect()
        baseUtility.log_info("mysql server connected.")
        yield connection
        connection.close()
    except Exception as e:
        baseUtility.log_error(f"failed to connect mysql server with exception : {e}")

@pytest.fixture(scope="module")
def connect_to_oracledb():
    try:
        baseUtility.log_info("connecting to oracle server...")
        oracle_conn = create_engine(f"oracle+oracledb://{ORACLE_USERNAME}:{ORACLE_PASSWORD}@{ORACLE_HOST}:{ORACLE_PORT}/{ORACLE_SERVICE}")
        connection=oracle_conn.connect()
        baseUtility.log_info("oracle server connected.")
        yield connection
        connection.close()
    except Exception as e:
        baseUtility.log_error(f"failed to connect oracle server with exception : {e}")


