quantitatize anaylysis of the top 5 invested retail stocks over the last 5 years compared to the S&P 500.

Team members: Amrita Prithiani, Austin Means
## Description 
   take user input of 5 stocks and compare that over the last 5 years and forcast next 5 years.

## Outline.
1. analyze performance. Annalyizing the data to determine if any of the portfolios outperform the broader stock market which is represented by the s&p 500.

2. Analyze the volatility, analyze the volatility of each portfolio and the sandp 500 using visualiazations.

3. Analyze the risk

4. Analyze the risk return with sharpe ratio.

5. Portfolio prediction for given amount amount of time (5years).

6. Answer the question would you have been better off investing on your own in the top stocks of the last 5 years or would you have been bettter off in the 
s&p 500. and will this trend continue.

## Research questions to answer
    *****is there any single stocks in our data that outperformed the s&P 500 ******
    	What could you have done to raise the performance of the retail portfolio
	would investing in stock (x) have been a less risky investment based on sharpe ratio and overall return compared to the s&p.
	would investing in only stocks from a given sector return more or less than the s&p?
	



## Data sets to be used
    use alpha vantage API
    Find top 10 stock from https://www.thestreet.com/investing/top-10-stocks-by-searches-which-is-no-1#gid=ci02a32650c0002519&pid=no-10-bank-of-america

## Rough breakdown of tasks
   1. Breaking down analyzing the portfolio. Use the Pandas pct_change function together with dropna to create the daily returns DataFrame. Base this DataFrame on the NAV prices of the four portfolios and on the closing price of the S&P 500 Index. Review the first five rows of the daily returns DataFrame. 
   The following image shows how your daily returns DataFrame should appear:

   2. Analyze the data to determine if any of the portfolios outperform the broader stock market, which the S&P 500 represents. To do so, complete the following steps:
Use the holoviews plot function to visualize the daily return data  of the 5 stocks and the S&P 500.
calculate the cumulative returns for the the 5 stocks and the S&P 500. Review the last five rows of the cumulative returns DataFrame.
visualize the cumulative return values for the 5 stocks and the S&P 500 over time.

Question: Based on the cumulative return data and the visualization, do any  of the 5 stocks outperform the S&P 500 Index?

2.5 Analyze the volatility of each of the 5 stocks and of the S&P 500 Index by using box plots.
visualize the daily return data for each of the four portfolios and for the S&P 500 in a box plot. 
create a new DataFrame that contains the data for just the the 5 stocks by dropping the S&P 500 column. 
Visualize the daily return data for just the the 5 stocks.


3. calculate the standard deviation for each of the four portfolios and for the S&P 500.
Calculate the annualized standard deviation for each of the four portfolios and for the S&P 500. 
Use the daily returns DataFrame and a 21-day rolling window to plot the rolling standard deviations of the 5 stocks and of the S&P 500 index. 
Use the daily returns DataFrame and a 21-day rolling window to plot the rolling standard deviations of only the the 5 stocks. 

4. Use the daily return DataFrame to calculate the annualized average return data for the the 5 stocks and for the S&P 500. 
Calculate the Sharpe ratios for the the 5 stocks and for the S&P 500.
Visualize the Sharpe ratios for the 5 stocks and for the S&P 500 in a bar chart.

Answer the following question: Which of the five stocks offers the best risk-return profile? Which offers the worst?

5. Using the 60-day rolling window, the daily return data, and the S&P 500 returns, calculate the covariance. Review the last five rows of the covariance of the portfolio.
Calculate the beta of the portfolio. 
calculate the average value of the 60-day rolling beta of the portfolio.
Plot the 60-day rolling beta.

6. **Make a usable input from terminal to pick any 5 stocks from the sandp 500.**

