from Server import App, db
from flask import jsonify
from flask import request

from Services import Util

import sys

#~~~~ Login
@App.route('/loginCliente', methods=["POST"])
def loginCliente():
    dados = request.get_json()
    resposta = Util.Login.cliente(dados)
    return jsonify(resposta)

@App.route('/loginOficina', methods=["POST"])
def loginOficina():
    dados = request.get_json()
    resposta = Util.Login.oficina(dados)
    return jsonify(resposta)

#~~~~ Cliente
@App.route('/cadastrarCliente', methods=["POST"])
def cadastrarCliente():

    dados = request.get_json()
    resposta = Util.FuncoesCliente.cadastrar(dados)
    return jsonify(resposta)

@App.route('/listarClientes', methods=["GET"])
def listarClientes():
    lista = Util.FuncoesCliente.listar()
    return jsonify(lista)

#~~~~ Cartao
@App.route('/cadastrarCartaoCliente', methods=["POST"])
def cadastrarCartaoCliente():
    dados = request.get_json()
    cartao = dados["cartao"]
    email = dados["cliente"]
    resposta = Util.FuncoesCliente.cadastrarCartao(cartao,email)
    return jsonify(resposta)

@App.route('/buscarCartaoCliente', methods=["POST"])
def buscarCartaoCliente():
    dados = request.get_json()
    cartoes = Util.FuncoesCliente.buscarCartaoCliente(dados)
    return jsonify(cartoes)

#~~~~ Oficina
@App.route('/cadastrarOficina', methods=["POST"])
def cadastrarOficina():

    dados = request.get_json()
    resposta = Util.FuncoesOficina.cadastrar(dados)
    return jsonify(resposta)

@App.route('/listarOficinas', methods=["GET"])
def listarOficinas():
    lista = Util.FuncoesOficina.listar()
    return jsonify(lista)

#~~~~ Produto
@App.route('/cadastrarProduto', methods=["POST"])
def cadastrarProduto():
    dados = request.get_json()
    produto = dados["produto"]
    oficina = dados["oficina"]
    resposta = Util.FuncoesProduto.cadastrar(produto,oficina)
    return jsonify(resposta)

@App.route('/listarProdutos', methods=["GET"])
def listarProdutos():
    lista = Util.FuncoesProduto.listar()
    return jsonify(lista)