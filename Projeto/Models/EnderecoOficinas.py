from Server import db
from sqlalchemy import Column, Integer, DateTime, String, Float


class EnderecoOficinas(db.Model):

    idEnderecoOficina = db.Column(db.Integer, primary_key=True)
    idOficina = db.Column(db.Integer, db.ForeignKey('Oficinas.idOficina'))
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    cep = db.Column(db.Integer, nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    raio = db.Column(db.Integer, nullable=False)