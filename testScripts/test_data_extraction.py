# 5 test cases

import inspect
from commonUtilities.utility import *


@pytest.mark.usefixtures('connect_to_mysqldb','connect_to_oracledb')
class TestDataExtraction:
    validation_utility = ValidationUtility()

    def test_extract_data_for_sales_file_to_stage(self,connect_to_mysqldb):
        try:
            test_case_name = inspect.currentframe().f_code.co_name
            self.validation_utility.execute_validation(
                validation_type='FILE_TO_DB'
                ,test_case_name=test_case_name
                ,file_type='csv'
                ,file_path='testData/sales_data_s3.csv'
                ,actual_query='''select * from stag_sales;'''
                ,actual_db=connect_to_mysqldb

            )
        except Exception as e:
            pytest.fail()

    ## reading from oracle db
    #@pytest.mark.skip
    def test_extract_stores_data_from_oracle_to_stag(self,connect_to_mysqldb,connect_to_oracledb):
        try:
            test_case_name = inspect.currentframe().f_code.co_name
            self.validation_utility.execute_validation(
                validation_type='DB_TO_DB'
                , test_case_name=test_case_name
                , expected_query='''select * from stores'''
                , expected_db=connect_to_oracledb
                , actual_query='''select * from stag_stores;'''
                , actual_db=connect_to_mysqldb

            )
        except Exception as e:
            pytest.fail()

    #@pytest.mark.skip
    def test_extract_product_data_from_file_to_stag(self,connect_to_mysqldb):
        try:
            test_case_name = inspect.currentframe().f_code.co_name
            self.validation_utility.execute_validation(
                validation_type='FILE_TO_DB'
                , test_case_name=test_case_name
                , file_type='csv'
                , file_path='testData/product_data_from_linux.csv'
                , actual_query='''select * from stag_product;'''
                , actual_db=connect_to_mysqldb

            )
        except Exception as e:
            pytest.fail()

    #@pytest.mark.skip
    def test_extract_inventory_data_from_file_to_stag(self,connect_to_mysqldb):
        try:
            test_case_name = inspect.currentframe().f_code.co_name
            self.validation_utility.execute_validation(
                validation_type='FILE_TO_DB'
                , test_case_name=test_case_name
                , file_type='xml'
                , file_path='testData/inventory_data.xml'
                , actual_query='''select * from stag_inventory;'''
                , actual_db=connect_to_mysqldb

            )
        except Exception as e:
            pytest.fail()

    #@pytest.mark.skip
    def test_extract_supplier_data_from_file_to_stag(self,connect_to_mysqldb):
        try:
            test_case_name = inspect.currentframe().f_code.co_name
            self.validation_utility.execute_validation(
                validation_type='FILE_TO_DB'
                , test_case_name=test_case_name
                , file_type='json'
                , file_path='testData/supplier_data.json'
                , actual_query='''select * from stag_supplier;'''
                , actual_db=connect_to_mysqldb

            )
        except Exception as e:
            pytest.fail()

