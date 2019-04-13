from Server import db
from sqlalchemy import Column, Integer, String


class ArquivoOficina(db.Model):

    __tablename__ = 'arquivo_oficina'

    id = db.Column(db.Integer, primary_key=True)
    arquivo = db.Column(db.String, nullable=False)

    idOficina = db.Column(db.Integer, db.ForeignKey('oficina.id'))

    def __init__(self, dados):
        self.arquivo=dados["arquivo"]

    def __repr__(self):
        return "%r" % (self.__dict__)