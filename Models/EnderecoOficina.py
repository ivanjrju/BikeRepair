from Server import db
from sqlalchemy import Column, Integer, Float


class EnderecoOficina(db.Model):

    __tablename__ = 'endereco'

    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    cep = db.Column(db.Integer, nullable=False)
    numero = db.Column(db.Integer, nullable=False)

    idOficina = db.Column(db.Integer, db.ForeignKey('oficina.id'))

    def __init__(self, dados):
        self.latitude=dados["latitude"]
        self.longitude=dados["longitude"]
        self.cep=dados["cep"]
        self.numero=dados["numero"]

    def __repr__(self):
        return "%r" % (self.__dict__)