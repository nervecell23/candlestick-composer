import pickle
import pandas as pd
from app.candle_composer import CandleComposer
from app.price_fetcher import PriceFetcher
from app import oanda_api

class Compare:
    def __init__(self):
        self.candle_composer = CandleComposer()

    def compare_from_file(self, loc_a, loc_b):
        '''
        Load pandas dataframe of candlesticks from pickle file
        '''
        with open(loc_a, 'rb') as f:
            df = pickle.load(f)
            return_series_a = self.candle_composer.compose_return_series(df, '8H') 
        with open(loc_b, 'rb') as f:
            df = pickle.load(f)
            return_series_b = self.candle_composer.compose_return_series(df, '8H')
        return return_series_a.corr(return_series_b)
        
    def compare(self, df_return_a, df_return_b):
        '''
        Calculate Pearson correlation of two pandas series
        '''
        return df_return_a.corr(df_return_b)

class MultipleCompare:
    def __init__(self):
        self.price_fetcher = PriceFetcher(oanda_api)
        self.comparer = Compare()
        self.candle_composer = CandleComposer()
        self.ticker_list = ['USD_CHF', 'USD_JPY', 'USD_CAD', 'USD_CHN',
                            'USD_THB', 'USD_NOR', 'USD_ZAR', 'USD_CZK',
                            'USD_SGD', 'USD_PLN', 'USD_MXN', 'USD_TRY']
    
    def calculate_corr(self):
        list_length = len(self.ticker_list)
        for i in range(list_length):
            for j in range(i+1, list_length):
                ticker_a = self.ticker_list[i]
                ticker_b = self.ticker_list[j]
                df_a = self.price_fetcher.fetch_from_db(ticker_a)
                df_b = self.price_fetcher.fetch_from_db(ticker_b)
                df_return_a = self.candle_composer.compose_return_series(df_a, '8H')
                df_return_b = self.candle_composer.compose_return_series(df_b, '8H') 
                return self.comparer.compare(df_return_a, df_return_b)


                


