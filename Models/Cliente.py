from Server import db
from sqlalchemy import Column, Integer, String, Boolean

from time import gmtime, strftime

class Cliente(db.Model):

    __tablename__ = 'cliente'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.Integer, nullable=False)
    aniversario = db.Column(db.String, nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    senha = db.Column(db.String(50), nullable=False)
    autenticado = db.Column(db.Boolean)
    dataCadastro = db.Column(db.String)
    raio = db.Column(db.Integer)

    cartoes = db.relationship('Cartao', backref='cliente')
    avaliacoes = db.relationship('Avaliacao', backref='cliente')
    ordemServicos = db.relationship('OrdemServico', backref='cliente')
    chats = db.relationship('Chat', backref='cliente')
    documentos = db.relationship('ArquivoCliente', backref='cliente')

    def __init__(self, dados):
        self.nome=dados["nome"]
        self.telefone=dados["telefone"]
        self.aniversario=dados["aniversario"]
        self.email=dados["email"]
        self.senha=dados["senha"]
        self.autenticado=False
        self.dataCadastro= strftime("%d/%m/%Y")
        self.raio=10

    def __repr__(self):
        return "%r" % (self.__dict__)