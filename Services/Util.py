from Models import Avaliacao, Cartao, Chat, ChatMensagem, Cliente, EnderecoOficina
from Models import ItemOrdemServico, Oficina, OrdemServico, Produto, ArquivoCliente, ArquivoOficina
from Server import db


import datetime

import requests as Req
import json

from time import strftime

#~~~~ Login
class Login(object):
    def cliente(dados):
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
    
    def oficina(dados):
        try:
            email = dados["email"]
            senha = dados["senha"]
            login = FuncoesOficina.buscarOficina(email)
            if(login["senha"] == senha):
                return resposta("OK", login)
            else:
                return resposta("NOK", None)
        except Exception as e:
            print(e)
            return resposta("NOK", None)


#~~~~ Cliente
class FuncoesCliente(object):
    def cadastrar(dados):
        try:
            cliente = Cliente.Cliente(dados)
            db.session.add(cliente)
            db.session.commit()
            return resposta("OK", "")
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

    def alterarCliente(dados):   
        try:
            cliente =  Cliente.Cliente.query.filter_by(id=dados["id"]).first()
            cliente.telefone = dados["telefone"]
            cliente.senha = dados["senha"]
            cliente.autenticado = dados["autenticado"]
            cliente.raio = dados["raio"]
            cliente.keyfirebase = dados["keyfirebase"]
            db.session.commit()
            return resposta("OK", "")
        except Exception as e: 
            print(e)
            return resposta("NOK", None)

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

    def buscarCartaoCliente(dados):
        try:
            cliente = removerInstance(Cliente.Cliente.query.filter_by(email=dados["email"]).first())
            cartoes  =  Cartao.Cartao.query.filter_by(idCliente=cliente["id"]).all()
            listaDeCartoes = []
            for cartao in cartoes:
                listaDeCartoes.append(removerInstance(cartao))

            return resposta("OK", listaDeCartoes)
        except Exception as e: 
            print(e)
            return resposta("NOK", None)


#~~~~ Arquivo Cliente
class FuncoesArquivoCliente(object):
    def cadastrar(arquivo,cliente):
        try:
            cliente = removerInstance(Cliente.Cliente.query.filter_by(email=cliente["email"]).first())
            arquivoCliente = ArquivoCliente.ArquivoCliente(arquivo)
            arquivoCliente.idCliente = cliente["id"]
            db.session.add(arquivoCliente)
            db.session.commit()
            return resposta("OK", "")
        except Exception as e:
            print(e)
            return resposta("NOK", None)

    def buscar(dados):
        try:
            cliente = removerInstance(Cliente.Cliente.query.filter_by(email=dados["email"]).first())
            arquivosCliente = ArquivoCliente.ArquivoCliente.query.filter_by(idCliente=cliente["id"]).all()
            arquivosClienteFormatados = []
            for arquivoCliente in arquivosCliente:
                arquivosClienteFormatados.append(removerInstance(arquivoCliente)) 
            return resposta("OK", arquivosClienteFormatados)
        except Exception as e: 
            print(e)
            return resposta("NOK", None)


