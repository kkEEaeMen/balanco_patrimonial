from persistencias import *

def inicializar():
  print("1 - Criar novo Arquivo\n2 - Abrir Arquivo")
  op = input("Escolha uma Opção: ")
  match (op):
    case 1:
      gerar_nome_arquivo = input("Digite o nome do arquivo: ")
      nome_arquivo = gerar_nome_arquivo + ".txt"
      gerar_arquivo(nome_arquivo)
      return nome_arquivo
    case 2:
      pass