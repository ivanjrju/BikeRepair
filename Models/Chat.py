from Server import db
from sqlalchemy import Column, Integer

class Chat(db.Model):

    __tablename__ = 'chat'

    id = db.Column(db.Integer, primary_key=True)

    idCliente = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    idOficina = db.Column(db.Integer, db.ForeignKey('oficina.id'))
    
    chatMensagem = db.relationship('ChatMensagem', backref='chat')

    def __init__(self, dados):
        self.id=dados["id"]
        self.idCliente=dados["idCliente"]
        self.idOficina=dados["idOficina"]

    def __repr__(self):
        return "%r" % (self.__dict__)