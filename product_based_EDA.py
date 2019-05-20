import pandas as pd # Import required packages
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from pylab import rcParams
import statsmodels.api as sm

df1 = pd.read_csv('C:\\Users\\Ayush gupta\\Documents\\Project Data.csv') # Import the data 
df = pd.DataFrame(df1)
df['transactionDate'] = pd.to_datetime(df['transactionDate'])
# print(df['transactionDate'].min())
# print(df['transactionDate'].max())

cols=['customerID','DOB','Gender','store_code','PinCode','store_description',
      'till_no','transaction_number_by_till','promotion_description'] # Import columns in list
df.drop(cols,axis=1,inplace=True)
df=df.sort_values('transactionDate')
# print(df[:].isnull().sum())   # print null values

df=df.groupby('transactionDate')["sales"].sum().reset_index()
df=df.set_index('transactionDate')
# print(df['product_description'].value_counts()[:10]) # print product discriptipn with value from start to end date
start='2015-06-01'
end='2017-06-30'
df=df.loc[start:end]

# print(df.index) # print with pyplot
y = df['sales'].resample('MS').mean()
#
# y1=y['2015-01-01':'2015-12-31']
# y2=y['2016-01-01':'2016-12-31']
# y3=y['2017-01-01':'2017-12-31']
# y1.plot(figsize=(15, 6))
# plt.show()
# y2.plot(figsize=(15, 6))
# plt.show()
# y3.plot(figsize=(15, 6))

# y.plot(figsize=(15, 6))
# plt.show()
#
rcParams['figure.figsize'] = 18, 8
decomposition = sm.tsa.seasonal_decompose(y, model='additive')
fig = decomposition.plot()
plt.show()

# pro_grp=df.groupby('transactionDate')['product_description'].sum().reset_index()
# df=df.set_index('transactionDate')
# x = df['product_description'].value_counts()
# p_count= x.iloc[[2,5,6,8,9,10,13,14,15,16],]
# xaxis_name= p_count.unique()
## print(p_count)
# y_pos = np.arange(len(p_count))
# p_bar = plt.barh(y_pos,p_count, align='center', alpha=0.5)
# plt.yticks(y_pos,p_count.keys(),fontsize=7,weight='light')
# plt.xlabel('count')
# plt.title('Item')
# plt.show()

# print(y.head()) # print top vlaues in head 

