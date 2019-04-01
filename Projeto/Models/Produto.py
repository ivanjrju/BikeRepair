from Server import db
from sqlalchemy import Column, Integer, String, Float


class Produto(db.Model):

    __tablename__ = 'produto'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    preco = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.String, nullable=False)
    categoria = db.Column(db.String, nullable=False)
    precoCancelamento = db.Column(db.Float, nullable=False)

    itemOrndemServicos = db.relationship('ItemOrdemServico', backref='produto')

    idOficina = db.Column(db.Integer, db.ForeignKey('oficina.id'))