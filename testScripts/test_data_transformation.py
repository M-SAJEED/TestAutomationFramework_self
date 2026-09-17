
#6 test cases

import inspect
from commonUtilities.utility import *


@pytest.mark.usefixtures('connect_to_mysqldb')
class TestDataTransformation:
    validation_utility = ValidationUtility()

    def test_transform_Filter_Sales(self,connect_to_mysqldb):
        try:
            expected_query = """select * from stag_sales where sale_date>='2024-09-10'"""
            actual_query = '''select * from filtered_sales'''
            test_case_name = inspect.currentframe().f_code.co_name
            self.validation_utility.execute_validation(
                validation_type='DB_TO_DB'
                , test_case_name=test_case_name
                , expected_query=expected_query
                , expected_db=connect_to_mysqldb
                , actual_query=actual_query
                , actual_db=connect_to_mysqldb

            )
        except Exception as e:
            pytest.fail()

    def test_transform_Router_High_Sales(self,connect_to_mysqldb):
        try:
            expected_query = """select * from filtered_sales where region='High'"""
            actual_query = '''select * from high_sales'''
            test_case_name = inspect.currentframe().f_code.co_name
            self.validation_utility.execute_validation(
                validation_type='DB_TO_DB'
                , test_case_name=test_case_name
                , expected_query=expected_query
                , expected_db=connect_to_mysqldb
                , actual_query=actual_query
                , actual_db=connect_to_mysqldb

            )
        except Exception as e:
            pytest.fail()

    def test_transform_Router_Low_Sales(self,connect_to_mysqldb):
        try:
            expected_query = """select * from filtered_sales where region='low'"""
            actual_query = '''select * from low_sales'''
            test_case_name = inspect.currentframe().f_code.co_name
            self.validation_utility.execute_validation(
                validation_type='DB_TO_DB'
                , test_case_name=test_case_name
                , expected_query=expected_query
                , expected_db=connect_to_mysqldb
                , actual_query=actual_query
                , actual_db=connect_to_mysqldb

            )
        except Exception as e:
            pytest.fail()

    def test_transform_Aggregator_Sales(self,connect_to_mysqldb):
        try:
            expected_query = """select fs.product_id,year(fs.sale_date) as year,month(fs.sale_date) as month, sum(fs.price*fs.quantity) as total_sales 
                                                from filtered_sales as fs group by fs.product_id,year(fs.sale_date),month(fs.sale_date)"""

            actual_query = '''select * from monthly_sales_summary_source'''
            test_case_name = inspect.currentframe().f_code.co_name
            self.validation_utility.execute_validation(
                validation_type='DB_TO_DB'
                , test_case_name=test_case_name
                , expected_query=expected_query
                , expected_db=connect_to_mysqldb
                , actual_query=actual_query
                , actual_db=connect_to_mysqldb

            )
        except Exception as e:
            pytest.fail()

    def test_transform_joiner_sales_product_stores(self,connect_to_mysqldb):
        try:
            expected_query = """select fs.sales_id,fs.quantity,fs.price,fs.quantity*fs.price as sales_amount,fs.sale_date,
                                    p.product_id,p.product_name,s.store_id,s.store_name from filtered_sales as fs inner join stag_product as p on fs.product_id = p.product_id
                                    inner join stag_stores as s on fs.store_id = s.store_id"""
            actual_query = '''select * from sales_with_details'''
            test_case_name = inspect.currentframe().f_code.co_name
            self.validation_utility.execute_validation(
                validation_type='DB_TO_DB'
                , test_case_name=test_case_name
                , expected_query=expected_query
                , expected_db=connect_to_mysqldb
                , actual_query=actual_query
                , actual_db=connect_to_mysqldb

            )
        except Exception as e:
            pytest.fail()

    def test_transform_Aggregator_Inventory(self,connect_to_mysqldb,):
        try:
            expected_query = """select store_id,sum(quantity_on_hand) as total_inventory from stag_inventory group by store_id"""
            actual_query = """select * from aggregated_inventory_level"""
            test_case_name = inspect.currentframe().f_code.co_name
            self.validation_utility.execute_validation(
                validation_type='DB_TO_DB'
                , test_case_name=test_case_name
                , expected_query=expected_query
                , expected_db=connect_to_mysqldb
                , actual_query=actual_query
                , actual_db=connect_to_mysqldb

            )
        except Exception as e:
            pytest.fail()

