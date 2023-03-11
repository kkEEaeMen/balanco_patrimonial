from persistencias import *

def menu(nome_arquivo):
  opcoes = int(input(" 1 - Inserir Item\n 2 - Alterar Item\n 3 - Remover Item\n 4 - Salvar Arquivo\n 5 - Fechar\n "))
  print(10*"-=")
  items(opcoes, nome_arquivo)


def items(opcao, nome_arquivo):
  if ( opcao == 1):
    opcoes2 = int(input(" 1 - Caixa\n 2 - Imoveis\n 3 - Contas a Pagar\n 4 - Capital Social\n 5 - Novo\n 0 - Voltar\n "))
    match opcoes2:
      case 1:
        nome_produto = "Caixa"
        preco_produto = float(input("Digite o valor do item cadastrado:\n "))
        classificacao(preco_produto, nome_produto, nome_arquivo)
      case 2:
        nome_produto = "Imoveis"
        preco_produto = float(input("Digite o valor do item cadastrado:\n "))
        classificacao(preco_produto, nome_produto, nome_arquivo)
      case 3:
        nome_produto = "Contas a Pagar"
        preco_produto = float(input("Digite o valor do item cadastrado:\n "))
        classificacao(preco_produto, nome_produto, nome_arquivo)
      case 4:
        nome_produto = "Capital Social"
        preco_produto = float(input("Digite o valor do item cadastrado:\n "))
        classificacao(preco_produto, nome_produto, nome_arquivo)
      case 5:
        nome_novo_produto = input("Digite o nome do produto:\n ")
        preco_produto = float(input("Digite o valor do item cadastrado:\n "))
        classificacao(preco_produto, nome_novo_produto, nome_arquivo)        


def classificacao(preco_produto, nome_produto, nome_arquivo):
  classificacoes = int(input(" 1 - Ativo Circulante\n 2 - Ativo Não Circulante\n 3 - Passivo Circulante\n 4 - Passivo Não Circulante\n 5 - Patrimônio Liquido\n "))
  match classificacoes:
    case 1:
      AC = "Ativo Circulante"
      cadastro(AC, preco_produto, nome_produto, nome_arquivo)
    case 2:
      ANC = "Ativo Não Circulante"
      cadastro(ANC, preco_produto, nome_produto, nome_arquivo)
    case 3:
      PC = "Passivo Circulante"
      cadastro(PC, preco_produto, nome_produto, nome_arquivo)
    case 4:
      PNC = "Passivo Não Circulante"
      cadastro(PNC, preco_produto, nome_produto, nome_arquivo)
    case 5:
      PL = "Patrimônio Liquido"
      cadastro(PL, preco_produto, nome_produto, nome_arquivo)

def deseja_continuar(parada):
  op = input("Deseja continuar[s/n]: ")
  if(op == 'n' or op == 'N'):
    parada = False
    return parada
  elif(op == 's' or op == 'S'):
    return parada
  else:
    print("opção invalida")
=======

def menu():
  opcoes = int(input(" 1 - Inserir Item\n 2 - Alterar Item\n 3 - Remover Item\n 4 - Salvar Arquivo\n 5 - Fechar\n "))
  print(10*"-=")
  items(opcoes)

def items(opcao):
    if ( opcao == 1):
        opcoes2 = int(input(" 1 - Caixa\n 2 - Imoveis\n 3 - Contas a Pagar\n 4 - Capital Social\n 5 - Novo\n 0 - Voltar\n "))
        match opcoes2:
            case 1:
                preco_produto = float(input("Digite o valor do item cadastrado:\n "))
                classificacao(preco_produto)
            case 5:
              nome_novo_produto = input("Digite o nome do produto:\n ")
              preco_produto = float(input("Digite o valor do item cadastrado:\n "))
              classificacao(preco_produto)
              
              
def classificacao(preco_produto):
    classificacoes = int(input(" 1 - Ativo Circulante\n 2 - Ativo Não Circulante\n 3 - Passivo Circulante\n 4 - Passivo Não Circulante\n 5 - Patrimônio Liquido\n "))
    match classificacao:
        case 1:
          AC = "Ativo Circulante"
          cadastro(AC)
        case 2:
          ANC = "Ativo Não Circulante"
          cadastro(ANC)
        case 3:
          PC = "Passivo Circulante"
          cadastro(PC)
        case 4:
          PNC = "Passivo Não Circulante"
          cadastro(PNC)
        case 5:
          PL = "Patrimônio Liquido"
          cadastro(PL)

>>>>>>> d6f4dd2e70822af8e31e120e0a4660ff396b24d9
