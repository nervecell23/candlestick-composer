import pytest
from app.price_fetcher import PriceFetcher
from unittest.mock import Mock, patch, call
from datetime import datetime
from app.models import db, CandleStick, Instrument

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

    @patch('app.price_fetcher.Instrument')
    def test_fetch_from_db(self, mock_Instrument):
        dt = datetime(2020, 1, 20, 13, 45)
        mock_candlestick = Mock()
        mock_candlestick.datetime = dt
        mock_candlestick.o = 1.11
        mock_candlestick.h = 2.22
        mock_candlestick.l = 3.33
        mock_candlestick.c = 4.44

        mock_candlestick_list = [mock_candlestick]

        mock_query_candlesticks = Mock()
        mock_query_candlesticks.all = Mock(return_value=mock_candlestick_list)

        mock_query_return = Mock()
        mock_query_return.candlesticks.limit = Mock(return_value=mock_query_candlesticks)
        
        mock_Instrument.query.filter_by = Mock(return_value=mock_query_return)

        expected_result = [{
            'Datetime': dt, 
            'Open': 1.11, 
            'High': 2.22, 
            'Low': 3.33, 
            'Close': 4.44
        }]

        mock_api = Mock()
        subject = PriceFetcher(api=mock_api)
        result = subject.fetch_from_db('EUR_USD')
        assert result == expected_result

        
        

