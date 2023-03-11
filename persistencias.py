from telas import *

elementos = []

def gerar_arquivo(nome_arquivo):
  try:
    arquivo = open(nome_arquivo, 'x', encoding='utf-8')
  except:
    print("Arquivo já existente !")
  else:
    print("Arquivo criado com sucesso !")

def salva_arquivo(dado_formatdo, nome_arquivo):
  arquivo = open(nome_arquivo, 'w', encoding='utf-8') # Mudar modo de gravar
  arquivo.write(dado_formatdo)
=======
   with open(nome_arquivo,'w', encoding='utf-8') as arquivo:
      print("Arquivo criado com sucesso !")
>>>>>>> d6f4dd2e70822af8e31e120e0a4660ff396b24d9

def gravar_arquivo():
  pass

def ler_arquivo(nome_arquivo):
<<<<<<< HEAD
  arquivo = open(nome_arquivo, 'r', encoding='utf-8')
  leitura = arquivo.readlines()
  exibir_balanco(leitura)
  gerar_balanco(leitura)

def cadastro(classificacao, preco, nome_produto, nome_arquivo):
  if classificacao == "Ativo Circulante":
        dado_formatado = classificacao + " " + nome_produto + " " + preco
        salvar = input("Deseja salvar as informações ? (s/n)\n ").lower()
        match (salvar):
          case "s":
            salva_arquivo(dado_formatado, nome_arquivo)

def exibir_balanco(leitura: list):
  print("")
  for i in leitura:
    print(i, end = "")

def gerar_balanco(leitura: list):
  ativos, passivos, patrimonios = [], [], []
  ativos_totais, passivos_totais, patrimonios_totais = 0, 0, 0
  for i in range(len(leitura)):
    linha = leitura[i].split()
    match linha[0]:
      case 'AC':
        ativos.append(float(linha[-1]))
      case 'ANC':
        ativos.append(float(linha[-1]))
      case 'PC':
        passivos.append(float(linha[-1]))
      case 'PNC':
        passivos.append(float(linha[-1]))
      case 'PL':
        patrimonios.append(float(linha[-1]))
  ativos_totais = sum(ativos)
  passivos_totais = sum(passivos)
  patrimonios_totais = sum(patrimonios)
  print("\n")
  print(f"Total de ativos = {ativos_totais}")
  print(f"Total de passivos = {passivos_totais}")
  print(f"Total de Patrimonio Liquido = {patrimonios_totais}")
  print(f"Total de passivos e Patrimonio Liquido = {passivos_totais + patrimonios_totais}\n")
  if ativos_totais == passivos_totais + patrimonios_totais:
    print("O balanço está correto\n")
  else:
    print("O balanço está incorreto\n")
=======
   arquivo = open(nome_arquivo, 'r', encoding='utf-8')
   leitura = arquivo.readlines()
   for i in leitura:
      print(i)

def cadastro(classificao):
  pass
>>>>>>> d6f4dd2e70822af8e31e120e0a4660ff396b24d9
