from Server import db
from sqlalchemy import Column, Integer, DateTime, String

class Dashboard(db.Model):

    idDashboard = db.Column(db.Integer, primary_key=True)
    idOficina = db.Column(db.Integer, db.ForeignKey('Oficina.idOficina'))
    orcamentosRealizados = db.Column(db.Integer, nullable=False)
    orcamentosCancelados = db.Column(db.Integer, nullable=False)