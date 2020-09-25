class MultipleCompare:
    def __init__(self):
        # self.ticker_list = ['USD_CHF', 'USD_JPY', 'USD_CAD', 'USD_CHN',
        #                     'USD_THB', 'USD_NOR', 'USD_ZAR', 'USD_CZK',
        #                     'USD_SGD', 'USD_PLN', 'USD_MXN', 'USD_TRY']
        self.ticker_list = ['USD_CHF', 'USD_JPY', 'USD_CHN']
        self.length = len(self.ticker_list)

    def calculate_corr(self):
        """
        Create a matrix of correlation

        return:
            2D array of correlation values
        """
        result = [[None] * self.length for _ in range(self.length)]
        for i in range(self.length):
            for j in range(i+1, self.length):
                instrument_a = self.ticker_list[i]
                instrument_b = self.ticker_list[j]
                compare_obj = Compare()
                result[i][j] = compare_obj.compare(instrument_a, instrument_b)
        return result
