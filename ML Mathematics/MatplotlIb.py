import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

stocks_df = pd.read_csv('stocks.csv')
##print(stocks_df)

##Direct Line Plot
stocks_df.plot(x='Date', y='IBM',
               label='IBM Stocks',
               linewidth=1)
plt.ylabel('Price')
##plt.legend(loc='upper left')
plt.title('LOL')

stocks_df.plot(x = 'Date', y = 'sp500',
               label ='S&P500 Stocks',
               linewidth =1,
               color = 'red' )
plt.ylabel('Price')
plt.title('S&P500 stocks over the years')
plt.show()
#############################################################

##Scatter Plot
daily_df = pd.read_csv('daily_returns.csv')

x = daily_df['AAPL']
y = daily_df['sp500']
plt.scatter(x, y)
plt.xlabel('AAPL')
plt.ylabel('S&P500')
plt.title('AAPL vs. S&P500 Return Scatter Graph')
plt.show()

X = daily_df['GOOG']
Y = daily_df['sp500']
plt.scatter(X,Y)
plt.xlabel('GOOG Daily Return')
plt.ylabel('S&P500 Daily Return')
plt.title('GOOG vs. S&P500 Daily Return Scatter Plot')
plt.show()
###################################################################

##Pie Chart 
values = [20,55,5,17,3]
colors = ['r','g','b','y','m']
labels = ['Sharad','Anand','Shruti','Prashant','Pratik']
explode = [0,0,0,0.1,0]
plt.figure(figsize=(10,10))
plt.pie(values, colors = colors, labels = labels, explode = explode);
plt.title('Dummies')
plt.show()

values = [20,20,20,20,20]
colors = ['r','g','b','y','m']
labels = ['Sharad','Anand','Shruti','Prashant','Pratik']
explode = [0.1,0,0,0.1,0]
plt.figure(figsize=(10,10))
plt.pie(values, colors = colors, labels = labels, explode = explode)
plt.title('Dummies')
plt.show()
##################################################################

##Histogram
mu = daily_df['AAPL'].mean()
sigma = daily_df['AAPL'].std()
##print(mu)
##print(sigma)
num_bins = 50
plt.figure(figsize = (7,7))
plt.hist(daily_df['AAPL'], num_bins);
plt.title('Apple Histogram \nMU = '+str(mu)+'\nSTD = '+str(sigma))
plt.grid()
plt.show()

mu = daily_df['GOOG'].mean()
sigma = daily_df['GOOG'].std() 
num_bins = 30
plt.figure(figsize=(8,8))
plt.hist(daily_df['GOOG'], num_bins);
plt.title('GOOG Histogram \nMU = '+str(mu)+'\nSTD = '+str(sigma))
plt.grid()
plt.show()
#################################################################

##Multiple Plots
stocks_df.plot(x ='Date', y = ['T','BA','TSLA'], linewidth = 1)
plt.title('Multiple Line Plots on a Single Plot')
plt.ylabel('Prices')
plt.grid()
plt.show()

stocks_df.plot(x ='Date', y = ['AAPL','sp500','GOOG'], linewidth = 1)
plt.title('Multiple Line Plots on a Single Plot')
plt.ylabel('Prices')
plt.grid()
plt.legend(loc = 'upper center')
plt.show()
#################################################################

##SubPlots
##Side to Side plots
plt.figure(figsize = (8,8))
plt.subplot(1,2,1)
plt.grid()
plt.plot(stocks_df['AAPL'], 'r--')
plt.legend(['Apple Stocks'])
plt.subplot(1,2,2)
plt.grid()
plt.plot(stocks_df['GOOG'], 'b--')
plt.legend(['Google Stocks'])
plt.show()

##Plots on top of each other
plt.figure(figsize = (7,7))
plt.subplot(2,1,1)
plt.grid()
plt.plot(stocks_df['sp500'],'g--')
plt.legend(['S&P 500 Stocks'])
plt.subplot(2,1,2)
plt.grid()
plt.plot(stocks_df['BA'],'m--')
plt.legend(['BA Stocks'])
plt.show()

plt.figure(figsize = (21,7))
plt.subplot(1,3,1)
plt.grid()
plt.plot(stocks_df['GOOG'], 'r--')
plt.legend(['Google Stocks'])
plt.subplot(1,3,2)
plt.grid()
plt.plot(stocks_df['AAPL'], 'g--')
plt.legend(['Apple Stocks'])
plt.subplot(1,3,3)
plt.grid()
plt.plot(stocks_df['sp500'], 'b--')
plt.legend(['S&P500 Stocks'])
plt.show()
#############################################################

##3D Plot
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(1,1,1, projection='3d')
x = list(range(1,11))
y = list(np.arange(1,20,2))
z = list(np.random.randint(1,30,10))
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.scatter(x, y, z, c = 'red',marker = 'o')
plt.show()

daily_df = pd.read_csv('daily_returns.csv')
fig = plt.figure(figsize=(10,10))
ax1 = fig.add_subplot(1,1,1, projection = '3d')
x = daily_df['sp500']
y = daily_df['GOOG']
z = daily_df['AAPL']
ax1.set_xlabel('S&P500')
ax1.set_ylabel('Google')
ax1.set_zlabel('Apple')
ax1.scatter(x,y,z, c = 'blue', marker = '^')
plt.show()
#########################################################

##BoxPlot
np.random.seed(20)
data1 = np.random.normal(200, 20, 2000)
data2 = np.random.normal(60, 30, 2000)
data3 = np.random.normal(70, 20, 2000)
data4 = np.random.normal(40, 5, 2000)
data = [data1, data2, data3, data4]

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(1,1,1)
bp = ax.boxplot(data)
plt.show()

np.random.seed(20)
data1 = np.random.normal(200, 20, 2000)
data2 = np.random.normal(60, 30, 2000)
data3 = np.random.normal(70, 20, 2000)
data4 = np.random.normal(40, 5, 2000)
data5 = np.random.normal(800, 100, 2000)
data = [data1, data2, data3, data4, data5]

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(1,1,1)
bp = ax.boxplot(data)
plt.show()
