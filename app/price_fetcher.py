import pandas as pd
from datetime import datetime, timedelta

class FetchPricesError(Exception):
    def __init__(self, status, body):
        self.status = status
        self.body = body

    def __str__(self):
        return f"status: {self.status}, msg: {self.body}"

class PriceFetcher:
    def __init__(self, api):
       self.api = api

    def fetch(self, instrument):
        kwargs = {}
        kwargs['granularity'] = 'H1'
        response = self.api.instrument.candles(instrument, **kwargs)
        if response.status != 200:
            raise FetchPricesError(response.status, response.body)
        candle_list = response.get('candles')
        dt_candle = []
        for candle in candle_list:
            time = datetime.fromtimestamp(float(candle.time))
            o = candle.mid.o
            h = candle.mid.h
            l = candle.mid.l
            c = candle.mid.c
            dt_candle.append({'DateTime': time, 'Open': o, 'High': h, 'Low': l, 'Close': c})
        df = pd.DataFrame(dt_candle)
        df.set_index('DateTime', inplace=True)
        return df

        
if __name__ == '__main__':
    pass
