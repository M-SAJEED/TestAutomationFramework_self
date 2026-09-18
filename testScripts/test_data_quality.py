# test cases
import pytest
import inspect
from commonUtilities.utility import DataQualityValidationUtility


@pytest.mark.usefixtures('connect_to_mysqldb')
class TestDataQuality:
    dq_val_util = DataQualityValidationUtility()

    #check duplicates in input files ---------------------------------
    @pytest.mark.dataquality
    def test_duplicates_for_sales_file(self):
        try:
            test_case_name = inspect.currentframe().f_code.co_name
            self.dq_val_util.validate_duplicates_in_file(
                 test_case_name=test_case_name
                ,file_type='csv'
                ,file_path='testData/sales_data_s3.csv'
                ,subset_col=None
            )
        except Exception as e:
            pytest.fail()

    ## reading from oracle db
    @pytest.mark.dataquality
    @pytest.mark.skip
    def test_extract_stores_data_from_oracle_to_stag(self,connect_to_oracledb):
        try:
            test_case_name = inspect.currentframe().f_code.co_name
            self.dq_val_util.validate_duplicates_in_file(
                 test_case_name=test_case_name
                ,file_type='csv'
                ,file_path='testData/sales_data_s3.csv'
                ,subset_col=None
            )
        except Exception as e:
            pytest.fail()

    @pytest.mark.dataquality
    #@pytest.mark.skip
    def test_duplicates_for_product_file(self):
        try:
            test_case_name = inspect.currentframe().f_code.co_name
            self.dq_val_util.validate_duplicates_in_file(
                 test_case_name=test_case_name
                ,file_type='csv'
                ,file_path='testData/product_data_from_linux.csv'
                ,subset_col=None
            )
        except Exception as e:
            pytest.fail()

    #@pytest.mark.skip
    @pytest.mark.dataquality
    def test_duplicates_for_inventory_file(self):
        try:
            test_case_name = inspect.currentframe().f_code.co_name
            self.dq_val_util.validate_duplicates_in_file(
                 test_case_name=test_case_name
                ,file_type='xml'
                ,file_path='testData/inventory_data.xml'
                ,subset_col=None
            )
        except Exception as e:
            pytest.fail()


    #@pytest.mark.skip
    @pytest.mark.dataquality
    def test_duplicates_for_supplier_file(self):
        try:
            test_case_name = inspect.currentframe().f_code.co_name
            self.dq_val_util.validate_duplicates_in_file(
                 test_case_name=test_case_name
                ,file_type='json'
                ,file_path='testData/supplier_data.json'
                ,subset_col=None
            )
        except Exception as e:
            pytest.fail()

#check null checks in input files ---------------------------------
    @pytest.mark.dataquality
    def test_null_for_sales_file(self):
        try:
            test_case_name = inspect.currentframe().f_code.co_name
            self.dq_val_util.validate_nulls_in_file(
                 test_case_name=test_case_name
                ,file_type='csv'
                ,file_path='testData/sales_data_s3.csv'
                ,subset_col=None
            )
        except Exception as e:
            pytest.fail()

    ## reading from oracle db
    @pytest.mark.dataquality
    @pytest.mark.skip
    def test_null_stores_data_from_oracle_to_stag(self,connect_to_oracledb):
        try:
            test_case_name = inspect.currentframe().f_code.co_name
            self.dq_val_util.validate_nulls_in_file(
                 test_case_name=test_case_name
                ,file_type='csv'
                ,file_path='testData/sales_data_s3.csv'
                ,subset_col=None
            )
        except Exception as e:
            pytest.fail()

    #@pytest.mark.skip
    @pytest.mark.dataquality
    def test_null_for_product_file(self):
        try:
            test_case_name = inspect.currentframe().f_code.co_name
            self.dq_val_util.validate_nulls_in_file(
                 test_case_name=test_case_name
                ,file_type='csv'
                ,file_path='testData/product_data_from_linux.csv'
                ,subset_col=None
            )
        except Exception as e:
            pytest.fail()

    #@pytest.mark.skip
    @pytest.mark.dataquality
    def test_null_for_inventory_file(self):
        try:
            test_case_name = inspect.currentframe().f_code.co_name
            self.dq_val_util.validate_nulls_in_file(
                 test_case_name=test_case_name
                ,file_type='xml'
                ,file_path='testData/inventory_data.xml'
                ,subset_col=None
            )
        except Exception as e:
            pytest.fail()


    #@pytest.mark.skip
    @pytest.mark.dataquality
    def test_null_for_supplier_file(self):
        try:
            test_case_name = inspect.currentframe().f_code.co_name
            self.dq_val_util.validate_nulls_in_file(
                 test_case_name=test_case_name
                ,file_type='json'
                ,file_path='testData/supplier_data.json'
                ,subset_col=None
            )
        except Exception as e:
            pytest.fail()

