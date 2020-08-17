from app import corr_app , db
from app.models import CandleStick, Instrument

@corr_app.route('/')
def index():
    return 'Hello'

@corr_app.route('/add_entry')
def add_entry():
    for i, c in db.session.query(Instrument, CandleStick).join(CandleStick, Instrument.id == CandleStick.ticker_id).all():
        print(f"---{i} ---{c}")
    return 'Done'
if __name__ == '__main__':
    corr_app.run()
