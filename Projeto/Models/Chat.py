from Server import db
from sqlalchemy import Column, Integer, DateTime, String, Float

class Chat(db.Model):

    __tablename__ = 'chat'

    id = db.Column(db.Integer, primary_key=True)
    grupo = db.Column(db.String(50), nullable=False)
    transmissor = db.Column(db.String, nullable=False)
    receptor = db.Column(db.String(50), nullable=False)
    mensagem = db.Column(db.String(50), nullable=False)
    horario = db.Column(db.String, nullable=False)
    
