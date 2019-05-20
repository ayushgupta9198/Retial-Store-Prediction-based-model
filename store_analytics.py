# ================Store analysis=======================================
# In this file store analysis i have tired to get store information with maximum sales from start to end date

import pandas as pd #import libraries
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

df1 = pd.read_csv('C:\\Users\\Ayush gupta\\Documents\\Project Data.csv') # import the data
df = pd.DataFrame(df1)from 
df['transactionDate'] = pd.to_datetime(df['transactionDate'])

cols=['customerID','DOB','Gender','store_code','PinCode',
      'till_no','transaction_number_by_till','promotion_description'] # Mentioning coloum names from data
df.drop(cols,axis=1,inplace=True)
df=df.sort_values('transactionDate')
df=df.set_index('transactionDate')
start='2016-01-01' # start date from where we can check the store sales
end='2016-12-31' # End date 
df=df.loc[start:end]

df=df.groupby('store_description')["sales"].sum().sort_values()
top=df.sort_values()
# top=df.top
print(top.nlargest(1)) # Print the largest vlaue from data

