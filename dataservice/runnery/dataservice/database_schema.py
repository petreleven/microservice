from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String, Unicode, Numeric
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    uid: Mapped[int] = mapped_column(
        Integer, primary_key=True)
    email: Mapped[str] = mapped_column(Unicode(length=128))
    firstname: Mapped[str] = mapped_column(Unicode(length=128))
    password: Mapped[str] = mapped_column(Unicode(length=128))
    strava_token: Mapped[str] = mapped_column(String(length=128), nullable=True)
    age: Mapped[int] = mapped_column(Integer)
    weight: Mapped[float] = mapped_column(Numeric(4, 1))
    max_hr: Mapped[int] = mapped_column(Integer)
    rest_hr: Mapped[int] = mapped_column(Integer)
    vo2max: Mapped[float] = mapped_column(Numeric(4, 1))

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._authenticated = False

    def get_id(self):
        return self.uid
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    @property
    def is_authenticated(self):
        return self._authenticated
    
    def authenticate(self, password):
        checked = check_password_hash(self.password, password)
        self._authenticated = checked
        return self.authenticate

    def to_json(self, secure : bool = False):
        res = {}
        for attr in ('uid', 'email', 'firstname', 'age',
                     'weight', 'max_hr', 'rest_hr', 'vo2max'):
            value = getattr(self, attr)
            res[attr] = value
        
        if secure:
            res['strava_token'] = self.strava_token

        return res

class Run(db.Model):
    __tablename__ = 'run'
    runner: Mapped[str] = mapped_column(Unicode(length=128))
    strava_id: Mapped[str] = mapped_column(String(length=128), primary_key=True)
    name: Mapped[str] = mapped_column(Unicode(length=128))
    distance: Mapped[float] = mapped_column(Numeric(4, 1))
    elapsed_time :Mapped[float] = mapped_column(Numeric(4, 1))
    average_speed : Mapped[float] = mapped_column(Numeric(4, 1))
    average_heartrate :Mapped[float] = mapped_column(Numeric(4, 1))
    total_elevation_gain :Mapped[float] = mapped_column(Numeric(4, 1))
    start_date: Mapped [str] = mapped_column(Unicode(length=128))


    def to_json(self):
        res = {}
        for attr in ('runner', 'strava_id', 'name', 'distance', 'elapsed_time',
                     'average_speed', 'average_heartrate', 'total_elevation_gain', 'start_date'):
            value = getattr(self, attr)
            res[attr] = value
        
        return res


def init_database():
    exists = db.session.query(User).filter(User.email == 'peter@gg.org')
    if exists.first() != None:
        return

    peter = User()
    peter.email = 'peter@gg.org'
    peter.firstname = 'peter'
    peter.password = "xxxxxxxxx"
    peter.age = 40
    peter.weight = 58
    peter.max_hr = 192
    peter.rest_hr = 47
    peter.vo2max = 63
    db.session.add(peter)
    db.session.commit()