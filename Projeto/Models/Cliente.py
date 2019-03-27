from Server import db
from sqlalchemy import Column, Integer, String, Boolean


class Cliente(db.Model):

    __tablename__ = 'cliente'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.Integer, nullable=False)
    aniversario = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String(50), nullable=False)
    fotoPerfil = db.Column(db.String, nullable=False)
    autenticado = db.Column(db.Boolean, nullable=False)
    dataCadastro = db.Column(db.Integer, nullable=False)
    raio = db.Column(db.Integer, nullable=False)