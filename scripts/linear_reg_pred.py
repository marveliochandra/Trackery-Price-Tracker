import pandas as pd
import numpy as np
from datetime import date
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
#-1 return means empty array
#-10 return means no data or less than 5 data is available
#-404 return means dataframe conversion error


#note, need future integration. however pretty much done for the linear regression. just need array of 2d size.
#doesnt truly predict next day, just the latest data date +1. idk the format for incoming data date, so hold on for now
#also, doesnt have any model accuracy evaluation, might need it someday.
#the prediction should only be coming out positive, since there is no negative price. so negative price will be used as a return error.
def lin_reg(data):

    if not data:
        return -1
    
    try:
        df=pd.DataFrame(data,columns=['Date','Price'])
    except ValueError:
        return -404
    
    if df.shape[0]<5:
        return -10
    
    #BUAT LINREG BIASA
    # df.insert(0,"Time",df.index)
   
    # X = df['Time'].values.reshape(-1, 1)
    # y = df['Price'].values.reshape(-1, 1)
    
    # split = int(0.8 * len(X))

    # X_train = X[:split]
    # X_test = X[split:]
    # y_train = y[:split]
    # y_test = y[split:]
    # model = LinearRegression()
    # model.fit(X_train,y_train)

    # #model test here, not required tbh

    # next_day = X_test[-1]+1
    # predicted_price = model.predict([next_day])[0][0]

    #buat timeseries
    
    past_days = 3
    df2 = df[['Price']]
   
    def TimeLagTransform(data, past_days):
        cols = data.columns
        for i in reversed(range(past_days+1)):
            for j in cols:
                if i>0:
                    data['%s(t-%d)'%(j,i)] = data[j].shift(periods=i)
                else:
                    data[f"{j}-Target"] = data[j].shift(periods=i)
        return data
    df2 = TimeLagTransform(data=df2.copy(), past_days=past_days).drop(columns=df2.columns, axis=1).dropna()
    split = int(len(df2)-1)
    train = df2.iloc[:split]
    test = df2.iloc[split:]
    X_train, y_train = train.iloc[:, :-1], train.iloc[:, -1:]
    X_test, y_test = test.iloc[:, :-1], test.iloc[:, -1:]
    nextday=pd.DataFrame(X_test,columns=['Price(t-3)','Price(t-2)'])
    nextday.insert(2,"Price(t-1)",y_test)
    print(nextday)
    model = LinearRegression()
    model.fit(X_train,y_train)
    predicted_price = model.predict(nextday)[0][0]

    plt.figure(figsize=(10,6))
    plt.title('Last 7 day price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.plot(df['Date'][-7:], df['Price'][-7:],marker = ".")
    plt.savefig('static/images/plot.png')

    return predicted_price