#~~~~ Oficina
class FuncoesOficina(object):
    def cadastrar(dados):
        try:
            oficina = Oficina.Oficina(dados)
            db.session.add(oficina)
            db.session.commit()
            return resposta("OK", "")
        except Exception as e: 
            print(e)
            return resposta("NOK", None)

    def listar():
        try:
            oficinas =  Oficina.Oficina.query.all()
            oficinasFormatados = []
            for oficina in oficinas:
                oficinasFormatados.append(removerInstance(oficina)) 
            return resposta("OK", oficinasFormatados)
        except Exception as e: 
            print(e)
            return resposta("NOK", None)

    def buscarOficina(email):
        try:
            oficina =  Oficina.Oficina.query.filter_by(email=email).first()
            return removerInstance(oficina)
        except Exception as e: 
            print(e)
            return None

    def buscarOficinaId(dados):
        try:
            oficina =  Oficina.Oficina.query.filter_by(id=dados["id"]).first()
            return removerInstance(oficina)
        except Exception as e: 
            print(e)
            return None

    def alterarOficina(dados):   
        try:
            oficina =  Oficina.Oficina.query.filter_by(id=dados["id"]).first()
            oficina.senha = dados["senha"]
            oficina.descricao = dados["descricao"]
            oficina.avaliacaoTotal = dados["avaliacaoTotal"]
            oficina.qntOrcamentosAtendidos = dados["qntOrcamentosAtendidos"]
            oficina.qntOrcamentosRejeitados = dados["qntOrcamentosRejeitados"]
            oficina.qntReboquesAtendidos = dados["qntReboquesAtendidos"]
            oficina.qntReboquesRejeitados = dados["qntReboquesRejeitados"]
            oficina.horarioFuncionamento = dados["horarioFuncionamento"]
            db.session.commit()
            return resposta("OK", "")
        except Exception as e: 
            print(e)
            return resposta("NOK", None)


#~~~~ Arquivo Oficina
class FuncoesArquivoOficina(object):
    def cadastrar(arquivo,oficina):
        try:
            oficina = removerInstance(Oficina.Oficina.query.filter_by(email=oficina["email"]).first())
            arquivoOficina = ArquivoOficina.ArquivoOficina(arquivo)
            arquivoOficina.idOficina = oficina["id"]
            db.session.add(arquivoOficina)
            db.session.commit()
            return resposta("OK", "")
        except Exception as e:
            print(e)
            return resposta("NOK", None)

    def buscar(dados):
        try:
            oficina = removerInstance(Oficina.Oficina.query.filter_by(email=dados["email"]).first())
            arquivosOficina = ArquivoOficina.ArquivoOficina.query.filter_by(idOficina=oficina["id"]).all()
            arquivosOficinaFormatados = []
            for arquivoOficina in arquivosOficina:
                arquivosOficinaFormatados.append(removerInstance(arquivoOficina)) 
            return resposta("OK", arquivosOficinaFormatados)
        except Exception as e: 
            print(e)
            return resposta("NOK", None)


#~~~~ Endereco
class FuncoesEndereco(object):
    def cadastrar(dados,oficina):
        try:
            oficina = removerInstance(Oficina.Oficina.query.filter_by(email=oficina["email"]).first())
            endereco = EnderecoOficina.EnderecoOficina(dados)
            endereco.idOficina = oficina["id"]
            db.session.add(endereco)
            db.session.commit()
            return resposta("OK", "")
        except Exception as e: 
            print(e)
            return resposta("NOK", None)
    
    def listar(oficina):
        try:
            oficina = removerInstance(Oficina.Oficina.query.filter_by(email=oficina["email"]).first())
            endereco = removerInstance(EnderecoOficina.EnderecoOficina.query.filter_by(idOficina=oficina["id"]).first())
            return resposta("OK", endereco)
        except Exception as e: 
            print(e)
            return resposta("NOK", None)


#~~~~ Avaliação
class FuncoesAvaliacao(object):
    def cadastrar(dados,cliente,oficina):
        try:
            oficina = removerInstance(Oficina.Oficina.query.filter_by(email=oficina["email"]).first())
            cliente = removerInstance(Cliente.Cliente.query.filter_by(email=cliente["email"]).first())
            avaliacao = Avaliacao.Avaliacao(dados)
            avaliacao.idOficina = oficina["id"]
            avaliacao.idCliente = cliente["id"]
            db.session.add(avaliacao)
            db.session.commit()
            return resposta("OK", "")
        except Exception as e: 
            print(e)
            return resposta("NOK", None)

    def listarPorOficina(oficina):
        try:
            oficina = removerInstance(Oficina.Oficina.query.filter_by(email=oficina["email"]).first())
            avaliacoes = Avaliacao.Avaliacao.query.filter_by(idOficina=oficina["id"]).all()
            avaliacoesFormatadas = []
            for avaliacao in avaliacoes:
                avaliacoesFormatadas.append(removerInstance(avaliacao))
            return resposta("OK", avaliacoesFormatadas)
        except Exception as e: 
            print(e)
            return resposta("NOK", None)

