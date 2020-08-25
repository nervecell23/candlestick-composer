import pytest
from app.price_fetcher import PriceFetcher
from unittest.mock import Mock
from datetime import datetime

class TestPriceFetcher:

    def test_fetch_from_api(self):
        mock_candle = Mock()
        mock_candle.mid.o = 1.0
        mock_candle.mid.h = 1.0
        mock_candle.mid.l = 1.0
        mock_candle.mid.c = 1.0
        mock_candle.time = datetime.now().timestamp()

        mock_candle_list = [mock_candle, mock_candle, mock_candle]

        mock_response = Mock()
        mock_response.status = 200
        mock_response.get = Mock(return_value=mock_candle_list)

        mock_api = Mock()
        mock_api.instrument.candles = Mock(return_value=mock_response)
        subject = PriceFetcher(api=mock_api)
        _ = subject.fetch_from_api('EUR_USD')
        mock_api.instrument.candles.assert_called_with('EUR_USD', granularity='H1')