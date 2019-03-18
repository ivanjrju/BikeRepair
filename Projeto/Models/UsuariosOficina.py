from Server import db
from sqlalchemy import Column, Integer, DateTime, String, Float


class UsuariosOficina(db.Model):

    idUsuariosOficina = db.Column(db.Integer, primary_key=True)
    idDashboard = db.Column(db.Integer, db.ForeignKey('Dashboards.idDashboard'))
    idOficina = db.Column(db.Integer, db.ForeignKey('Oficinas.idOficina'))
    idCliente = db.Column(db.Integer, db.ForeignKey('Clientes.idCliente'))
    