from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/diy_api_python'

db = SQLAlchemy(app)

class Guitar(db.Model):
    __tablename__ = 'guitars'

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    make = db.Column(db.String, nullable=False)
    model = db.Column(db.String, nullable=False)
    finish = db.Column(db.String)

    def as_dict(self):
        return {
            'id': self.id,
            'year': self.year,
            'make': self.make,
            'model': self.model,
            'finish': self.finish
        }

    def __repr__(self):
        return f'<Guitar ({year} {make} {model}. {finish} finish.) >'
