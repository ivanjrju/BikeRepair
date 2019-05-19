from Server import db
from sqlalchemy import Column, Integer, String

class ChatMensagem(db.Model):

    __tablename__ = 'chat_mensagem'

    id = db.Column(db.Integer, primary_key=True)
    mensagem = db.Column(db.String, nullable=False)
    data = db.Column(db.String, nullable=False)
    receptor = db.Column(db.String, nullable=False)
    emissor = db.Column(db.String, nullable=False) 

    idChat = db.Column(db.Integer, db.ForeignKey('chat.id'))
    
    def __repr__(self):
        return "%r" % (self.__dict__)