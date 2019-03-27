from Server import db
from sqlalchemy import Column, Integer, String, Float

class Oficina(db.Model):

    __tablename__ = 'oficina'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    foto = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    senha = db.Column(db.String, nullable=False)
    cpfCnpj = db.Column(db.String, nullable=False)
    avaliacaoTotal = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.String, nullable=False)
    qntOrcamentosAtendidos = db.Column(db.Integer, nullable=False)
    qntOrcamentosRejeitados = db.Column(db.Integer, nullable=False)
    qntReboquesAtendidos = db.Column(db.Integer, nullable=False)
    qntReboquesRejeitados = db.Column(db.Integer, nullable=False)