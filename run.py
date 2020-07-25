import pickle
from common.oanda_api_config import Config
from app.price_fetcher import PriceFetcher
from app.compare import Compare
from datetime import datetime
from pathlib import Path

'''
file_loc = Path(__file__).absolute()
api = Config()
api.load()
ctx = api.create_context()
fetcher = PriceFetcher(ctx)

pkl_loc_b = file_loc.parent / 'df2.pkl'
pkl_loc_a = file_loc.parent / 'df.pkl'
r = fetcher.fetch('GBP_USD')
with open(str(pkl_loc_a), 'wb') as f:
    pickle.dump(r, f)
r = fetcher.fetch('EUR_USD')
with open(str(pkl_loc_b), 'wb') as f:
    pickle.dump(r, f)
'''
compare_obj = Compare()
compare_obj.load_from_file('df.pkl', 'df2.pkl')
print('======================')
print(compare_obj.compare())
'''
print(datetime.fromtimestamp(float(r[0].time)))
print(datetime.fromtimestamp(float(r[-1].time)))
print(type(r[0].time))
'''
