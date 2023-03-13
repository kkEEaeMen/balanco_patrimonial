from persistencias import *

def menu(nome_arquivo):
  opcoes = int(input(" 1 - Inserir Item\n 2 - Alterar Item\n 3 - Remover Item\n 4 - Salvar Arquivo\n 5 - Fechar\n "))
  print(10*"-=")
  match opcoes:
    case 1:
      inserir_itens(nome_arquivo)
    case 2:
      alterar_itens(nome_arquivo)
    case 3:
      remover_itens(nome_arquivo)
    case 4:
      salva_arquivo(nome_arquivo)
    case 5:
      pass
    case _:
      print("Opção invalida")

def inserir_itens(nome_arquivo):
  opcoes = int(input(" 1 - Caixa\n 2 - Imoveis\n 3 - Contas a Pagar\n 4 - Capital Social\n 5 - Novo\n 0 - Voltar\n "))
  match opcoes:
    case 1:
      if detectar_itens(nome_arquivo, "Caixa") == False:
        nome_produto = "Caixa"
        preco_produto = float(input("Digite o valor do item cadastrado:\n "))
        classificacao(preco_produto, nome_produto)
      else:
        print("Item já cadastrado")
    case 2:
      if detectar_itens(nome_arquivo, "Imoveis") == False:
        nome_produto = "Imoveis"
        preco_produto = float(input("Digite o valor do item cadastrado:\n "))
        classificacao(preco_produto, nome_produto)
      else:
        print("Item já cadastrado")
    case 3:
      if detectar_itens(nome_arquivo, "Contas a Pagar") == False:
        nome_produto = "Contas a Pagar"
        preco_produto = float(input("Digite o valor do item cadastrado:\n "))
        classificacao(preco_produto, nome_produto)
      else:
        print("Item já cadastrado")
    case 4:
      if detectar_itens(nome_arquivo, "Capital Social") == False:
        nome_produto = "Capital Social"
        preco_produto = float(input("Digite o valor do item cadastrado:\n "))
        classificacao(preco_produto, nome_produto)
      else:
        print("Item já cadastrado")
    case 5:
      nome_novo_produto = input("Digite o nome do produto:\n ")
      if detectar_itens(nome_arquivo, nome_novo_produto) == False:
        preco_produto = float(input("Digite o valor do item cadastrado:\n "))
        classificacao(preco_produto, nome_novo_produto)
      else:
        print("Item já cadastrado")
    case 0:
      menu(nome_arquivo)
    case _:
      print("Opção invalida")

def classificacao(preco_produto, nome_produto):
  classificacoes = int(input(" 1 - Ativo Circulante\n 2 - Ativo Não Circulante\n 3 - Passivo Circulante\n 4 - Passivo Não Circulante\n 5 - Patrimônio Liquido\n "))
  match classificacoes:
    case 1:
      cadastro("AC", preco_produto, nome_produto)
    case 2:
      cadastro("ANC", preco_produto, nome_produto)
    case 3:
      cadastro("PC", preco_produto, nome_produto)
    case 4:
      cadastro("PNC", preco_produto, nome_produto)
    case 5:
      cadastro("PL", preco_produto, nome_produto)

def deseja_continuar(parada):
  op = input("Deseja continuar[s/n]: ")
  if(op == 'n' or op == 'N'):
    parada = False
    return parada
  elif(op == 's' or op == 'S'):
    return parada
  else:
    print("opção invalida")