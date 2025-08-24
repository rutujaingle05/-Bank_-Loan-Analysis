#!/usr/bin/env python
# coding: utf-8

# 
# ### BANK LAON ANALYSIS Report

# ## Import Libaries

# In[104]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings 
import plotly.express as px


# In[105]:


import pip
pip.main(["install","matplotlib"])


# In[106]:


# required for building interactive dashboard
import panel as pn
pn.extension('tabulator')
import hvplot.pandas
import holoviews as hv 
hv.extension('bokeh')


# In[107]:


df = pd.read_excel("D:/projects/financial_loan.xlsx")


# In[108]:


df .head()


# In[109]:


df.tail()


# In[110]:


df.columns


# ### Metadata of Data

# In[111]:


print("No of Rows :",df.shape[0])


# In[112]:


print("NO of Column:", df.shape[1])


# In[113]:


df.info()


# ### Data Tpes

# In[114]:


df.dtypes


# In[115]:


df.describe()


# ### KPI

# ### Total Loan Application

# In[116]:


total_loan_application = df['id'].count()
print("Total Loan Applications:", total_loan_application)


# In[117]:


# Activate Panel extension
pn.extension(sizing_mode="stretch_width")

# Example dataframe (replace with your own df)
# df = pd.read_csv("your_file.csv")

# KPI calculation
total_loan_application = df['id'].count()

# Create KPI card
kpi_card = pn.Card(
    pn.pane.Markdown(f"### 📊 Total Loan Applications\n\n**{total_loan_application:,}**"),
    title="Loan KPI",
    width=300,
    height=150,
    styles={'background': '#f5f5f5', 'color': '#333', 'font-size': '16px'}
)

# Layout
dashboard = pn.Row(kpi_card)

dashboard.servable()


# ### MTD Total Loan Applications

# In[118]:


latest_issue_date = df['issue_date'].max()
latest_year = latest_issue_date.year
latest_month = latest_issue_date.month

mtd_data  = df[(df['issue_date'].dt.year == latest_year) & (df['issue_date'].dt.month == latest_month)]

mtd_loan_applications = mtd_data['id'].count()

print(f"MTD Loan Applications (for {latest_issue_date.strftime('%B %Y')}):{mtd_loan_applications}")


# In[119]:


import pandas as pd
import panel as pn
import datetime as dt

pn.extension(sizing_mode="stretch_width")

# Example dataframe (replace with your actual df)
# df = pd.read_csv("your_data.csv")
# Ensure issue_date is in datetime format
# df['issue_date'] = pd.to_datetime(df['issue_date'])

# --- KPI Calculation ---
latest_issue_date = df['issue_date'].max()
latest_year = latest_issue_date.year
latest_month = latest_issue_date.month

mtd_data  = df[(df['issue_date'].dt.year == latest_year) & 
               (df['issue_date'].dt.month == latest_month)]

mtd_loan_applications = mtd_data['id'].count()

# --- Panel KPI Card ---
kpi_card = pn.Card(
    pn.pane.Markdown(
        f"""
        ### 📊 MTD Loan Applications  
        **{mtd_loan_applications:,}**  
        _for {latest_issue_date.strftime('%B %Y')}_
        """,
        style={"font-size": "20px", "text-align": "center"}
    ),
    title="KPI Overview",
    collapsed=False,
    width=300,
    height=180
)

# Display panel
dashboard = pn.Row(kpi_card)
dashboard.servable()


# ### Total Fundated Amount

# In[120]:


total_funded_amount = df['loan_amount'].sum()
total_funded_amount_millions = total_funded_amount/1000000
print("Total Fundated Amount: ${:.2f}M".format(total_funded_amount_millions))


# ### MTD -Total Fundated Amount

# In[121]:


latest_issue_date = df['issue_date'].max()
latest_year = latest_issue_date.year
latest_month = latest_issue_date.month

mtd_data  = df[(df['issue_date'].dt.year == latest_year) & (df['issue_date'].dt.month == latest_month)]

mtd_total_funded_amount = mtd_data['loan_amount'].sum()

mtd_total_funded_amount_millions = mtd_total_funded_amount/1000000

print("MTD Total Funded Amount: ${:.2f}M".format(mtd_total_funded_amount_millions))


# ### Total Amount Received

# In[122]:


total_amount_received = df['total_payment'].sum()
total_amount_received_millions = total_funded_amount/1000000
print("Total  Amount Received: ${:.2f}M".format(total_amount_received_millions))


# ### Month To Date Amount Receivied

