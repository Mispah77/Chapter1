#!/usr/bin/env python
# coding: utf-8

# In[1]:Importing required libraries


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


import warnings
warnings.filterwarnings('ignore')


# In[3]:Loading the dataset


df = pd.read_csv('data.csv',encoding = 'ISO-8859-1')


# In[4]:Displaying the dataframe


print(df)


# In[5]:Displaying no.of rows and columns


df.shape


# In[6]:Access first five rows


df.head()


# In[7]:Access last five rows


df.tail()


# In[8]:Displaying total columns from the dataset


df.columns


# In[9]:Displaying all columns one by one


for column in df.columns:
    print(column)


# In[10]:Renaming columns names


d = {'InvoiceNo' : 'invoice_num',
     'StockCode' : 'stock_code',
     'Description' : 'description',
     'Quantity' : 'quantity',
     'InvoiceDate' : 'invoice_date',
     'UnitPrice' : 'unit_price',
     'CustomerID' : 'cust_id',
     'Country' : 'country'}

df.rename(columns = d,inplace = True)


# In[11]:After changing checking new column names


df.columns

for i in df.columns:
    print(i)


# In[12]:Checking initial data


df.head()

# Data Cleaning

# In[13]:Checking column types


df.dtypes


# In[14]:DataFrame Information


df.info()


# In[15]:Checking missing values for each column


df.isnull()


# In[16]:Checking no.of columns


len(df.columns)


# In[17]:Displaying no.of rows and columns


df.shape


# In[18]:Checking missing values count on each column


df.isnull().sum()


# In[19]:Checking missing values count on each column,applying sort


df.isnull().sum().sort_values()

df.isnull().sum().sort_values(ascending = False)


# In[20]:Accessing initial data


df.head(2)


# In[21]:Checking column datatypes


df.dtypes


# In[22]:Converting invoice_date datatype into datetime datatype


df['invoice_date'] = pd.to_datetime(df.invoice_date,format = '%m/%d/%Y %H:%M')


# In[23]:Checking type of invoice_date


df.dtypes


# In[24]:Access the first five rows


df.head()


# In[25]:Checking description column


df.description


# In[26]:Converting description column to lower() method


df.description.str.lower()

df['description'] = df.description.str.lower()


# In[27]:Access the initial data


df.head(3)


# In[28]:Missing values


df.isnull().sum().sort_values(ascending = False)


# In[29]:Dropping missing values


df_new = df.dropna()


# In[30]:After dropping again checking missing values


df_new.isnull().sum()


# In[31]:Dataframe Information


df_new.info()


# In[32]:Access initial data


df_new.head()


# In[33]:Checking column datatypes


df_new.dtypes


# In[34]:Checking type of cust_id


df_new['cust_id']


# In[35]:Converting cust_id float type into integer type 


df_new['cust_id'] = df_new['cust_id'].astype('int64')


# In[36]:Accessing first five rows


df_new.head()


# In[37]:Dataframe Information


df_new.info()


# In[38]:Dataframe Statistical description


df_new.describe()


# In[39]:Rounding the values in dataframe


df_new.describe().round(2)


# In[40]:Removing negative values from quantity column


df_new.quantity > 0

con = df_new.quantity > 0

df_new = df_new[con]

df_new.describe().round(2)


# In[41]:Access initial data


df_new.head()


# In[42]:Checking total no.of rows and columns


df_new.shape


# In[43]:Adding the column - amount_spent


df_new['amount_spent'] = df_new['quantity']*df_new['unit_price']


# In[44]:Access initial data


df_new.head()


# In[45]:Access column names from Dataframe


for col in df.columns:
    print(col)


# In[46]:Rearranging column names


col_order = ['invoice_num','invoice_date','stock_code','description','quantity','unit_price','amount_spent','cust_id','country']

df_new = df_new[col_order]


# In[47]:Access initial data


df_new.head()


# In[48]:Access no.of rows and columns


df_new.shape


# In[49]:Access total no.of columns in the dataframe 


len(df_new.columns)


