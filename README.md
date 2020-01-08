# sqlite_stock_database
This is an example of how you can set up a sqlite stock database. Import and update stock data from yahoo finance.

Set up steps
1. Get latest python version 
Python 3.7.3 64-bit, spyder 4.0.0. from Anaconda


2. Install relevant python packages

pip install sqlite3
pip install os
pip install pandas
pip install pandas_datareader
pip install datetime 


3. Choose relevant stocks for you, which you want in your database

Example: Johnson&Johnson. To get the data in yahoo finance, you need the ticker for it. 
It is JNJ (https://de.finance.yahoo.com/quote/JNJ?p=JNJ&.tsrc=fin-srch)

4. Put the Tickers in the Excel sheet attached  or take the example Tickers.xlsx.

Columns: Stocks	| Ticker	| Ticker_tablenames	 | tablenames

Stocks: Stock Name
Ticker: Ticker in yahoo finance
Ticker_tablenames: Ticker without special character
tablenames: Ticker_tablenames but in small characters which is better for sqlite

5. Organise files

Python script and excel sheet should be in the same directory

6. Run script

Output in console should be: 

pdate Import from MMM is done from 2020-01-08
Update Import from ABT is done from 2020-01-08
Update Import from MO is done from 2020-01-08
Update Import from T is done from 2020-01-08
Update Import from KO is done from 2020-01-08
Update Import from CMPGF is done from 2020-01-08
Update Import from IBM is done from 2020-01-08
Update Import from JNJ is done from 2020-01-08
Update Import from JPM is done from 2020-01-08
Update Import from MCD is done from 2020-01-08
Update Import from NSRGF is done from 2020-01-08
Update Import from NVO is done from 2020-01-08
Update Import from PEP is done from 2020-01-08
Update Import from PG is done from 2020-01-08
Update Import from QCOM is done from 2020-01-08
Update Import from RDS-A is done from 2020-01-08
Update Import from UL is done from 2020-01-08
Update Import from BLK is done from 2020-01-08
Update Import from 1088.HK is done from 2019-11-26
Update Import from EPD is done from 2019-11-23
Update Import from FME.DE is done from 2019-11-29
Update Import from HD is done from 2019-11-23
Update Import from MSFT is done from 2019-11-23
Update Import from PFE is done from 2019-11-23
Update Import from DIS is done from 2019-11-23
Update Import from ABBV is done from 2019-11-23









