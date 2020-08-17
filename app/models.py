from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Instrument(db.Model):
    __tablename__ = 'instruments'
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(64), nullable=False, unique=True)

class CandleStick(db.Model):
    __tablename__ = 'candlesticks'
    id = db.Column(db.Integer, primary_key=True)
    o = db.Column(db.Float)
    h = db.Column(db.Float)
    l = db.Column(db.Float)
    c = db.Column(db.Float)
    ticker_id = db.Column(db.Integer, db.ForeignKey('instruments.id'), 
            nullable=False)
    instrument = db.relationship('Instrument', 
            backref=db.backref('candlesticks', lazy=True))
