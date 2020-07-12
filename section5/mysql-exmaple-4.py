import pandas_datareader.data as web
import pandas as pd
import datetime
import pymysql

#Create MySql DB
pymysql.install_as_MySQLdb()
from sqlalchemy import create_engine


#Install pymysql, sqlalchemy
try:
    engine = create_engine("mysql+mysqldb://root:"+"sesame"+"@localhost/python_01", encoding='utf-8')
    with engine.connect() as conn:
      symbol = 'WIKI/AAPL'  # or 'AAPL.US'
      df = web.DataReader(symbol, 'quandl', '2015-01-01', '2015-01-05')
      print(df.loc['2015-01-02'])

finally:
    print("Dataframe SQL Work Complete!")

###########We need to have access key for APIs!

