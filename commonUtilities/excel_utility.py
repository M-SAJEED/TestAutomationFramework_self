import pandas as pd

class ExcelUtility:

    def get_table_schema(excel_path, table_name):
        df = pd.read_excel(excel_path)

        schema = (
            df[df["table_name"].str.strip().str.lower() == table_name.lower()]
            .set_index("column_name")["dtype"]
            .to_dict()
        )

        return schema

    schema = get_table_schema("metadata.xlsx", "fact_sales")
    print(schema)