# In[50]:Access invoice_date column


df_new['invoice_date']

df_new.invoice_date


# In[51]:Access year value from invoice_date column


df_new['invoice_date'].dt.year


# In[52]:Access month value from invoice_date column


df_new['invoice_date'].dt.month


# In[53]:Access initial data


df_new.head(2)


# In[54]:Inserting year_month column in 2nd position


c1 = 'year_month'

v1 = df_new['invoice_date'].map(lambda col:100*(col.year)+col.month)

df_new.insert(loc=2,column=c1,value=v1)

df_new


# In[55]:Access initial data


df_new.head()


# In[56]:Adding month column to the existing dataframe


c2 = 'month'

v2 = df_new.invoice_date.dt.month

df_new.insert(loc=3,column=c2,value=v2)


# In[57]:Access initial data


df_new.head()


# In[58]:Access final data


df_new.tail()


# In[59]:Access invoice_date column


df_new.invoice_date


# In[60]:Access day of the week


df_new.invoice_date.dt.dayofweek


# In[61]:In pandas the day formate starts from 0 to 6
         Apply +1 to make Monday=1....until Sunday=7


c3='day'

v3=(df_new.invoice_date.dt.dayofweek)+1

df_new.insert(loc=4,column=c3,value=v3)


# In[62]:Access initial data


df_new.head()


# In[63]:Access invoice_date column


df_new.invoice_date


# In[64]:Adding hour column to the existing dataframe


df_new.invoice_date.dt.hour

c4='hour'

v4=df_new.invoice_date.dt.hour

df_new.insert(loc=5,column=c4,value=v4)


# In[65]:Access initial data


df_new.head()


# In[66]:Display columnnames


df_new.columns

for col in df_new.columns:
    print(col)


# In[67]:Exploratory Data Analysis


df_new.groupby(by=['cust_id']).count()

df_new.groupby(by=['cust_id','country']).count()

df_new.groupby(by=['cust_id','country'])['invoice_num'].count()

df_new.groupby(by=['cust_id','country'],as_index=False)['invoice_num'].count()

df_new.groupby(by=['cust_id','country'],as_index=False)['invoice_num'].count().head()

orders=df_new.groupby(by=['cust_id','country'],as_index=False)['invoice_num'].count()

orders


# In[68]:Check top 5 most no.of orders


orders.sort_values(by='invoice_num',ascending=False).head()


# In[69]:Visualizing - No.of orders for different customers

orders=df_new.groupby(by=['cust_id','country'],as_index=False)['invoice_num'].count()
plt.subplots(figsize=(15,6))
plt.plot(orders.cust_id,orders.invoice_num)
plt.xlabel('CustomersID')
plt.ylabel('Number of Orders')
plt.title('Number of Orders for different Customers')
plt.show()


# In[70]:Money spent by each customer


df_new.groupby(by=['cust_id','country']).sum()

df_new.groupby(by=['cust_id','country'])['amount_spent'].sum()

df_new.groupby(by=['cust_id','country'],as_index=False)['amount_spent'].sum()

money_spent=df_new.groupby(by=['cust_id','country'],as_index=False)['amount_spent'].sum()

money_spent


# In[71]:Check top 5 customers who spent highest money


money_spent.sort_values(by='amount_spent',ascending=False).head()


# In[72]:Check top ten customers who spent highest money


money_spent.sort_values(by='amount_spent',ascending=False).head(10)


# In[73]:Visualizing - Money spent for different customers


money_spent=df_new.groupby(by=['cust_id','country'],as_index=False)['amount_spent'].sum()
plt.subplots(figsize=(15,6))
plt.plot(money_spent.cust_id,money_spent.amount_spent)
plt.xlabel('CustomersID')
plt.ylabel('Money spent(Dollar)')
plt.title('Money Spent by different Customers')
plt.show()


# In[74]:Access initial data


df_new.head()


# In[75]:No.of orders for different months


color=sns.color_palette()

