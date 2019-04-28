from Server import db
from sqlalchemy import Column, Integer, String


class ArquivoCliente(db.Model):

    __tablename__ = 'arquivo_cliente'

    id = db.Column(db.Integer, primary_key=True)
    arquivo = db.Column(db.String, nullable=False)

    idCliente = db.Column(db.Integer, db.ForeignKey('cliente.id'))

    def __init__(self, dados):
        self.arquivo=dados["arquivo"]

    def __repr__(self):
        return "%r" % (self.__dict__)