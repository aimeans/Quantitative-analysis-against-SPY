import yfinance as yf
import pandas as pd
import csv
tickerStrings = ['AAPL', 'TSLA', 'NVDA','AMZN','BABA','SPY']
df_list = list()
for ticker in tickerStrings:
    data = yf.download(ticker, group_by="Ticker", period='36mo')
    data['ticker'] = ticker  # add this column because the dataframe doesn't contain a column with the ticker
    df_list.append(data)

# combine all dataframes into a single dataframe
df = pd.concat(df_list)

# save to csv
df.to_csv('ticker.csv')

ticker

with open("ticker.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    print(row)
df = pd.read_csv("ticker.csv")

print(df)