ax=df_new.groupby('invoice_num')['year_month'].unique().value_counts().sort_index().plot(kind='bar',color=color[0],figsize=(15,6))
ax.set_xlabel('Month and Year',fontsize=15)
ax.set_ylabel('Number of Orders',fontsize=15)
ax.set_title('Number of orders in different Months(1stDec2010 - 9thDec2011)',fontsize=15)
t=('Dec_10','Jan_11','Feb_11','Mar_11','Apr_11','May_11','Jun_11','July_11','Aug_11','Sep_11','Oct_11','Nov_11','Dec_11')
ax.set_xticklabels(t,rotation='horizontal',fontsize=13)
plt.show()


# In[76]:No.of orders per day


df_new.groupby('invoice_num')

df_new.groupby('invoice_num')['day']

df_new.groupby('invoice_num')['day'].unique()


# In[77]:Day wise sales bussiness


ax=df_new.groupby('invoice_num')['day'].unique().value_counts().sort_index().plot(kind='bar',color=color[0],figsize=(15,6))
ax.set_xlabel('Day',fontsize=15)
ax.set_ylabel('Number of Orders',fontsize=15)
ax.set_title('Number of orders for different Days',fontsize=15)
d=('Mon','Tue','Wed','Thur','Fri','Sun')
ax.set_xticklabels(d,rotation='horizontal',fontsize=15)
plt.show()


# In[78]:Statistical description for unit price


df_new.unit_price.describe()


# In[79]:Check the distribution of unit price


plt.subplots(figsize=(12,6))
sns.boxplot(df_new.unit_price)
plt.show()

df_free=df_new[df_new.unit_price==0]

df_free

df_free.year_month.value_counts().sort_index()

ax=df_free.year_month.value_counts().sort_index().plot(kind='bar',color=color[0],figsize=(12,6))
ax.set_xlabel('Month',fontsize=15)
ax.set_ylabel('Frequency',fontsize=15)
ax.set_title('Frequency for different Months(Dec2010 - Dec2011)',fontsize=15)
m=('Dec_10','Jan_11','Feb_11','Mar_11','Apr_11','May_11','July_11','Aug_11','Sep_11','Oct_11','Nov_11')
ax.set_xticklabels(m,rotation='horizontal',fontsize=13)
plt.show()


# In[80]:No.of orders for each country


group_country_orders=df_new.groupby('country')['invoice_num'].count().sort_values()

plt.subplots(figsize=(15,8))
group_country_orders.plot(kind='barh',fontsize=12,color=color[0])
plt.xlabel('Number of Orders',fontsize=12)
plt.ylabel('Country',fontsize=12)
plt.title('Number of Orders for different Countries',fontsize=12)
plt.show()


group_country_orders=df_new.groupby('country')['invoice_num'].count().sort_values()

del group_country_orders['United Kingdom']

plt.subplots(figsize=(15,8))
group_country_orders.plot(kind='barh',fontsize=12,color=color[0])
plt.xlabel('Number of Orders',fontsize=12)
plt.ylabel('Country',fontsize=12)
plt.title('Number of Orders for different Countries',fontsize=12)
plt.show()


# In[81]:Money spent by each country


group_country_amount_spent=df_new.groupby('country')['amount_spent'].sum().sort_values()

plt.subplots(figsize=(15,8))
group_country_amount_spent.plot(kind='barh',fontsize=12,color=color[0])
plt.xlabel('Money Spent(Dollar)',fontsize=12)
plt.ylabel('Country',fontsize=12)
plt.title('Money Spent by different Countries',fontsize=12)
plt.show()


group_country_amount_spent=df_new.groupby('country')['amount_spent'].sum().sort_values()

del group_country_amount_spent['United Kingdom']

plt.subplots(figsize=(15,8))
group_country_amount_spent.plot(kind='barh',fontsize=12,color=color[0])
plt.xlabel('Money Spent(Dollar)',fontsize=12)
plt.ylabel('Country',fontsize=12)
plt.title('Money Spent by different Countries',fontsize=12)
plt.show()


# This is Data Analysis




