from Server import db
from sqlalchemy import Column, Integer, String


class Cartao(db.Model):

    __tablename__ = 'cartao'

    id = db.Column(db.Integer, primary_key=True)
    pan = db.Column(db.Integer, nullable=False)
    dataValidade = db.Column(db.String, nullable=False)
    codigoSeguranca = db.Column(db.Integer, nullable=False)
    nomeCartao = db.Column(db.String, nullable=False)