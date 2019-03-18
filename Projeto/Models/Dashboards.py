from Server import db
from sqlalchemy import Column, Integer, DateTime, String


class Dashboards(db.Model):

    idDashboard = db.Column(db.Integer, primary_key=True)
    idOficina = db.Column(db.Integer, db.ForeignKey('Oficinas.idOficina'))
    #usuariosOficina = db.relationship('UsuariosOficina', backref='usuariosOficina')