# Load the necessary packages and modules
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Compute the Bollinger Bands 
def calculate_BBANDS(data, window):
    MA = data['Close'].rolling(window=window).mean()
    SD = data['Close'].rolling(window=window).std()
    data['MiddleBand'] = MA
    data['UpperBand'] = MA + (2 * SD)
    data['LowerBand'] = MA - (2 * SD)
    return data
 
# Retrieve the Google stock data from Yahoo finance
data = yf.download('NVDA', start="2020-01-01", end="2024-12-31")
data.tail()

# Compute the Bollinger Bands for Google using the 50-day Moving average
n = 50
data_with_bbands = calculate_BBANDS(data, n)

# Create the plot
plt.figure(figsize=(10,7))

# Set the title and axis labels
plt.title('Bollinger Bands')
plt.xlabel('Date')
plt.ylabel('Price')

# Plot the closing price and Bollinger Bands
plt.plot(data_with_bbands['Close'], lw=1, label='Close Price')
plt.plot(data_with_bbands['UpperBand'], 'g', lw=1, label='Upper Band')
plt.plot(data_with_bbands['MiddleBand'], 'r', lw=1, label='Middle Band')
plt.plot(data_with_bbands['LowerBand'], 'g', lw=1, label='Lower Band')

# Add a legend to the axis
plt.legend()

plt.show()
