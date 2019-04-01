from Server import db
from sqlalchemy import Column, Integer, Boolean


class OrdemServico(db.Model):

    __tablename__ = 'ordem_servico'

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    precoTotal = db.Column(db.Integer, nullable=False)

    itemOrndemServicos = db.relationship('ItemOrdemServico', backref='ordemServico')

    idCliente = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    idOficina = db.Column(db.Integer, db.ForeignKey('oficina.id'))