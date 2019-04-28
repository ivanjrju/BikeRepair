from Server import App, db
from flask import jsonify
from flask import request

from Services import Util

import sys

#~~~~ Login
@App.route('/loginCliente', methods=["POST"])
def loginCliente():
    dados = request.get_json()
    print("Dados: ",dados)
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


#~~~~ Arquivo Cliente
@App.route('/cadastrarArquivoCliente', methods=["POST"])
def cadastrarArquivoCliente():
    dados = request.get_json()
    arquivo = dados["arquivo"]
    cliente = dados["cliente"]
    resposta = Util.FuncoesArquivoCliente.cadastrar(arquivo,cliente)
    return jsonify(resposta)

@App.route('/buscarArquivosCliente', methods=["POST"])
def buscarArquivosCliente():
    dados = request.get_json()
    resposta = Util.FuncoesArquivoCliente.buscar(dados)
    return jsonify(resposta)


#~~~~ Arquivo Oficina
@App.route('/cadastrarArquivoOficina', methods=["POST"])
def cadastrarArquivoOficina():
    dados = request.get_json()
    arquivo = dados["arquivo"]
    oficina = dados["oficina"]
    resposta = Util.FuncoesArquivoOficina.cadastrar(arquivo,oficina)
    return jsonify(resposta)

@App.route('/buscarArquivosOficina', methods=["POST"])
def buscarArquivosOficina():
    dados = request.get_json()
    resposta = Util.FuncoesArquivoOficina.buscar(dados)
    return jsonify(resposta)


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


#~~~~ Endereco
@App.route('/cadastrarEndereco', methods=["POST"])
def cadastrarEndereco():
    dados = request.get_json()
    endereco = dados["endereco"]
    oficina = dados["oficina"]
    resposta = Util.FuncoesEndereco.cadastrar(endereco,oficina)
    return jsonify(resposta)

@App.route('/exibirEndereco', methods=["POST"])
def exibirEndereco():
    dados = request.get_json()
    resposta = Util.FuncoesEndereco.listar(dados)
    return jsonify(resposta)


#~~~~ Avaliação
@App.route('/cadastrarAvaliacao', methods=["POST"])
def cadastrarAvaliacao():
    dados = request.get_json()
    avaliacao = dados["avaliacao"]
    cliente = dados["cliente"]
    oficina = dados["oficina"]
    resposta = Util.FuncoesAvaliacao.cadastrar(avaliacao,cliente,oficina)
    return jsonify(resposta)

@App.route('/listarAvaliacaoPorOficina', methods=["POST"])
def listarAvaliacaoPorOficina():
    dados = request.get_json()
    resposta = Util.FuncoesAvaliacao.listarPorOficina(dados)
    return jsonify(resposta)


#~~~~ Produto
@App.route('/cadastrarProduto', methods=["POST"])
def cadastrarProduto():
    dados = request.get_json()
    produto = dados["produto"]
    oficina = dados["oficina"]
    resposta = Util.FuncoesProduto.cadastrar(produto,oficina)
    return jsonify(resposta)

@App.route('/listarProdutos', methods=["POST"])
def listarProdutos():
    dados = request.get_json()
    lista = Util.FuncoesProduto.listar(dados)
    return jsonify(lista)


#~~~~ Ordem Servico
@App.route('/cadastrarOrdemServico', methods=["POST"])
def cadastrarOrdemServico():
        dados = request.get_json()
        ordemServico = dados["ordemServico"]
        oficina = dados["oficina"]
        cliente = dados["cliente"]

        resposta = Util.FuncoesOrdemSerivo.cadastrar(ordemServico,oficina,cliente)
        return jsonify(resposta)

@App.route('/listarOrdemServicoCliente', methods=["POST"])
def listarOrdemServicoCliente():
    dados = request.get_json()
    resposta = Util.FuncoesOrdemSerivo.listarOrdemServicoCliente(dados)
    return jsonify(resposta)

@App.route('/listarOrdemServicoOficina', methods=["POST"])
def listarOrdemServicoOficina():
    dados = request.get_json()
    resposta = Util.FuncoesOrdemSerivo.listarOrdemServicoOficina(dados)
    return jsonify(resposta)


#~~~~ Item Ordem Servico
@App.route('/cadastrarItemOrdemServico', methods=["POST"])
def cadastrarItemOrdemServico():
    dados = request.get_json()
    ordemServico = dados["ordemServico"]
    produto = dados["produto"]
    item = dados["item"]
    resposta = Util.FuncoesItemOrdemSerivo.cadastrar(ordemServico, produto, item)
    return jsonify(resposta)

@App.route('/listarItemOrdemServico', methods=["POST"])
def listarItemOrdemServico():
    dados = request.get_json()
    resposta = Util.FuncoesItemOrdemSerivo.listarItemOrdemServicos(dados)
    return jsonify(resposta)


