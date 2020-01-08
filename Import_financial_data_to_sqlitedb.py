"""
Created on Wed Nov  6 13:03:42 2019

@author: antonio.blago
"""
#%% Connect to database

import sqlite3
conn = sqlite3.connect('Portfolio_dividens.db')
c = conn.cursor()

from sqlalchemy import create_engine #suport pd.dataframe to sql table
#import mysqlclient

engine = create_engine("sqlite:///Portfolio_dividens.db")

#%% Set up path

import os
# detect the current working directory and print it
path = os.getcwd()

#%%
''' Yahoo finance'''
import pandas as pd
from pandas_datareader import data as wb
import datetime as dt

date_today=dt.date.today()

start_1='2005-1-1'

tickers_df=pd.read_excel(path+r'\Tickers.xlsx')

tickers=list(tickers_df['Ticker'])

tablenames=list(tickers_df['tablenames'])


from sqlalchemy import inspect


inspector = inspect(engine)

# Get table information
inspect_tables=inspector.get_table_names()


Select_last_value= "Select Date from '{}' order by date desc limit 1;"

Check_table_exists="SHOW TABLES LIKE {}"

#pd.read_sql_query(Select_last_value,con=engine)

if len(inspect_tables)==0: #first initialize db
    
    for k, t in enumerate(tickers):
    
        ticker_data=pd.DataFrame()
        try:
            ticker_data=wb.DataReader(t, data_source='yahoo',start=start_1)
            ticker_data.to_sql(tablenames[k],con=engine,if_exists="replace" )
        
        except:
            print("New Import from {} went wrong".format(t))
        else:
            print("New Import from {} is done".format(t))
            
else:
    
    for k, t in enumerate(tickers):
                
        if tablenames[k] not in inspect_tables: #check table is existing
            ticker_data=pd.DataFrame()
            try:
                ticker_data=wb.DataReader(t, data_source='yahoo',start=start_1)
                ticker_data.to_sql(tablenames[k],con=engine,if_exists="replace" )
            
            except:
                print("New Import from {} went wrong".format(t))
            else:
                print("New Import from {} is done".format(t))
                
        
        else:   
            
        
            ticker_data=pd.DataFrame()
            
            check_last_value=pd.read_sql_query(Select_last_value.format(tablenames[k]),con=engine)
            check_last_value2=(pd.to_datetime(check_last_value['Date'][0],format="%Y-%m-%d")).date()
            
            if check_last_value2!=date_today: #dt.datetime.strptime("2019-11-13", "%Y-%m-%d")==pd.to_datetime(check_last_value['Date'][0])
                
                try:
                    ticker_data=wb.DataReader(t, data_source='yahoo',start=check_last_value2+dt.timedelta(days=1))
                    ticker_data.to_sql(tablenames[k],con=engine,if_exists="append")
                
                except:
                    print("Update Import from {} went wrong".format(t))
                else:
                    print("Update Import from {} is done from {}".format(t,str(check_last_value2+dt.timedelta(days=1))))
                    
        
        
