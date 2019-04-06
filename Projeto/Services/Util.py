from Models import Avaliacao, Cartao, Chat, ChatMensagem, Cliente, EnderecoOficina, ItemOrdemServico, Oficina, OrdemServico, Produto
from Server import db

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
            print(cliente)
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


#~~~~ Oficina
class FuncoesOficina(object):
    def cadastrar(dados):
        try:
            oficina = Oficina.Oficina(dados)
            print(oficina)
            db.session.add(oficina)
            db.session.commit()
            return resposta("OK", "")
        except Exception as e: 
            print(e)
            return resposta("NOK", None)

    def listar():
        try:
            oficinas =  Oficina.Oficina.query.all()
            print(oficinas)
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
                print(avaliacao)
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
            db.session.add(ordemServico)
            db.session.commit()
            return resposta("OK", "")
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