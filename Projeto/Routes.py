from Server import App, db
from flask import jsonify
from flask import request

from Services import Util

import sys


@App.route('/login', methods=["POST"])
def efetuarLogin():
    dados = request.get_json()
    resposta = Util.Login.efetuarLogin(dados)
    return jsonify(resposta)

@App.route('/cadastrarCliente', methods=["POST"])
def cadastrarCliente():

    dados = request.get_json()
    resposta = Util.FuncoesCliente.cadastrar(dados)
    return jsonify(resposta)

@App.route('/listarClientes', methods=["GET"])
def listarClientes():
    lista = Util.FuncoesCliente.listar()
    return jsonify(lista)

@App.route('/cadastrarCartaoCliente', methods=["POST"])
def cadastrarCartaoCliente():
    dados = request.get_json()
    cartao = dados["cartao"]
    email = dados["cliente"]
    resposta = Util.FuncoesCliente.cadastrarCartao(cartao,email)
    return jsonify(resposta)