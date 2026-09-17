#4 test cases for columns test
#4 test cases for dtype checks
#change table names and expected columns list
import inspect
from commonUtilities.utility import *


@pytest.mark.usefixtures('connect_to_mysqldb')
class TestSchema:
    schema_validation_utility = SchemaValidationUtitily()
    #columns check test cases -----------------------------------------------------
    def test_columns_for_monthly_sales_summary(self,connect_to_mysqldb):
        try:
            expected_columns = ['product_id','month','year','total_sales']
            test_case_name = inspect.currentframe().f_code.co_name
            self.schema_validation_utility.validate_columns(
                test_case_name=test_case_name,
                expected_columns=expected_columns,
                table_name='monthly_sales_summary',
                actual_db=connect_to_mysqldb,
            )
        except Exception as e:
            pytest.fail()

    def test_columns_for_fact_sales(self,connect_to_mysqldb):
        try:
            expected_columns = ['sales_id','product_id','store_id','quantity','total_sales','sale_date']
            test_case_name = inspect.currentframe().f_code.co_name
            self.schema_validation_utility.validate_columns(
                test_case_name=test_case_name,
                expected_columns=expected_columns,
                table_name='fact_sales',
                actual_db=connect_to_mysqldb,
            )
        except Exception as e:
            pytest.fail()

    def test_columns_for_fact_inventory(self,connect_to_mysqldb):
        try:
            expected_columns = ['product_id','store_id','quantity_on_hand','last_updated']
            test_case_name = inspect.currentframe().f_code.co_name
            self.schema_validation_utility.validate_columns(
                test_case_name=test_case_name,
                expected_columns=expected_columns,
                table_name='fact_inventory',
                actual_db=connect_to_mysqldb,
            )
        except Exception as e:
            pytest.fail()

    def test_columns_for_inventory_level_by_stores(self,connect_to_mysqldb):
        try:
            expected_columns = ['store_id','total_inventory']
            test_case_name = inspect.currentframe().f_code.co_name
            self.schema_validation_utility.validate_columns(
                test_case_name=test_case_name,
                expected_columns=expected_columns,
                table_name='inventory_levels_by_store',
                actual_db=connect_to_mysqldb,
            )
        except Exception as e:
            pytest.fail()



#Datatypes check test cases -----------------------------------------------------
    def test_dtypes_for_monthly_sales_summary(self,connect_to_mysqldb):
        try:
            expected_dtypes = {'product_id':'INT',
                                'month':'INT',
                                'year':'INT',
                                'total_sales':'DECIMAL(10,2)'
                               }
            expected_pandas_dtypes = self.schema_validation_utility.to_pandas_dtype(expected_dtypes)
            test_case_name = inspect.currentframe().f_code.co_name
            test_case_name = inspect.currentframe().f_code.co_name
            self.schema_validation_utility.validate_datatype_of_col(
                test_case_name=test_case_name,
                expected_dtypes=expected_pandas_dtypes,
                table_name='monthly_sales_summary',
                actual_db=connect_to_mysqldb,
            )
        except Exception as e:
            pytest.fail()

    def test_dtypes_for_fact_sales(self,connect_to_mysqldb):
        try:
            expected_dtypes = {'sales_id':'INT',
                                'product_id':'INT',
                                'store_id':'INT',
                                'quantity':'INT',
                                'total_sales':'DECIMAL(10,2)',
                                'sale_date':'DATE'
                                }
            expected_pandas_dtypes = self.schema_validation_utility.to_pandas_dtype(expected_dtypes)
            test_case_name = inspect.currentframe().f_code.co_name
            self.schema_validation_utility.validate_datatype_of_col(
                test_case_name=test_case_name,
                expected_dtypes=expected_pandas_dtypes,
                table_name='fact_sales',
                actual_db=connect_to_mysqldb,
            )
        except Exception as e:
            pytest.fail()

    def test_dtypes_for_fact_inventory(self,connect_to_mysqldb):
        try:
            expected_dtypes = {'product_id':'INT',
                                'store_id':'INT',
                                'quantity_on_hand':'INT',
                                'last_updated':'DATE',
                                }
            expected_pandas_dtypes = self.schema_validation_utility.to_pandas_dtype(expected_dtypes)
            test_case_name = inspect.currentframe().f_code.co_name
            self.schema_validation_utility.validate_datatype_of_col(
                test_case_name=test_case_name,
                expected_dtypes=expected_pandas_dtypes,
                table_name='fact_inventory',
                actual_db=connect_to_mysqldb,
            )
        except Exception as e:
            pytest.fail()

    def test_dtypes_for_inventory_level_by_stores(self,connect_to_mysqldb):
        try:
            expected_dtypes = {'store_id':'INT',
                                'total_inventory':'INT',
                                }
            expected_pandas_dtypes = self.schema_validation_utility.to_pandas_dtype(expected_dtypes)
            test_case_name = inspect.currentframe().f_code.co_name
            self.schema_validation_utility.validate_datatype_of_col(
                test_case_name=test_case_name,
                expected_dtypes=expected_pandas_dtypes,
                table_name='inventory_levels_by_store',
                actual_db=connect_to_mysqldb,
            )
        except Exception as e:
            pytest.fail()