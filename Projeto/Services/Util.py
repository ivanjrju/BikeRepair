from Models import Avaliacao, Cartao, Chat, ChatMensagem, Cliente, EnderecoOficina, ItemOrdemServico, Oficina, OrdemServico, Produto
from Server import db

class Login(object):
    def efetuarLogin(dados):
        try:
            email = dados["email"]
            senha = dados["senha"]

            login = FuncoesCliente.buscarCliente(email)

            if(login["senha"] == senha):
                return resposta("OK", login)
            else:
                return resposta("NOK", None)

        except Exception as e:
            print(e)
            return resposta("NOK", None)

class FuncoesCliente(object):
    def cadastrar(dados):
        try:
            cliente = Cliente.Cliente(dados)
            print(cliente)
            db.session.add(cliente)
            db.session.commit()
            return resposta("OK", cliente)
        except Exception as e: 
            print(e)
            return resposta("NOK", None)

    def listar():
        try:
            clientes =  Cliente.Cliente.query.all()
            clientesFormatados = []
            for cliente in clientes:
                clientesFormatados.append(removerInstance(cliente))
                
            return resposta("OK", clientesFormatados)
        except Exception as e: 
            print(e)
            return resposta("NOK", None)

    def buscarCliente(email):
        try:
            cliente =  Cliente.Cliente.query.filter_by(email=email).first()
            return removerInstance(cliente)
        except Exception as e: 
            print(e)
            return None

    def cadastrarCartao(dados,email):
        try:
            cliente = removerInstance(Cliente.Cliente.query.filter_by(email=email["email"]).first())
            
            cartao = Cartao.Cartao(dados)
            cartao.idCliente = cliente["id"]

            db.session.add(cartao)
            db.session.commit()
            
            return resposta("OK", removerInstance(cartao))
            
        except Exception as e: 
            print(e)
            return resposta("NOK", None)


def resposta(status, dados):
    respostaPadrao = {}
    respostaPadrao['status'] = status
    respostaPadrao['dados'] = dados
    return respostaPadrao

def removerInstance(dados):
    dados = dados.__dict__
    del dados["_sa_instance_state"]
    return dados

def teste(dados):
    print(dados)