import pandas as pd

df1 = pd.DataFrame({'a':[1,2,3,3], 'b':[4,5,6,6]})
df2 = pd.DataFrame({'a':[2,2,3], 'b':[4,5,6]})

print(df1)
print(df2)

print(df1.merge(df2, how='outer',indicator=True))
print(df1.merge(df2,on='a', how='outer',indicator=True))

'''
fact_sales
Column Name	Data Type
sales_id	INT
product_id	INT
store_id	INT
quantity	INT
total_sales	DECIMAL(10,2)
sale_date	DATE

fact_inventory
product_id	INT
store_id	INT
quantity_on_hand	INT
last_updated	DATE

monthly_sales_summary
product_id	INT
month	INT
year	INT
total_sales	DECIMAL(10,2)

inventory_levels_by_store
store_id	INT
total_inventory	INT


'''