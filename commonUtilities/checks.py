import pandas as pd
from testConfigurations.config import *
import paramiko
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
#download file from linux

def linux_utility_download_file_from_linux_server():
    try:
        print("Linux file download started..")
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(LINUX_HOSTNAME, username=LINUX_USERNAME, password=LINUX_PASSWORD)
        sftp = ssh_client.open_sftp()
        sftp.get(LINUX_REMOTE_FILE_PATH, LOCAL_FILE_PATH)
        sftp.close()
        print("Linux file download finished.")
    except Exception as e:
        print(e)
linux_utility_download_file_from_linux_server()
