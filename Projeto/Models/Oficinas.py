from Server import db
from sqlalchemy import Column, Integer, DateTime, String, Float


class Oficinas(db.Model):

    idOficina = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String, nullable=False)
    cpfCnpj = db.Column(db.String(50), nullable=False)
    avaliacaoTotal = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.String, nullable=False)
    promocao = db.Column(db.String, nullable=False)
    #enderecoOficinas = db.relationship('EnderecoOficinas', backref='enderecoOficinas')
    #avaliacoesCliente = db.relationship('AvaliacoesCliente', backref='avaliacoesCliente')
    #dashboard = db.relationship('Dashboards', backref='dashboard')
    #servicos = db.relationship('Servicos', backref='servicos')
    #usuariosOficina = db.relationship('UsuariosOficina', backref='usuariosOficina')
