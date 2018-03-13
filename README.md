AutoTrading
===========

In this HW, we will implement a very aged prediction problem from the financial field. Given a series of stock prices, including daily open, high, low, and close prices, decide your daily action and make your best profit for the future trading. Can you beat the simple “buy-and-hold” strategy? Please check the sample data. You will see each line contains four tuples: open-high-low-close. The sample data is NASDAQ:GOOG. The data, called training_data.csv, contains more-than-five-year daily prices, whose line number corresponds to the time sequence. Another data, called testing_data.csv, contains one-year daily prices, which corresponds to the time period next to the final date in training_data.csv. In this project, we ignore the transaction cost, meaning that you can do an action every day if you want without extra expense (at most one action can be executed within one day, as the open price)

Method
======

buy:if one day's high price + low price > 2 * close price ， then buy in next day and record the price in register "buy"

sell:if this day's open price is higher than "buy" , then sell it

otherwise doing nothing
