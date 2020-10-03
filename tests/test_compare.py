import pytest
from app.price_fetcher import PriceFetcher
from app.candle_composer import CandleComposer
from app.compare import Compare


class TestCompare():

    @pytest.fixture
    def price_fetcher(self, oanda_api):
        return PriceFetcher(oanda_api)

    @pytest.fixture
    def candle_composer(self):
        return CandleComposer()

    def test_compare(self, price_fetcher, candle_composer):
        subject = Compare(price_fetcher, candle_composer)
        result = subject.compare('USD_JPY', 'USD_CAD')
        assert isinstance(result, float) == True
