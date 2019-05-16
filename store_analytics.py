import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

df1 = pd.read_csv('C:\\Users\\Prince\\Downloads\\cproducts.csv')
df = pd.DataFrame(df1)
df['transactionDate'] = pd.to_datetime(df['transactionDate'])

cols=['customerID','DOB','Gender','store_code','PinCode',
      'till_no','transaction_number_by_till','promotion_description']
df.drop(cols,axis=1,inplace=True)
df=df.sort_values('transactionDate')
df=df.set_index('transactionDate')
start='2016-01-01'
end='2016-12-31'
df=df.loc[start:end]


df=df.groupby('store_description')["sales"].sum().sort_values()


top=df.sort_values()
# top=df.top
print(top.nlargest(1))

