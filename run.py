from common.oanda_api_config import Config
from app.price_fetcher import PriceFetcher
from datetime import datetime
api = Config()
api.load()
ctx = api.create_context()

fetcher = PriceFetcher(ctx)
r = fetcher.fetch('EUR_USD')
print(datetime.fromtimestamp(float(r[0].time)))
print(datetime.fromtimestamp(float(r[-1].time)))
print(type(r[0].time))