# In[123]:


latest_issue_date = df['issue_date'].max()
latest_year = latest_issue_date.year
latest_month = latest_issue_date.month

mtd_data  = df[(df['issue_date'].dt.year == latest_year) & (df['issue_date'].dt.month == latest_month)]

mtd_total_amount_received = mtd_data['total_payment'].sum()

mtd_total_amount_received_millions = mtd_total_amount_received/1000000

print("MTD Total Funded Amount Received: ${:.2f}M".format(mtd_total_amount_received_millions))


# ###  Average Interest Rate 

# In[124]:


average_interest_rate = df['int_rate'].mean()*100
print("Avg Interest Rate:{:.2f}%".format(average_interest_rate))


# ### Average  Dept-To-Income Ratio(DTI)

# In[125]:


average_dti = df['dti'].mean()*100
print("Average DTI:{:.2f}%".format(average_dti))


# ### Good Loan Matrix
# 

# In[126]:


#goodloan
good_loans = df[df['loan_status'].isin(["Fully Paid","Current"])]

total_loan_applications = df['id'].count()

good_loan_applications = df['id'].count()
print("Good Loan Applications:",good_loan_applications)


# In[127]:


# goodloan Funded Amount
good_loan_funded_amount = good_loans['loan_amount'].sum()

good_loan_received = good_loans['total_payment'].sum()

good_loan_funded_amount_millions = good_loan_funded_amount / 1000000
good_loan_received_millions = good_loan_received / 1000000

good_loan_percentage = (good_loan_applications / total_loan_applications) * 100

print("Good Loan Funded Amount (in millions): ${:.2f}M".format(good_loan_funded_amount_millions))
print("Good Loan Received (in millions): ${:.2f}M".format(good_loan_received_millions))
print("Good Loan Percentage: ${:.2f}%".format(good_loan_percentage))


# ### Bad loan Matrics

# In[128]:


bad_loans = df[df['loan_status'].isin(["Fully Paid","Current"])]

total_loan_applications = df['id'].count()

bad_loan_applications = df['id'].count()

bad_loan_funded_amount = bad_loans['loan_amount'].sum()
bad_loan_received = bad_loans['total_payment'].sum()

bad_loan_funded_amount_millions = bad_loan_funded_amount / 1000000
bad_loan_received_millions = bad_loan_received / 1000000

bad_loan_percentage = (bad_loan_applications / total_loan_applications) * 100
print("Bad Loan Applications:",bad_loan_applications)
print("Bad Loan Funded Amount (in millions): ${:.2f}M".format(bad_loan_funded_amount_millions))
print("Bad Loan Received (in millions): ${:.2f}M".format(bad_loan_received_millions))
print("Bad Loan Percentage: ${:.2f}%".format(bad_loan_percentage))


# ### Monthly Trend By Issue Date For Total Funded Amount

# In[129]:


monthly_funded = (
  df.sort_values('issue_date')
    .assign(month_name=lambda x: x['issue_date'].dt.strftime('%b %y'))
    .groupby('month_name', sort=False)['loan_amount']
    .sum()
    .div(1_000_000)
    .reset_index(name='loan_amount_millions')
)
plt.figure(figsize=(10,5))
plt.fill_between(monthly_funded['month_name'], monthly_funded['loan_amount_millions'], color='white', alpha=0.5)
plt.plot(monthly_funded['month_name'], monthly_funded['loan_amount_millions'], color='blue',linewidth=2)

for i, row in  monthly_funded.iterrows():
   plt.text(i, row['loan_amount_millions'] + 0.1, f"{row['loan_amount_millions']:.2f}",
           ha='center', va='bottom', fontsize=9, rotation=0, color='black')



plt.title('Total Funded Amount by Month', fontsize=14)
plt.xlabel('Month')
plt.ylabel('Funded Amount (₹ Millions)')
plt.xticks(ticks=range(len(monthly_funded)), labels=monthly_funded['month_name'], rotation=45)

plt.grid(True, linestyle='--',alpha=0.6)
plt.tight_layout()
plt.show()





# ###  Monthly Trends by Issue Date for Total Amount Received

# ### Monthly Trends by Issue Date for Total Loan Application

# In[130]:


monthly_applications = (
   df.sort_values('issue_date')
     .assign(month_name=lambda x: x['issue_date'].dt.strftime('%b %y'))
     .groupby('month_name', sort=False)['id']
     .count()
     .reset_index(name='loan_applications_count')
 )
