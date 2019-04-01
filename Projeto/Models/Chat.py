from Server import db
from sqlalchemy import Column, Integer

class Chat(db.Model):

    __tablename__ = 'chat'

    id = db.Column(db.Integer, primary_key=True)

    idCliente = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    idOficina = db.Column(db.Integer, db.ForeignKey('oficina.id'))
    
    chatMensagens = db.relationship('ChatMensagem', backref='chat')
