from app.multi_compare import MultipleCompare
from common.oanda_api_config import Config
from flask import Flask

corr_app = Flask(__name__)

config = Config()
config.load()
api = config.create_context()
multi_comparer = MultipleCompare(api)


@corr_app.route('/')
def index():
    return 'Hello'


@corr_app.route('/corr')
def calculate_corr():
    return multi_comparer.calculate_corr()


if __name__ == '__main__':
    corr_app.run()
