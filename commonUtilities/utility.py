import pandas as pd
import logging
import datetime as dt
import pytest

logging.basicConfig(filename=f"logs/logfile_{dt.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
                    ,format = '%(asctime)s-%(levelname)s-%(message)s'
                    ,filemode='a'
                    ,level=logging.INFO)
logger = logging.getLogger(__name__)

class BaseUtility:
    def __init__(self):
        pass

    def __readfile(self,file_type,file_path):
        self.log_info(f"started reading file {file_path} filetype{file_type}")
        if file_type == "csv":
            df=pd.read_csv(file_path)
        elif file_type == "json":
            df=pd.read_json(file_path)
        elif file_type == "xml":
            df=pd.read_xml(file_path,xpath=".//item")
        else:
            self.log_error(f"file type not supported,type:{file_type}")
            raise ValueError(f"invalid file type{file_type}")
        self.log_info(f"completed reading file {file_path} filetype{file_type}")
        return df

    def readfile(self,file_type,file_path):
        return self.__readfile(file_type,file_path)

    def log_info(self,message):
        logger.info(message)

    def log_error(self,message):
        logger.error(message)


class ValidationUtility(BaseUtility):

    def execute_validation(self,validation_type,test_case_name,file_key=None,file_type=None,file_path=None,actual_db=None,actual_query=None,expected_db=None,expected_query=None):
        try:
            self.log_info(f"selected  {validation_type} validation type.")
            if validation_type == 'FILE_TO_DB':
                self.validate_file_to_db(test_case_name,file_type,file_path,actual_query,actual_db)
            elif validation_type == 'DB_TO_DB':
                self.validate_db_to_db(test_case_name,actual_query,actual_db,expected_query,expected_db)
            elif validation_type == 'S3_TO_DB':
                self.validate_s3_to_db(file_key,file_path,actual_db,actual_query)
            else:
                raise ValueError(f"invalid validation type{validation_type}")
        except Exception as e:
            self.log_error(e)

    def validate_file_to_db(
            self,
            test_case_name,
            file_type,
            file_path,
            actual_query,
            actual_db):

        try:
            self.log_info(f"{test_case_name}: Validation started...")

            expected_df = self.readfile(file_type, file_path)
            actual_df = pd.read_sql(actual_query, actual_db)

            self._compare_dataframes(
                test_case_name,
                expected_df,
                actual_df
            )

            self.log_info(
                f"{test_case_name}: Validation completed successfully!"
            )

        except Exception as e:
            self.log_error(str(e))
            pytest.fail(str(e))

    def validate_db_to_db(
            self,
            test_case_name,
            expected_query,
            expected_db,
            actual_query,
            actual_db):

        try:
            self.log_info(f"{test_case_name}: Validation started...")

            expected_df = pd.read_sql(expected_query, expected_db)
            actual_df = pd.read_sql(actual_query, actual_db)

            self._compare_dataframes(
                test_case_name,
                expected_df,
                actual_df
            )

            self.log_info(
                f"{test_case_name}: Validation completed successfully!"
            )

        except Exception as e:
            self.log_error(str(e))
            pytest.fail(str(e))

    def validate_s3_to_db(self,file_key,file_path,actual_db,actual_query):
            pass

    def _compare_dataframes(
            self,
            test_case_name: str,
            expected_df: pd.DataFrame,
            actual_df: pd.DataFrame):

        expected_df = expected_df.convert_dtypes()
        actual_df = actual_df.convert_dtypes()

        sort_cols = list(expected_df.columns)

        expected_df = (
            expected_df
            .sort_values(sort_cols)
            .reset_index(drop=True)
        )

        actual_df = (
            actual_df
            .sort_values(sort_cols)
            .reset_index(drop=True)
        )

        # Handle duplicate records
        expected_df["rn"] = (
            expected_df.groupby(sort_cols).cumcount()
        )

        actual_df["rn"] = (
            actual_df.groupby(sort_cols).cumcount()
        )

        expected_rows = expected_df.apply(tuple, axis=1)
        actual_rows = actual_df.apply(tuple, axis=1)

        extra_in_expected = expected_df[
            ~expected_rows.isin(actual_rows)
        ]

        extra_in_actual = actual_df[
            ~actual_rows.isin(expected_rows)
        ]

        if not extra_in_expected.empty:
            extra_in_expected[sort_cols].to_csv(
                f"differences/{test_case_name}_extra_in_expected.csv",
                index=False
            )

        if not extra_in_actual.empty:
            extra_in_actual[sort_cols].to_csv(
                f"differences/{test_case_name}_extra_in_actual.csv",
                index=False
            )

        assert expected_df.equals(actual_df) ,f'''           
                {test_case_name}: Records are not matching.
                f"Refer differences folder.'''


