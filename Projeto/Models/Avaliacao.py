from Server import db
from sqlalchemy import Column, Integer, DateTime, String


class Avaliacao(db.Model):

    idAvaliacao = db.Column(db.Integer, primary_key=True)
    nota = db.Column(db.Integer, nullable=False)
    comentario = db.Column(db.String, nullable=False)
    idCliente = db.Column(db.Integer, db.ForeignKey('Cliente.idCliente'))
    idOficina = db.Column(db.Integer, db.ForeignKey('Oficina.idOficina'))