#~~~~ Produto
class FuncoesProduto(object):
    def cadastrar(produto,oficina):
        try:
            oficina = removerInstance(Oficina.Oficina.query.filter_by(email=oficina["email"]).first())
            produto = Produto.Produto(produto)
            produto.idOficina = oficina["id"]
            db.session.add(produto)
            db.session.commit()
            return resposta("OK", "")
        except Exception as e: 
            print(e)
            return resposta("NOK", None)

    def listar(dados):
        try:
            oficina = removerInstance(Oficina.Oficina.query.filter_by(email=dados["email"]).first())
            produtos =  Produto.Produto.query.filter_by(idOficina=oficina["id"]).all()
            produtosFormatados = []
            for produto in produtos:
                produtosFormatados.append(removerInstance(produto)) 
            return resposta("OK", produtosFormatados)
        except Exception as e: 
            print(e)
            return resposta("NOK", None)


#~~~~ Ordem Servico
class FuncoesOrdemSerivo(object):
    def cadastrar(ordemServico,oficina,cliente):
        try:
            oficina = removerInstance(Oficina.Oficina.query.filter_by(email=oficina["email"]).first())
            cliente = removerInstance(Cliente.Cliente.query.filter_by(email=cliente["email"]).first())
            ordemServico = OrdemServico.OrdemServico(ordemServico)
            ordemServico.idCliente = cliente["id"]
            ordemServico.idOficina = oficina["id"]    
            ordemServico.data = int((datetime.date.today()).strftime("%d%m%Y")) 
            db.session.add(ordemServico)
            db.session.commit()
            return resposta("OK", ordemServico.id)
        except Exception as e: 
            print(e)
            return resposta("NOK", None)

    def listarOrdemServicoCliente(cliente):
        try:
            cliente = removerInstance(Cliente.Cliente.query.filter_by(email=cliente["email"]).first())
            ordemServicos = OrdemServico.OrdemServico.query.filter_by(idCliente=cliente["id"]).all()
            ordemServicosFormatados = []
            for ordemServico in ordemServicos:
                ordemServicosFormatados.append(removerInstance(ordemServico)) 
            return resposta("OK", ordemServicosFormatados)
        except Exception as e: 
            print(e)
            return resposta("NOK", None)

    def listarOrdemServicoOficina(oficina):
        try:
            oficina = removerInstance(Oficina.Oficina.query.filter_by(email=oficina["email"]).first())
            ordemServicos = OrdemServico.OrdemServico.query.filter_by(idOficina=oficina["id"]).all()
            ordemServicosFormatados = []
            for ordemServico in ordemServicos:
                ordemServicosFormatados.append(removerInstance(ordemServico)) 
            return resposta("OK", ordemServicosFormatados)
        except Exception as e: 
            print(e)
            return resposta("NOK", None)


#~~~~ Item Ordem Servico
class FuncoesItemOrdemSerivo(object):
    def cadastrar(ordemServico, produto, item):
        try:
            itemOrdemServico = ItemOrdemServico.ItemOrdemServico(item)
            itemOrdemServico.idOrdemServico =  ordemServico["id"]
            itemOrdemServico.idProduto =  produto["id"]
            db.session.add(itemOrdemServico)
            db.session.commit()
            return resposta("OK", "")
        except Exception as e: 
            print(e)
            return resposta("NOK", None)

    def listarItemOrdemServicos(ordemServico):
        try:
            itemsOrdemServico = ItemOrdemServico.ItemOrdemServico.query.filter_by(idOrdemServico=ordemServico["id"]).all()
            itemOrdemServicoFormatados = []
            for itemOrdemServico in itemsOrdemServico:
                itemOrdemServicoFormatados.append(removerInstance(itemOrdemServico))
            return resposta("OK", itemOrdemServicoFormatados)
        except Exception as e: 
            print(e)
            return resposta("NOK", None)


