import pickle
import pandas as pd
from app.candle_composer import CandleComposer

class Compare:
    def __init__(self):
        self.series_a = None
        self.series_b = None 
        self.candle_composer = CandleComposer()

    def load_from_file(self, loc_a, loc_b):
        with open(loc_a, 'rb') as f:
            df = pickle.load(f)
            self.series_a = self.candle_composer.compose(df, '8H') 
        with open(loc_b, 'rb') as f:
            df = pickle.load(f)
            self.series_b = self.candle_composer.compose(df, '8H')

    def compare(self):
        return self.series_a.corr(self.series_b)

