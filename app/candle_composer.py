import numpy as np
import pandas as pd

class CandleComposer:
    def compose(self, df, interval):
        df.resample(interval).agg({'Open': 'first', 'High': np.max, 'Low': np.min, 'Close': 'last'})[df.columns]
        df.dropna(how='any', inplace=True)
        return df






