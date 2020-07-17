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
        return response.get('candles')
        
if __name__ == '__main__':
    pass
