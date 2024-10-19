from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Rule(db.Model):
    __tablename__ = 'rules'
    id = db.Column(db.Integer, primary_key=True)
    rule_string = db.Column(db.String(500), nullable=False)
    ast = db.Column(db.Text, nullable=False)  # Store the AST as a serialized JSON
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

class RuleMetadata(db.Model):
    __tablename__ = 'rule_metadata'
    id = db.Column(db.Integer, primary_key=True)
    rule_id = db.Column(db.Integer, db.ForeignKey('rules.id'), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean, default=True)
    created_by = db.Column(db.String(100), nullable=False)
    rule = db.relationship('Rule', backref=db.backref('metadata', lazy=True))
