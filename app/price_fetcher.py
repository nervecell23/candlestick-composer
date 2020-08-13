import pandas as pd
from datetime import datetime, timedelta
from app.models import CandleSticks

class FetchPricesError(Exception):
    def __init__(self, status, body):
        self.status = status
        self.body = body

    def __str__(self):
        return f"status: {self.status}, msg: {self.body}"

class PriceFetcher:
    def __init__(self, api):
       self.api = api

    def fetch_from_api(self, instrument):
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

    def fetch_from_db(self, instrument):
        temp_list = []
        candlesticks = CandleSticks.query.limit(24*30).all()
        for candlestick in candlesticks:
            time = candlestick.datetime
            open = candlestick.o
            high = candlestick.h
            low = candlestick.l
            close = candlestick.c
            temp_list.append({'Datetime': time, 'Open': open, 'High': high, 'Low': low, 'Close': close})
        df = pd.DataFrame(temp_list)
        df.set_index('DateTime', inplace=True)
        return df


        
if __name__ == '__main__':
    pass
