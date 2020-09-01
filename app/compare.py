import pickle
import pandas as pd
from app.candle_composer import CandleComposer
from app.price_fetcher import PriceFetcher

class Compare:
    def __init__(self, api, ticker_a, ticker_b, granularity='D'):
        self.price_fetcher = PriceFetcher(api)
        self.candle_composer = CandleComposer()
        self.granularity = granularity 
        self.ticker_a = ticker_a
        self.ticker_b = ticker_b

    def compare(self):
        '''
        Calculate Pearson correlation of two pandas series
        '''
        candle_list_a = self.price_fetcher.fetch_from_api(self.ticker_a)
        candle_list_b = self.price_fetcher.fetch_from_api(self.ticker_b)
        df_a = self.price_fetcher.convert_to_dataframe(candle_list_a)
        df_b = self.price_fetcher.convert_to_dataframe(candle_list_b)
        return_series_a = self.candle_composer.compose_return_series(df_a)
        return_series_b = self.candle_composer.compose_return_series(df_b)
        return return_series_a.corr(return_series_b)
    
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
        
class MultipleCompare:
    def __init__(self):
        # self.ticker_list = ['USD_CHF', 'USD_JPY', 'USD_CAD', 'USD_CHN',
        #                     'USD_THB', 'USD_NOR', 'USD_ZAR', 'USD_CZK',
        #                     'USD_SGD', 'USD_PLN', 'USD_MXN', 'USD_TRY']
        self.ticker_list = ['USD_CHF', 'USD_JPY', 'USD_CHN']
        self.length = len(self.ticker_list)
    
    def calculate_corr(self):
        result = [[None] * self.length for _ in range(self.length)]
        for i in range(self.length):
            for j in range(i+1, self.length):
                ticker_a = self.ticker_list[i]
                ticker_b = self.ticker_list[j]
                compare_obj = Compare(ticker_a, ticker_b, granularity='D')
                result[i][j] = compare_obj.compare()
        return result


                


