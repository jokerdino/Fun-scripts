import pandas as pd
import numpy as np
import re
import sys

# receive input file as argument of script
file_name = sys.argv[1]
file_type = file_name.split(".")[-1]
remarks = sys.argv[2]

df_rewards = pd.read_excel(file_name)


df_rewards["TXT_INTERMEDIARY_NAME"] = (df_rewards["TXT_INTERMEDIARY_NAME"].astype('category')
                                        .str.replace(".","",regex=True)
                                        .str.replace("/","",regex=True)
                                        )

df_rewards["TXT_AGENT_ID"] = df_rewards["TXT_AGENT_ID"].astype('category')

# collect names of dataframe and parse columns with _DATE as suffix into datetime types
column_names = df_rewards.columns.values.tolist()
r = re.compile(".*_DATE")
list_date = list(filter(r.match, column_names))


# converting datetime types into human readable date values
if file_type == "xlsx":
    for dates in list_date:
        df_rewards[dates] = pd.to_datetime(df_rewards[dates],dayfirst=True, errors='coerce').dt.strftime("%d/%m/%Y")
elif file_type == "xlsb":
    for dates in list_date:
        df_rewards[dates] = pd.to_datetime(pd.to_numeric(df_rewards[dates], errors='coerce'),errors='coerce',origin='1899-12-30',unit='D').dt.strftime("%d/%m/%Y")

# splitting the details file into separate files based on broker name
broker_name = df_rewards["TXT_INTERMEDIARY_NAME"].unique()

for i in broker_name:
    df_broker = df_rewards[df_rewards["TXT_INTERMEDIARY_NAME"].str.contains(i)]
    broker_file_name = i+"_"+remarks+ ".xlsx"
    df_broker.to_excel(broker_file_name,index=False,sheet_name="Details")
    # creating a summary file
    pivot_table = pd.pivot_table(data=df_broker,index=['TXT_RO_CODE','TXT_INTERMEDIARY_NAME','CATEGORY'],aggfunc={'CUR_REWARD_AMOUNT':np.sum})
    with pd.ExcelWriter(broker_file_name) as writer:
        df_broker.to_excel(writer, sheet_name="Details",index=False)
        pivot_table.to_excel(writer, sheet_name='Summary')
