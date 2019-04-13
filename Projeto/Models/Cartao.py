from Server import db
from sqlalchemy import Column, Integer, String


class Cartao(db.Model):

    __tablename__ = 'cartao'

    id = db.Column(db.Integer, primary_key=True)
    pan = db.Column(db.BigInteger, nullable=False)
    dataValidade = db.Column(db.String, nullable=False)
    codigoSeguranca = db.Column(db.Integer, nullable=False)
    nomeCartao = db.Column(db.String, nullable=False)

    idCliente = db.Column(db.Integer, db.ForeignKey('cliente.id'))

    def __init__(self, dados):
        self.pan=dados["pan"]
        self.dataValidade=dados["dataValidade"]
        self.codigoSeguranca=dados["codigoSeguranca"]
        self.nomeCartao=dados["nomeCartao"]

    def __repr__(self):
        return "%r" % (self.__dict__)