from Server import db
from sqlalchemy import Column, Integer, DateTime, String

class Dashboard(db.Model):

    __tablename__ = 'dashboard'

    id = db.Column(db.Integer, primary_key=True)
    idOficina = db.Column(db.Integer, db.ForeignKey('oficina.id'))
    orcamentosRealizados = db.Column(db.Integer, nullable=False)
    orcamentosCancelados = db.Column(db.Integer, nullable=False)