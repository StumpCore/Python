import time

import pandas as pd
from ib_insync import *
from contextlib import contextmanager
import yfinance as yf
import polars as pl

class IBConnection():
    def __init__(self):
        self.ib = IB()


    @contextmanager
    def __connect(self):
        """
        Creates a connection to the InteractiveBroker API, as long as the TraderWorkstation
        is active and the user is logged in.
        :return:
        """
        connection = self.ib.connect()
        try:
            yield connection
        except :
            raise Exception('No Connection to TraderWorkstation.')
        finally:
            connection.disconnect()

    def trading(self):
        with self.__connect() as con:
            try:
                msft_df = pd.read_csv('msft.csv')
            except:
                start = '2014-01-01'
                end = '2023-12-31'
                symbol = 'MSFT'
                msft_df = yf.download(symbol, start, end)
                msft_df.to_csv('msft.csv')
            print(msft_df.head())












if __name__ == '__main__':
    con = IBConnection()
    con.trading()