plt.figure(figsize=(10,5))
plt.fill_between(monthly_applications['month_name'], monthly_applications['loan_applications_count'], 
                 color='white', alpha=0.5)
plt.plot(monthly_applications['month_name'], monthly_applications['loan_applications_count'], 
         color='green',linewidth=2)

for i, row in  monthly_applications.iterrows():
    plt.text(i, row['loan_applications_count'] + 0.5, f"{row['loan_applications_count']:.2f}",
            ha='center', va='bottom', fontsize=9, rotation=0, color='black')
    


plt.title('Total Loan Applications by Month', fontsize=14)
plt.xlabel('Month')
plt.ylabel('Number of Applications')
plt.xticks(ticks=range(len(monthly_applications)), 
           labels=monthly_applications['month_name'], rotation=45)

plt.grid(True, linestyle='--',alpha=0.6)
plt.tight_layout()
plt.show()


# ### Regional Analysis by State for Total Funded Amount 

# In[137]:


state_funding = df.groupby('address_state')['loan_amount'].sum().sort_values(ascending=True)
state_funding_thousand = state_funding / 1000
plt.figure(figsize =(10,8))
bars = plt.barh(state_funding_thousand.index,state_funding_thousand.values,color='darkblue')

for bar in  bars:
    width = bar.get_width()
    plt.text(width + 10, bar.get_y()+ bar.get_height() / 2 ,
            f'{width:,.0f}k', va='center',fontsize=9)
plt.title('Total Funded Amount By State(in ₹ Thousands)')
plt.xlabel('Funded Amount (₹ \'000)')
plt.ylabel('State')
plt.tight_layout()
plt.show()


# ### Loan Term Anlaysis  by Total Funded Amount

# In[132]:


term_funding_millions = df.groupby('term')['loan_amount'].sum() / 1_000_000

plt.figure(figsize=(5,5))
plt.pie(
    term_funding_millions,
    labels=term_funding_millions.index,
    autopct=lambda p: f"{p:.1f}%\n({p * term_funding_millions.sum() / 100:.1f}M)",
    startangle=90,
    wedgeprops={'width':0.4}
)

# Add white circle in the middle (donut chart)
centre_circle = plt.Circle((0,0), 0.70, fc='white')
plt.gca().add_artist(centre_circle)

plt.title("Total Funded Amount By Term ($ in millions)")
plt.tight_layout()
plt.show()


# ### Employee  lenght by Total Funded Amount

# In[133]:


# Group loan amount by employee length (convert to thousands)
emp_funding_thousands = (
    df.groupby('emp_length')['loan_amount']
      .sum()
      .div(1000)  # convert to thousands
      .sort_values(ascending=True)
)

plt.figure(figsize =(10,6))
bars = plt.barh(emp_funding_thousands.index, emp_funding_thousands.values, color='orange')

# Add labels at the end of bars
for bar in bars:
    width = bar.get_width()
    plt.text(width + 50, bar.get_y() + bar.get_height() / 2,
             f'{width:,.0f}k', va='center', fontsize=9)

plt.title('Total Funded Amount By Employee Length (in ₹ Thousands)')
plt.xlabel('Funded Amount (₹ Thousands)')
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()


# ### Loan Purpose by Total Funded Amount 

# In[134]:


purpose_funding_millions = (
    df.groupby('emp_length')['loan_amount']
      .sum()
      .sort_values ()/ 1000000  # convert to thousands
      
)

plt.figure(figsize =(10,6))
bars = plt.barh(emp_funding_thousands.index, emp_funding_thousands.values, color='skyblue')

# Add labels at the end of bars
for bar in bars:
    width = bar.get_width()
    plt.text(width + 50, bar.get_y() + bar.get_height() / 2,
             f'{width:,.0f}k', va='center', fontsize=9)

plt.title('Total Funded Amount By Employee Length (in ₹ Thousands)')
plt.xlabel('Funded Amount (₹ Thousands)')
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()


# ###  Home Ownership by Total Funded Amount

# In[135]:


import plotly.express as px

home_funding = df.groupby('home_ownership')['loan_amount'].sum().reset_index()
home_funding['loan_amount_millions'] = home_funding['loan_amount'] / 1_000_000

fig = px.treemap(
    home_funding,
    path=['home_ownership'],
    values='loan_amount_millions',
    color='loan_amount_millions',
    color_continuous_scale='Blues',  # Changed from 'Yellow' to valid scale
    title='Total Funded Amount by Home Ownership (₹ Millions)'
)

fig.show()


# In[ ]:





# In[ ]:





# In[ ]:




