from Server import db
from sqlalchemy import Column, Integer


class ItemOrdemServico(db.Model):

    __tablename__ = 'item_ordem_servico'

    id = db.Column(db.Integer, primary_key=True)
    idOrdemServico = db.Column(db.Integer, db.ForeignKey('ordem_servico.id'))
    idProduto = db.Column(db.Integer, db.ForeignKey('produto.id'))
    qntProduto = db.Column(db.Integer, nullable=False)