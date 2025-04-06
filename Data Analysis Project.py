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


# In[21]:Checking type of invoice_date column


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


# In[34]:


df_new = df.dropna()


# In[35]:


df_new.isnull().sum()


# In[36]:


df_new.info()


# In[37]:


df_new.head()


# In[38]:


df_new.dtypes


# In[39]:


df_new['cust_id']


# In[40]:


df_new['cust_id'] = df_new['cust_id'].astype('int64')


# In[41]:


df_new.head()


# In[42]:


df_new.info()


# In[43]:


df_new.describe()


# In[44]:


df_new.describe().round(2)


# In[45]:


df_new.quantity > 0


# In[46]:


con = df_new.quantity > 0


# In[47]:


df_new = df_new[con]


# In[48]:


df_new.describe().round(2)


# In[49]:


df_new.head()


# In[50]:


df_new.shape


# In[51]:


df_new['amount_spent'] = df_new['quantity']*df_new['unit_price']


# In[52]:


df_new.head()


# In[53]:


for col in df.columns:
    print(col)


# In[54]:


col_order = ['invoice_num','invoice_date','stock_code','description','quantity','unit_price','amount_spent','cust_id','country']


# In[55]:


df_new = df_new[col_order]


# In[56]:


df_new.head()


# In[57]:


df_new.shape


# In[58]:


len(df_new.columns)


# In[59]:


df_new['invoice_date']


# In[60]:


df_new.invoice_date


# In[61]:


df_new['invoice_date'].dt.year


# In[62]:


df_new['invoice_date'].dt.month


# In[63]:


df_new.head(2)


# In[65]:


c1 = 'year_month'


# In[66]:


v1 = df_new['invoice_date'].map(lambda col:100*(col.year)+col.month)


# In[67]:


df_new.insert(loc=2,column=c1,value=v1)


# In[68]:


df_new


# In[69]:


df_new.head()


# In[70]:


c2 = 'month'


# In[71]:


v2 = df_new.invoice_date.dt.month


# In[72]:


df_new.insert(loc=3,column=c2,value=v2)


# In[73]:


df_new.head()


# In[74]:


df_new.tail()


# In[75]:


df_new.invoice_date


# In[76]:


df_new.invoice_date.dt.dayofweek


# In[77]:


c3='day'


# In[78]:


v3=(df_new.invoice_date.dt.dayofweek)+1


# In[79]:


df_new.insert(loc=4,column=c3,value=v3)


# In[80]:


df_new.head()


# In[81]:


df_new.invoice_date


# In[82]:


df_new.invoice_date.dt.hour


# In[83]:


c4='hour'


# In[84]:


v4=df_new.invoice_date.dt.hour


# In[85]:


df_new.insert(loc=5,column=c4,value=v4)


# In[86]:


df_new.head()


# In[87]:


df_new.columns


# In[88]:


for col in df_new.columns:
    print(col)


# In[89]:


df_new.groupby(by=['cust_id']).count()


# In[90]:


df_new.groupby(by=['cust_id','country']).count()


# In[91]:


df_new.groupby(by=['cust_id','country'])['invoice_num'].count()


# In[92]:


df_new.groupby(by=['cust_id','country'],as_index=False)['invoice_num'].count()


# In[93]:


df_new.groupby(by=['cust_id','country'],as_index=False)['invoice_num'].count().head()


# In[95]:


orders=df_new.groupby(by=['cust_id','country'],as_index=False)['invoice_num'].count()


# In[96]:


orders


# In[97]:


orders.sort_values(by='invoice_num',ascending=False).head()


# In[98]:


orders=df_new.groupby(by=['cust_id','country'],as_index=False)['invoice_num'].count()


# In[100]:


plt.subplots(figsize=(15,6))
plt.plot(orders.cust_id,orders.invoice_num)
plt.xlabel('CustomersID')
plt.ylabel('Number of Orders')
plt.title('Number of Orders for different Customers')
plt.show()


# In[101]:


df_new.groupby(by=['cust_id','country']).sum()


# In[102]:


df_new.groupby(by=['cust_id','country'])['amount_spent'].sum()


# In[103]:


df_new.groupby(by=['cust_id','country'],as_index=False)['amount_spent'].sum()


# In[104]:


money_spent=df_new.groupby(by=['cust_id','country'],as_index=False)['amount_spent'].sum()


# In[105]:


money_spent


# In[106]:


money_spent.sort_values(by='amount_spent',ascending=False).head()


# In[107]:


money_spent.sort_values(by='amount_spent',ascending=False).head(10)


# In[115]:


