from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CandleSticks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime)
    ticker = db.Column(db.String(64))
    o = db.Column(db.Float)
    h = db.Column(db.Float)
    l = db.Column(db.Float)
    c = db.Column(db.Float)
