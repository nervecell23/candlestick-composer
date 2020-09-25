import pandas as pd
from datetime import datetime, timedelta
from app.models import Instrument


class FetchPricesError(Exception):
    def __init__(self, status, body):
        self.status = status
        self.body = body

    def __str__(self):
        return f"status: {self.status}, msg: {self.body}"


class PriceFetcher:
    def __init__(self, api):
        self.api = api

    def fetch_from_api(self, instrument, granularity='D', count=60):
        """
        Fetch prices for specified instrument

        params:
            count: Number of candlesticks to fetch

        return:
            List[Dict[DateTime, Float, Float, Float, Float]]
        """
        kwargs = {}
        kwargs['granularity'] = granularity
        kwargs['count'] = count
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
            dt_candle.append({'DateTime': time, 'Open': o,
                              'High': h, 'Low': l, 'Close': c})
        return candle_list

    def convert_to_dataframe(self, price_list):
        """
        Convert fetched price list into Pandas dataframe

        params:
            price_list: List of candlesticks fetched from OANDA API

        return:
            Pandas df
        """
        df = pd.DataFrame(price_list)
        df.set_index('DateTime', inplace=True)
        return df

    def fetch_from_db(self, instrument):
        price_list = []
        candlesticks = Instrument.query.filter_by(
            ticker=instrument).candlesticks.limit(720).all()
        for candlestick in candlesticks:
            time = candlestick.datetime
            open = candlestick.o
            high = candlestick.h
            low = candlestick.l
            close = candlestick.c
            price_list.append({'Datetime': time, 'Open': open,
                               'High': high, 'Low': low, 'Close': close})
        return price_list


if __name__ == '__main__':
    pass
