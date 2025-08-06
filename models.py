from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Resume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    phone = db.Column(db.String(20))
    education = db.Column(db.Text)
    experience = db.Column(db.Text)
    projects = db.Column(db.Text)
    skills = db.Column(db.Text)
