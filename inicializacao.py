from persistencias import *

def inicializar() -> str:
  print("1 - Criar novo Arquivo\n2 - Abrir Arquivo")
  op = int(input("Escolha uma Opção: "))
  gerar_nome_arquivo = input("Digite o nome do arquivo: ")
  nome_arquivo = gerar_nome_arquivo + ".txt"
  match (op):
    case 1:
      gerar_arquivo(nome_arquivo)
      return nome_arquivo
    case 2:
      ler_arquivo(nome_arquivo)
      return nome_arquivo