class SchemaValidationUtitily(BaseUtility):

    def validate_columns(self, test_case_name,actual_db,table_name,expected_columns):
        try:
            query =f'''select * from {table_name}'''
            self.log_info(f"{test_case_name}: column Validation started for {table_name} table...")
            actual_col_not_available =[]
            expected_col_not_avialble = []
            actual_df = pd.read_sql(query, actual_db)
            actual_col_set = set(actual_df.columns)
            len_of_actual_col=len(actual_col_set)
            len_of_expected_col=len(expected_columns)
            if (len_of_expected_col != len_of_actual_col) or (set(expected_columns)!=actual_col_set):
                for col in expected_columns:
                    if col not in actual_col_set:
                        actual_col_not_available.append(col)
                for col in actual_col_set:
                    if col not in expected_columns:
                        expected_col_not_avialble.append(col)
            assert len_of_expected_col==len_of_actual_col , (f'column count mismatch expected_col:{len_of_expected_col} '
                                                             f'actual_col_set:{len_of_actual_col}'
                                                             f'extra col in expected {actual_col_not_available}'
                                                             f'extra col in actual {expected_col_not_avialble}'
                                                             )

            assert not actual_col_not_available ,f'unavailable columns are {actual_col_not_available} in actual but available in expected'
            assert not expected_col_not_avialble, f'unavailable columns are {expected_col_not_avialble} in expected but available in actual'
            self.log_info(f"{test_case_name}: column Validation completed successfully!")
        except Exception as e:
            self.log_error(str(e))
            pytest.fail(str(e))


    def validate_datatype_of_col(self, test_case_name,actual_db,table_name,expected_dtypes:dict):
        try:
            query = f'''select * from {table_name}'''
            self.log_info(f"{test_case_name}: datatype Validation started for {table_name} table...")
            mismatch_dtypes = {}
            actual_df = pd.read_sql(query, actual_db)
            print(actual_df.dtypes)

            for col,expect_dtype in expected_dtypes.items():
                if actual_df[col].dtype not in expect_dtype:
                    mismatch_dtypes[col] =f"expected:{expect_dtype} - actual:{actual_df[col].dtype}"
            assert not mismatch_dtypes , f'datatypes mismatch: {mismatch_dtypes}'
            self.log_info(f"{test_case_name}: datatype Validation completed successfully!")
        except Exception as e:
            self.log_error(str(e))
            pytest.fail(str(e))

#duplicate checks
#null checks
#data integrity checks
class DataQualityValidationUtility(BaseUtility):
    #duplicate checks for entire row by keeping subset_col as None or pass list of columns
    def validate_duplicates_in_file(self,test_case_name,file_type,file_path,subset_col=None):
        try:
            self.log_info(f"{test_case_name}: duplicate  validation started for file {file_path}")
            df = self.readfile(file_path=file_path,file_type=file_type)
            duplicate_df=df[df.duplicated(subset=subset_col,keep="first")]
            if not duplicate_df.empty:
                duplicate_df.to_csv('differences/duplicates/'+test_case_name+'_duplicates.csv',index=False)

            assert duplicate_df.empty , f'{test_case_name}: duplicate file validation failed. refer differences/duplicates folder'
            self.log_info(f"{test_case_name}: duplicate validation for file {file_path} completed successfully!")
        except Exception as e:
            self.log_error(str(e))
            pytest.fail(str(e))

    def validate_nulls_in_file(self, test_case_name, file_type, file_path, subset_col=None):
        try:
            self.log_info(f"{test_case_name}: duplicate file validation started for {file_path}")
            df = self.readfile(file_path=file_path, file_type=file_type)
            is_cols_null=False
            if subset_col is not None:
                is_cols_null = df[subset_col].isnull().values.any()
            else:
                is_cols_null = df.isnull().values.any()
            assert not is_cols_null , f'{test_case_name}: null  validation failed'
            self.log_info(f"{test_case_name}: null  validation for file {file_path} completed successfully!")
        except Exception as e:
            self.log_error(str(e))
            pytest.fail(str(e))

