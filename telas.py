from persistencias import *

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

