import pandas as pd # Import required packages
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

'''Gender base plotting''' #Sex Ratio Distriubution of the sale
def gender_plot(self):
        df['Gender'].fillna(method='ffill',inplace=True)
        gender_data= plt.pie(df['Gender'].value_counts(),
                        labels=['Male','Female'],
                        shadow=True,
                        autopct='%1.1f%%',
                        explode = (0, 0.1),
                        startangle=90)
        return(gender_data)

'''Age base plotting''' #Age Groups Frequency Distribution
'''For filling blank dates(NAN) and NANA values'''
def age_group(self):
        df['DOB'].fillna(method='ffill',inplace=True)
        df['DOB'].replace(to_replace='NANA',
                          value='2019-04-02',
                          inplace=True)
        df['DOB']=pd.to_datetime(df['DOB'])
        # for col in df:
        #         print(type(df["DOB"][1]))
        column_1 = df['DOB'].loc[:]
        datestamp=pd.DataFrame({"year": column_1.dt.year,
                      # "month": column_1.dt.month,
                      # "day": column_1.dt.day,
                      # "hour": column_1.dt.hour,
                      # "dayofyear": column_1.dt.dayofyear,
                      # "week": column_1.dt.week,
                      # "weekofyear": column_1.dt.weekofyear,
                      # "dayofweek": column_1.dt.dayofweek,
                      # "weekday": column_1.dt.weekday,
                      # "quarter": column_1.dt.quarter,
                     })

        '''extraction of age from DOB'''

        cst_dob=datestamp.year
        df['age']=2019-cst_dob
        df['age_group'] = 'NA'
        df['age_group'][(df['age'] >= 30) &  (df['age']<=60)]= 'family'
        df['age_group'][(df['age'] > 18) & (df['age'] <= 29)] = 'youth'
        df['age_group'][(df['age'] <= 18) & (df['age']>=10)] = 'teen'
        df['age_group'][df['age'] >=61 ]='senior_c'
        # print(df['age_group'].value_counts())

        '''ploting AgeGroup'''
        plt.figure(figsize=(16,9),dpi=80)
        agcount=df['age_group'].value_counts()
        a_objects=('Family(30-60)','Youth(18-29)','Senior Citizen(60+)','NA','Teen(10-18)')
        y_pos=np.arange(len(a_objects))
        age_grp = plt.bar(y_pos,agcount,align='center',alpha=0.5)
        plt.xticks(y_pos,a_objects, fontsize=12 )
        plt.ylabel('count')
        plt.title('Age Group')

        # age_grp= plt.pie(df['age_group'].value_counts(),
        #                 labels=['Family','Youth','Senior Citizen','NA','Teen'],
        #                 shadow=True,
        #                 autopct='%1.1f%%',
        #                 explode = (0.1, 0,0,0,0),
        #                 startangle=180)
        return age_grp


'''For item counts or unique items count'''
# for col in df:
#         print(df["customerID"].value_counts())
#         break

if __name__ == '__main__':
        # header = ['customerID', 'DOB', 'Gender', 'State', 'PinCode', 'transactionDate',
        #           'store_code', 'store_description', 'till_no',
        #           'transaction_number_by_till', 'promo_code', 'promotion_description',
        #           'product_code', 'product_description', 'sale_price_after_promo', 'discountUsed']
        df1 = pd.read_csv('C:\\Users\\Prince\\Downloads\\cproducts.csv')
        df = pd.DataFrame(df1)

# ==============*Consumer Analytics*======================

# **************-Gender Plot-*****************************
        gender_obj=gender_plot(df['Gender'])
        plt.show(gender_obj)
# *************-Age Group Plot-***************************
        age_obj=age_group(df['DOB'])
        # grp_obj=df.groupby(['transactionDate'])
        plt.show(age_obj)

# =============*Product Based Analytics*==================

# *************-Top Selling products-*********************

        # desired_width = 400
        # pd.set_option('display.width', desired_width)
        # pd.set_option('display.max_columns', 16)
        #
        # df['transactionDate'] = pd.to_datetime(df['transactionDate'])
        # column_2 = df['transactionDate'].loc[:]
        # purchase_datestamp = pd.DataFrame({"year": column_2.dt.year,
        #                           # "month": column_2.dt.month,
        #                           # "day": column_1.dt.day,
        #                           # "hour": column_1.dt.hour,
        #                           # "dayofyear": column_1.dt.dayofyear,
        #                           # "week": column_1.dt.week,
        #                           # "weekofyear": column_1.dt.weekofyear,
        #                           # "dayofweek": column_1.dt.dayofweek,
        #                           # "weekday": column_1.dt.weekday,
        #                           # "quarter": column_2.dt.quarter,
        #                           })
        # # print(purchase_datestamp)
        # df['year_grp']=purchase_datestamp.year
        # gcount=df.groupby(['year_grp']).count()
        # pcount=df.groupby(['product_description']['year_grp':'2015']).value_counts()
        # print(gcount.head())
        # print(pcount.head())



