from Server import db
from sqlalchemy import Column, Integer, DateTime, String, Float


class Servico(db.Model):

    idServico = db.Column(db.Integer, primary_key=True)
    idCliente = db.Column(db.Integer, db.ForeignKey('Cliente.idCliente'))
    idOficina = db.Column(db.Integer, db.ForeignKey('Oficina.idOficina'))
    servico = db.Column(db.String(50), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    detalhe = db.Column(db.String, nullable=False)
    precoCancelamento = db.Column(db.Float, nullable=False)