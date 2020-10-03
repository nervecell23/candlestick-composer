class Compare:
    def __init__(self, price_fetcher, candle_composer):
        self.price_fetcher = price_fetcher
        self.candle_composer = candle_composer

    def compare(self, instrument_a, instrument_b):
        '''
        Calculate Pearson correlation of two return Series
        '''
        candle_list_a = self.price_fetcher.fetch_from_api(instrument_a)
        candle_list_b = self.price_fetcher.fetch_from_api(instrument_b)
        df_a = self.price_fetcher.convert_to_dataframe(candle_list_a)
        df_b = self.price_fetcher.convert_to_dataframe(candle_list_b)
        return_series_a = self.candle_composer.compose_return_series(df_a)
        return_series_b = self.candle_composer.compose_return_series(df_b)
        return return_series_a.corr(return_series_b)
