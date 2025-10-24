from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class ProfessionalLevel(db.Model):
    __tablename__ = "professional_levels"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    hourly_total = db.Column(db.Numeric(10,2), nullable=False, default=0)

class Markup(db.Model):
    __tablename__ = "markups"
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(20), nullable=False)
    label = db.Column(db.String(80), nullable=False)
    pct = db.Column(db.Numeric(6,2), nullable=False, default=0)

class CourseDraft(db.Model):
    __tablename__ = "course_drafts"
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(20), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    hours = db.Column(db.Integer, nullable=False, default=40)
    students = db.Column(db.Integer, nullable=False, default=20)
    material_class = db.Column(db.Numeric(10,2), nullable=False, default=0)
    material_consumable = db.Column(db.Numeric(10,2), nullable=False, default=0)
    level_id = db.Column(db.Integer, db.ForeignKey("professional_levels.id"), nullable=True)
    segment = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    level = db.relationship("ProfessionalLevel", lazy="joined")
