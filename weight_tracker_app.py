
import pandas as pd
import numpy as np
from datetime import datetime, date
import plotly.express as px

weight_list = [147, 145]
date_list = ['2022-10-08', '2022-10-15']

today = str(date.today())
date_list.append(today)
today_weight = float(input('Enter your weight in pounds: '))
weight_list.append(today_weight)

data = {'date': date_list, 
       'weight_lbs': weight_list}
df = pd.DataFrame(data)
df['date'] = df.date.astype('datetime64[ns]')

fig = px.line(df, x="date", y="weight_lbs", title='Weight Tracker', markers = 'True')
fig.show()

print(df)
