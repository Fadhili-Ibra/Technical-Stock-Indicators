# Load the necessary packages and modules
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Returns the Force Index 
def ForceIndex(data, ndays): 
    FI = pd.Series(data['Close'].diff(ndays) * data['Volume'], name = 'ForceIndex') 
    data = data.join(FI) 
    return data


# Retrieve the Apple Inc. data from Yahoo finance
data = yf.download("AAPL", start="2020-01-01", end="2022-04-30") 

# Compute the Force Index for AAPL
n = 1
AAPL_ForceIndex = ForceIndex(data,n)
AAPL_ForceIndex['ForceIndex']