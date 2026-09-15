import pandas as pd
import logging
import datetime as dt
import pytest

import inspect
from commonUtilities.utility import *

@pytest.mark.usefixtures('','')
class TestDataExtraction:
    validation_utility = ValidationUtility()

    def test_extract_data_for_sales_file_to_stage(self):
        try:
            test_case_name = inspect.currentframe().f_code.co_name
            self.validation_utility.execute_validation(
                validation_type='FILE_TO_DB'
                ,test_case_name=test_case_name
                ,file_type='csv'
                ,file_path=''
                ,actual_query=''
                ,actual_db=''

            )
        except Exception as e:
            pytest.fail()

    ## reading from oracle db
    def test_extract_stores_data_from_oracle_to_stag(self):


    def test_extract_product_data_from_file_to_stag(self):

    def test_extract_inventory_data_from_file_to_stag(self):

    def test_extract_supplier_data_from_file_to_stag(self):

