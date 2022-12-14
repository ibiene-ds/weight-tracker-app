import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, date
import plotly.express as px



st.write("""
# Weight Tracker App
### **This simple app tracks daily weight and plots it for seamless tracking**
""")


# load historical data, import csv
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQyusdJWanOk38Wsm3HBSKnMohrn52K7W2Bz4SIbAOSlKHMb62IJXJT5iOHvmndVRuQXqCQKJ3iIkU7/pub?gid=0&single=true&output=csv"
df = pd.read_csv(url)

#check for and drop empty rows
df.dropna(axis =0, how = 'all', inplace = True)

#initiate empty lists
weight_list = []
date_list = []

# get today's date
today = str(date.today())

# ask user for input
today_weight = st.number_input('Enter your weight in pounds: ')

#append to empty lists
date_list.append(today)
weight_list.append(today_weight)

#create new dataframe
data = {'date': date_list, 
       'weight_lbs': weight_list}
new_df = pd.DataFrame(data)

# append new df to df and overwrite dataframe
df = pd.concat([df, new_df])

# drop nas
df.dropna(axis =0, how ='all', inplace = True)

#check for duplicate dates
df = df.drop_duplicates(subset = ['date'], keep = 'last')

# string to date transformation
df['date'] = df.date.astype('datetime64[ns]')

# save and overwrite history file
df.to_csv(url,index= False)

# plot historical data
st.markdown("**Daily Weight Tracker**")

fig = px.line(df, x="date", y="weight_lbs", markers = 'True')

st.plotly_chart(fig, use_container_width=True)

st.dataframe(df)

st.write("Good job!")

# st.download_button("Download file", 'history.csv')



