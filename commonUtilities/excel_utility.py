import pandas as pd

class MyExcelUtility:

    def get_table_schema(self,excel_path, table_name):
        df = pd.read_excel(excel_path)
        schema = (
            df[df['table_name'].str.strip().str.lower() == table_name.lower()]
            .set_index('column_name')["data_type"]
            .to_dict()
        )

        return schema

