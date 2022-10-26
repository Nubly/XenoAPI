from flask_sqlalchemy import SQLAlchemy
from core import app

db = SQLAlchemy(app)


class Hydro(db.Model):
    __tablename__ = "data"
    location = db.Column(db.String(100), primary_key=True)
    water_temp = db.Column(db.Float)
    air_temp = db.Column(db.Float)
    tds = db.Column(db.Integer)
    ph = db.Column(db.Float)
    humidity = db.Column(db.Float)

    def __repr__(self):
        return f"Hydro<{self.location}>"

    @classmethod
    def create(self, loc, wt, at, tds, hum, ph=-20):
        hydro = self(
            location=loc, water_temp=wt, air_temp=at, tds=tds, ph=ph, humidity=hum
        )
        db.session.add(hydro)
        db.session.commit()
        return hydro
