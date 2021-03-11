from datetime import datetime
from src import db
from werkzeug.security import check_password_hash, generate_password_hash

class InterventionType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    interventions = db.relationship('PerformedIntervention', backref='InterventionType', lazy='dynamic')

class PerformedIntervention(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer, db.ForeignKey('intervention_type.id'))
    worker = db.Column(db.String(64), index=True)
    time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    direction = db.Column(db.String(64), index=True)
    pain_level = db.Column(db.Integer)
    intervention_location = db.Column(db.String(64))
    pain_location = db.Column(db.String(64))
    pu_concern = db.Column(db.Integer)
    late = db.Column(db.Integer, default=0)

    def to_dict(self):
        data = {
            'id': self.id,
            'type': self.InterventionType.name,
            'worker': self.worker,
            'time': self.time.isoformat() + 'Z',
            'direction': self.direction,
            'pain_level': self.pain_level,
            'intervention_location': self.intervention_location,
            'pain_location': self.pain_location,
            'pu_concern': self.pu_concern,
            'late': self.late
        }
        return data

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    friendly = db.Column(db.String(64), unique=True)
    salt = db.Column(db.String(128))
    password_hash = db.Column(db.String(128))
    user_type = db.Column(db.String(32))

    def checkPassword(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        data = {
            'id': self.id,
            'friendly': self.friendly
        }
        return data