money_spent=df_new.groupby(by=['cust_id','country'],as_index=False)['amount_spent'].sum()


# In[116]:


plt.subplots(figsize=(15,6))
plt.plot(money_spent.cust_id,money_spent.amount_spent)
plt.xlabel('CustomersID')
plt.ylabel('Money spent(Dollar)')
plt.title('Money Spent by different Customers')
plt.show()


# In[117]:


df_new.head()


# In[118]:


color=sns.color_palette()


# In[120]:


ax=df_new.groupby('invoice_num')['year_month'].unique().value_counts().sort_index().plot(kind='bar',color=color[0],figsize=(15,6))
ax.set_xlabel('Month and Year',fontsize=15)
ax.set_ylabel('Number of Orders',fontsize=15)
ax.set_title('Number of orders in different Months(1stDec2010 - 9thDec2011)',fontsize=15)
t=('Dec_10','Jan_11','Feb_11','Mar_11','Apr_11','May_11','Jun_11','July_11','Aug_11','Sep_11','Oct_11','Nov_11','Dec_11')
ax.set_xticklabels(t,rotation='horizontal',fontsize=13)
plt.show()


# In[157]:


df_new.groupby('invoice_num')


# In[158]:


df_new.groupby('invoice_num')['day']


# In[159]:


df_new.groupby('invoice_num')['day'].unique()


# In[164]:


ax=df_new.groupby('invoice_num')['day'].unique().value_counts().sort_index().plot(kind='bar',color=color[0],figsize=(15,6))
ax.set_xlabel('Day',fontsize=15)
ax.set_ylabel('Number of Orders',fontsize=15)
ax.set_title('Number of orders for different Days',fontsize=15)
d=('Mon','Tue','Wed','Thur','Fri','Sun')
ax.set_xticklabels(d,rotation='horizontal',fontsize=15)
plt.show()


# In[165]:


df_new.unit_price.describe()


# In[168]:


plt.subplots(figsize=(12,6))
sns.boxplot(df_new.unit_price)
plt.show()


# In[167]:


df_free=df_new[df_new.unit_price==0]


# In[169]:


df_free


# In[170]:


df_free.year_month.value_counts().sort_index()


# In[173]:


ax=df_free.year_month.value_counts().sort_index().plot(kind='bar',color=color[0],figsize=(12,6))
ax.set_xlabel('Month',fontsize=15)
ax.set_ylabel('Frequency',fontsize=15)
ax.set_title('Frequency for different Months(Dec2010 - Dec2011)',fontsize=15)
m=('Dec_10','Jan_11','Feb_11','Mar_11','Apr_11','May_11','July_11','Aug_11','Sep_11','Oct_11','Nov_11')
ax.set_xticklabels(m,rotation='horizontal',fontsize=13)
plt.show()


# In[174]:


group_country_orders=df_new.groupby('country')['invoice_num'].count().sort_values()


# In[175]:


plt.subplots(figsize=(15,8))
group_country_orders.plot(kind='barh',fontsize=12,color=color[0])
plt.xlabel('Number of Orders',fontsize=12)
plt.ylabel('Country',fontsize=12)
plt.title('Number of Orders for different Countries',fontsize=12)
plt.show()


# In[176]:


group_country_orders=df_new.groupby('country')['invoice_num'].count().sort_values()


# In[177]:


del group_country_orders['United Kingdom']


# In[178]:


plt.subplots(figsize=(15,8))
group_country_orders.plot(kind='barh',fontsize=12,color=color[0])
plt.xlabel('Number of Orders',fontsize=12)
plt.ylabel('Country',fontsize=12)
plt.title('Number of Orders for different Countries',fontsize=12)
plt.show()


# In[179]:


group_country_amount_spent=df_new.groupby('country')['amount_spent'].sum().sort_values()


# In[180]:


plt.subplots(figsize=(15,8))
group_country_amount_spent.plot(kind='barh',fontsize=12,color=color[0])
plt.xlabel('Money Spent(Dollar)',fontsize=12)
plt.ylabel('Country',fontsize=12)
plt.title('Money Spent by different Countries',fontsize=12)
plt.show()


# In[181]:


group_country_amount_spent=df_new.groupby('country')['amount_spent'].sum().sort_values()


# In[182]:


del group_country_amount_spent['United Kingdom']


# In[183]:


plt.subplots(figsize=(15,8))
group_country_amount_spent.plot(kind='barh',fontsize=12,color=color[0])
plt.xlabel('Money Spent(Dollar)',fontsize=12)
plt.ylabel('Country',fontsize=12)
plt.title('Money Spent by different Countries',fontsize=12)
plt.show()


# In[ ]:




