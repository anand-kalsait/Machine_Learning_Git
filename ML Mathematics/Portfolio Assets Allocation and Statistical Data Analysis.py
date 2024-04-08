import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from copy import copy
from scipy import stats
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go

def normalize(df):
  x = df.copy()
  for i in x.columns[1:]:
    x[i] = x[i]/x[i][0]
  return x

def inact_plot(df, title):
  fig = px.line(title = title)
  for i in df.columns[1:]:
    fig.add_scatter(x = df['Date'], y = df[i], name = i)
  fig.show()

stocks_df = pd.read_csv('stock.csv')

normal_stocks_df = normalize(stocks_df)

# inact_plot(stocks_df, 'Stocks prices without normalization')
# inact_plot(normal_stocks_df, 'Stocks prices with normalization')
 
np.random.seed()

weights = np.array(np.random.random(9))
weights = weights/np.sum(weights)

normal_stocks_df = normal_stocks_df.drop(columns = ['Date'], axis = 0)
for counter, stocks in enumerate(normal_stocks_df.columns):
  normal_stocks_df[stocks] = normal_stocks_df[stocks]*weights[counter]*1000000

normal_stocks_df['portfolio in $'] = normal_stocks_df.sum(axis = 1)
normal_stocks_df['daily percent return'] = 0.0000

for i in range(1, len(stocks_df)):
  normal_stocks_df['daily percent return'][i] = ((normal_stocks_df['portfolio in $'][i]-normal_stocks_df['portfolio in $'][i-1]) / normal_stocks_df['portfolio in $'][i-1])*100

print(normal_stocks_df)
inact_plot(normal_stocks_df, 'Normalized stocks with total portfolio and percernt daily return')