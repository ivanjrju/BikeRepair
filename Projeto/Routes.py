from Server import App, db
from flask import jsonify
from flask import request

from Models import Avaliacao, Chat, Cliente, Dashboard, EnderecoOficina, Oficina, Servico

@App.route("/")
def teste():
    oficina = Oficina.Oficina(nome="Oficina do Joao",email="Joao@gmail.com",senha="joao123",cpfCnpj="12345612325",avaliacaoTotal="80",descricao="texto1",promocao="texto2")
    endereco = EnderecoOficina.EnderecoOficina(idOficina=oficina.id,latitude=10.10,longitude=10.10,cep=123456,numero=20,raio=20)

    db.session.add(oficina)
    db.session.add(endereco)
    db.session.commit()

    
    