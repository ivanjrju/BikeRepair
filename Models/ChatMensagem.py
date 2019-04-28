from Server import db
from sqlalchemy import Column, Integer, String

class ChatMensagem(db.Model):

    __tablename__ = 'chat_mensagem'

    id = db.Column(db.Integer, primary_key=True)
    mensagem = db.Column(db.String, nullable=False)
    data = db.Column(db.Integer, nullable=False)
    receptor = db.Column(db.String, nullable=False)
    emissor = db.Column(db.String, nullable=False) 

    idCliente = db.Column(db.Integer, db.ForeignKey('chat.id'))
