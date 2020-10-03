import numpy as np
from app.multi_compare import MultipleCompare
from common.oanda_api_config import Config


class TestMultipleCompare:

    """
            USD_CHF     USD_JPY     USD_CAD
    USD_CHF    X           *           *
    USD_JPY    X           X           *
    USD_CAD    X           X           X
    """

    def test_calculate_corr(self, oanda_api):

        subject = MultipleCompare(oanda_api)
        result = subject.calculate_corr()
        assert np.array(result).shape == (3, 3)