#~~~~ Chat
class FuncoesChat(object):
    def criar(cliente,oficina):
        try:
            chat = Chat.Chat()

            cliente = removerInstance(Cliente.Cliente.query.filter_by(email=cliente["email"]).first())
            oficina = removerInstance(Oficina.Oficina.query.filter_by(email=oficina["email"]).first())
            
            chat.idCliente = cliente["id"]
            chat.idOficina = oficina["id"]

            db.session.add(chat)
            db.session.commit()
            return resposta("OK", "")
        except Exception as e: 
            print(e)
            return resposta("NOK", None)

    def retornaChat(dados):
        CHAVE_CLIENTE = 0
        CHAVE_OFICINA = 1
        try:
            print("#")
            chats = ""
            if(dados["valor"] == CHAVE_CLIENTE):
                cliente = removerInstance(Cliente.Cliente.query.filter_by(id=dados["id"]).first())
                chats = Chat.Chat.query.filter_by(idCliente=cliente["id"]).all()

            if(dados["valor"] == CHAVE_OFICINA):
                oficina = removerInstance(Oficina.Oficina.query.filter_by(id=dados["id"]).first())
                chats = Chat.Chat.query.filter_by(idOficina=oficina["id"]).all()
     
            chatFormatados = []
            for chat in chats:
                chatFormatados.append(removerInstance(chat))
            return resposta("OK", chatFormatados)
        except Exception as e: 
            print(e)
            return resposta("NOK", None)

    def mensagem(mensagemEnviada,chat,chave):
        CHAVE_CLIENTE = 0
        CHAVE_OFICINA = 1
        try:
            msg = ChatMensagem.ChatMensagem()
            
            msg.mensagem = mensagemEnviada["texto"]
            msg.data = strftime("%d/%m/%Y %H:%M")

            chatRecuperado = removerInstance(Chat.Chat.query.filter_by(id=chat["id"]).first())

            msg.idChat = chatRecuperado["id"]
            cliente = removerInstance(Cliente.Cliente.query.filter_by(id=chatRecuperado["idCliente"]).first())
            oficina = removerInstance(Oficina.Oficina.query.filter_by(id=chatRecuperado["idOficina"]).first())

            if(chave["valor"] == CHAVE_CLIENTE):
                msg.emissor =  cliente["email"]
                msg.receptor = oficina["email"]

            if(chave["valor"] == CHAVE_OFICINA):
                msg.emissor = oficina["email"]
                msg.receptor = cliente["email"]

                fb = cliente["keyfirebase"]
                url = "https://fcm.googleapis.com/fcm/send"
                payload = {'to': fb, 'data': {'msg': msg.mensagem, 'cliente': cliente, 'oficina': oficina} }
                headers = {'Content-Type': 'application/json', 'Authorization': 'key=AAAAUj-NrpI:APA91bHzgjvmH_W5piYkJSvIpdbCWji8zYWl2FFEH7Uba7qCVoAG-6Nood9odHRwsSWKtJnN-zcGfwqorP3NMmYE0qVgmMgrQh9DmFzpf0r7cxFbx0Nr4jVLo2LwmTxV_ETusRQMimZz'}
                r = Req.post(url, data=json.dumps(payload), headers=headers)
                print(r)

            print(msg)

            db.session.add(msg)
            db.session.commit()
            return resposta("OK", "")
        except Exception as e: 
            print(e)
            return resposta("NOK", None)

    def exibirMensagens(dados):
        try:
            print(dados)
            print("#")
            chatMensagens = ChatMensagem.ChatMensagem.query.filter_by(idChat=dados["id"]).all()
            print("#")
            chatMensagensFormatados = []
            print("#")
            for mensagens in chatMensagens:
                chatMensagensFormatados.append(removerInstance(mensagens))
            print("#")
            return resposta("OK", chatMensagensFormatados)
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

    