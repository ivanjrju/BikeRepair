from Server import db
from sqlalchemy import Column, Integer, DateTime, String


class AvaliacoesCliente(db.Model):

    idAvaliacoesCliente = db.Column(db.Integer, primary_key=True)
    nota = db.Column(db.Integer, nullable=False)
    comentario = db.Column(db.String, nullable=False)
    idCliente =
    idOficina =