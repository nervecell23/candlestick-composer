import numpy as np
import pandas as pd


class CandleComposer:
    def compose_return_series(self, df, resample_timeframe=None):
        """
        Convert candlesticks of a timeperiod into a series of returns

        params: 
            df:  Pandas DataFrame of candlesticks
            resample_timeframe: String - see Pandas doc

        return: 
            Pandas Series
        """
        if resample_timeframe:
            df = df[df.index.dayofweek < 5]
            df = df.resample(resample_timeframe).agg({
                'Open': 'first',
                'High': np.max,
                'Low': np.min,
                'Close': 'last'
            })[df.columns]
            df.dropna(how='any', inplace=True)
            df = df.iloc[1: df.shape[0]-1]

        # turn candlesticks into series of return based on close prices
        series_close = df['Close']
        series_close_shifted = df['Close'].shift(periods=1)
        series_return = series_close / series_close_shifted
        return series_return.iloc[1:]
