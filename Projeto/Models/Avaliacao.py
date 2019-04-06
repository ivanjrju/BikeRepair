from Server import db
from sqlalchemy import Column, Integer, String


class Avaliacao(db.Model):

    __tablename__ = 'avaliacao'

    id = db.Column(db.Integer, primary_key=True)
    nota = db.Column(db.Integer, nullable=False)
    comentario = db.Column(db.String, nullable=False)
    idCliente = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    idOficina = db.Column(db.Integer, db.ForeignKey('oficina.id'))

    def __init__(self, dados):
        self.nota=dados["nota"]
        self.comentario=dados["comentario"]

    def __repr__(self):
        return "%r" % (self.__dict__)