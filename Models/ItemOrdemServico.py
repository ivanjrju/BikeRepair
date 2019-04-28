from Server import db
from sqlalchemy import Column, Integer


class ItemOrdemServico(db.Model):

    __tablename__ = 'item_ordem_servico'

    id = db.Column(db.Integer, primary_key=True)
    qntProduto = db.Column(db.Integer, nullable=False)

    idOrdemServico = db.Column(db.Integer, db.ForeignKey('ordem_servico.id'))
    idProduto = db.Column(db.Integer, db.ForeignKey('produto.id'))

    def __init__(self, dados):
        self.qntProduto=dados["qntProduto"]

    def __repr__(self):
        return "%r" % (self.__dict__)