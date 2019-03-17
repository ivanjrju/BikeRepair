from Server import db
from sqlalchemy import Column, Integer, DateTime, String


class Dashboards(db.Model):

    idCliente = db.Column(db.Integer, primary_key=True)
    idOficina =