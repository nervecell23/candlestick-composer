import pytest
from common.oanda_api_config import Config


@pytest.fixture
def oanda_api():
    cfg = Config()
    cfg.load()
    return cfg.create_context()
