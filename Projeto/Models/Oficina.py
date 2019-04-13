from Server import db
from sqlalchemy import Column, Integer, String, Float

from time import gmtime, strftime

class Oficina(db.Model):

    __tablename__ = 'oficina'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    senha = db.Column(db.String, nullable=False)
    cpfCnpj = db.Column(db.String, nullable=False)
    avaliacaoTotal = db.Column(db.Float)
    descricao = db.Column(db.String)
    dataCadastro = db.Column(db.String)
    qntOrcamentosAtendidos = db.Column(db.Integer)
    qntOrcamentosRejeitados = db.Column(db.Integer)
    qntReboquesAtendidos = db.Column(db.Integer)
    qntReboquesRejeitados = db.Column(db.Integer)
    horarioFuncionamento = db.Column(db.String, nullable=False)

    avaliacoes = db.relationship('Avaliacao', backref='oficina')
    ordemServicos = db.relationship('OrdemServico', backref='oficina')
    produtos = db.relationship('Produto', backref='oficina')
    endereco = db.relationship('EnderecoOficina', backref='oficina')
    chats = db.relationship('Chat', backref='oficina')
    documentos = db.relationship('ArquivoOficina', backref='oficina')

    def __init__(self, dados):
        self.nome=dados["nome"]
        self.email=dados["email"]
        self.senha=dados["senha"]
        self.cpfCnpj=dados["cpfCnpj"]
        self.avaliacaoTotal=0
        self.descricao=""
        self.dataCadastro= strftime("%d/%m/%Y", gmtime())
        self.qntOrcamentosAtendidos=0
        self.qntOrcamentosRejeitados=0
        self.qntReboquesAtendidos=0
        self.qntReboquesRejeitados=0
        self.horarioFuncionamento=dados["horarioFuncionamento"]

    def __repr__(self):
        return "%r" % (self.__dict__)