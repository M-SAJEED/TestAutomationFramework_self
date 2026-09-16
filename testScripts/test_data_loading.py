
#4 test cases

import inspect
from commonUtilities.utility import *


@pytest.mark.usefixtures('connect_to_mysqldb')
class TestDataLoading:
    validation_utility = ValidationUtility()

    def test_data_loading_for_monthly_sales_summary(self,connect_to_mysqldb):
        try:
            expected_query = """select ms.product_id,ms.month,ms.year,ms.total_sales 
                                from monthly_sales_summary_source as ms order by ms.product_id"""
            actual_query = """select m.product_id,m.month,m.year,m.total_sales 
                                from monthly_sales_summary as m order by m.product_id"""
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

    def test_data_loadin_for_fact_sales(self,connect_to_mysqldb):
        try:
            expected_query = """select sd.sales_id,sd.product_id,sd.store_id,sd.quantity,cast(sd.sales_amount as decimal(10,2)) as total_sales,
                                cast(sd.sale_date as date) sale_date from sales_with_details as sd order by sd.sales_id,sd.product_id,sd.store_id"""
            actual_query = """select fs.sales_id,fs.product_id,fs.store_id,fs.quantity, fs.total_sales,fs.sale_date 
                              from fact_sales as fs order by fs.sales_id,fs.product_id,fs.store_id"""
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

    def test_data_loading_for_fact_inventory(self,connect_to_mysqldb):
        try:
            expected_query = """select product_id,store_id,quantity_on_hand,cast(last_updated as date)as last_updated  from stag_inventory"""
            actual_query = """select product_id,store_id,quantity_on_hand,last_updated from fact_inventory"""
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

    def test_data_loading_for_inventory_levl_by_stores(self,connect_to_mysqldb):
        try:
            expected_query = """select store_id,total_inventory from aggregated_inventory_level"""
            actual_query = """select store_id,total_inventory from inventory_levels_by_store"""
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


