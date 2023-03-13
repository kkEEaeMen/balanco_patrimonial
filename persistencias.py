salvar = []

def gerar_arquivo(nome_arquivo):
  try:
    arquivo = open(nome_arquivo, 'x', encoding='utf-8')
  except:
    print("Arquivo já existente !")
  else:
    print("Arquivo criado com sucesso !")

def salva_arquivo(nome_arquivo):
  arquivo = open(nome_arquivo, 'a', encoding='utf-8')
  for i in salvar:
    arquivo.write(f"{i}\n")
  salvar.clear()

def ler_arquivo(nome_arquivo):
  arquivo = open(nome_arquivo, 'r', encoding='utf-8')
  leitura = arquivo.readlines()
  exibir_balanco(leitura)
  gerar_balanco(leitura)

def cadastro(classificacao, preco, nome_produto):
  match classificacao:
    case "AC":
      dado_formatado = classificacao + " " + nome_produto + " " + str(preco)
      salvar.append(dado_formatado)
    case "ANC":
      dado_formatado = classificacao + " " + nome_produto + " " + str(preco)
      salvar.append(dado_formatado)
    case "PC":
      dado_formatado = classificacao + " " + nome_produto + " " + str(preco)
      salvar.append(dado_formatado)
    case "PNC":
      dado_formatado = classificacao + " " + nome_produto + " " + str(preco)
      salvar.append(dado_formatado)
    case "PL":
      dado_formatado = classificacao + " " + nome_produto + " " + str(preco)
      salvar.append(dado_formatado)

def detectar_itens(nome_arquivo, item):
  arquivo = open(nome_arquivo, 'r', encoding='utf-8')
  leitura = arquivo.readlines()
  item = item.split()
  for i in range(len(leitura)):
    linha = leitura[i].split()
    linha.pop(0)
    linha.pop(-1)
    if item == linha:
      return i + 1
  return False

def alterar_itens(nome_arquivo): # não está funcionando
  item_comparador = []
  item = input("Qual item quer alterar: ")
  arquivo = open(nome_arquivo, 'r', encoding='utf-8')
  leitura = arquivo.readlines()
  item_comparador.append(item)
  for i in range(len(leitura)):
    linha = leitura[i].split()
    linha.pop(0)
    linha.pop(-1)
    if item_comparador == linha:
      classificacao = input("Nova classificação: ")
      nome = input("Nova Nome: ")
      valor = float(input("Nova Valor: "))
      produto = classificacao + " " + nome + " " + str(valor)
      leitura.remove(leitura[i])
      leitura.insert(i, produto)
  arquivo.close()
  arquivo = open(nome_arquivo, 'w', encoding='utf-8')
  for i in leitura:
    arquivo.write(f"{i}\n")
  arquivo.close()

def remover_itens(nome_arquivo):
  item_comparador = []
  item = input("Qual item quer remover: ")
  arquivo = open(nome_arquivo, 'r', encoding='utf-8')
  leitura = arquivo.readlines()
  item_comparador.append(item)
  for i in range(len(leitura)):
    linha = leitura[i].split()
    linha.pop(0)
    linha.pop(-1)
    if item_comparador == linha:
      leitura.remove(leitura[i])
      leitura.insert(i, "")
  arquivo.close()
  arquivo = open(nome_arquivo, 'w', encoding='utf-8')
  for i in leitura:
    arquivo.write(f"{i}")
  arquivo.close()
  arquivo = open(nome_arquivo, 'a', encoding='utf-8')
  arquivo.write("\n")
  arquivo.close()

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