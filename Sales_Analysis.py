#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


sales_analysis = pd.read_excel("superstore_sales.xlsx")


# In[3]:


sales_analysis.info


# In[4]:


from datetime import datetime
initial_date_format = "%Y-%m-%d"
new_date_format = "%d/%m/%Y"


# In[5]:


sa = sales_analysis


# In[6]:


sa.head()


# In[7]:


sa.describe()


# In[8]:


sa.shape


# In[9]:


from datetime import datetime
initial_date_format = "%Y-%m-%d"
new_date_format = "%d/%m/%Y"


# In[10]:


sa.head()


# In[11]:


sa.set_index("order_id")


# In[12]:


sa = sa.set_index("order_id")


# In[13]:


sa.head()


# In[14]:


def sale (sales):
    if sales < 100.000 :
        return "Small Sale"
    elif sales >= 100.00 and sales < 300.000 :
        return "Medium Sale"
    else:
        return "Max Sale"


# In[15]:


sa["sale"] = sa["sales"].apply(sale)


# In[16]:


sa.head()


# In[17]:


mean_profit_by_region = sa.groupby("region")["profit"].mean()


# In[18]:


mean_profit_by_region


# In[19]:


profit_by_region = sa.groupby("region")["profit"].sum()


# In[20]:


profit_by_region


# In[21]:


max_profit_region = profit_by_region.idxmax()
max_profit = profit_by_region[max_profit_region]


# In[22]:


max_profit


# In[23]:


max_profit_region


# In[24]:


profit_by_region.nlargest(5)


# In[25]:


mean_sales_by_product = sa.groupby("product_name")["sales"].mean()


# In[26]:


mean_sales_by_product


# In[27]:


sales_by_product = sa.groupby("product_name")["sales"].max()


# In[28]:


sales_by_product.head()


# In[29]:


max_sales_product = sales_by_product.idxmax()


# In[30]:


max_sales_product


# In[31]:


max_sales = sales_by_product[max_sales_product]


# In[32]:


max_sales


# In[33]:


print (f"The product with the highest total sales is '{max_sales_product}'with total sales of {max_sales}.")


# In[34]:


orders_by_year = sa.groupby("year").size()


# In[35]:


orders_by_year


# In[36]:


max_order_year = orders_by_year.idxmax()


# In[37]:


max_order_year


# In[38]:


min_order_year = orders_by_year.idxmin()


# In[39]:


min_order_year


# In[40]:


sorted_order_by_year = orders_by_year.sort_values(ascending=False)


# In[41]:


sorted_order_by_year


# In[42]:


sa["order_date"] = pd.to_datetime(sa["order_date"])
sa["ship_date"] = pd.to_datetime(sa["ship_date"])


# In[43]:


sa["order_duration"] = sa["ship_date"] - sa["order_date"]


# In[44]:


mean_order_duration = sa["order_duration"].mean()


# In[45]:


mean_order_duration


# In[46]:


sa.head()


# In[47]:


discount_by_country = sa.groupby("country")["discount"].mean()


# In[48]:


discount_by_country


# In[50]:


jupyter nbconvert --to pdf Sales_Analysis.ipynb

