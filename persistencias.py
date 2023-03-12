def gerar_arquivo(nome_arquivo):
  try:
    arquivo = open(nome_arquivo, 'x', encoding='utf-8')
  except:
    print("Arquivo já existente !")
  else:
    print("Arquivo criado com sucesso !")

def salva_arquivo(dado_formatdo, nome_arquivo):
  arquivo = open(nome_arquivo, 'a', encoding='utf-8')
  arquivo.write(f"{dado_formatdo}\n")


def ler_arquivo(nome_arquivo):
  arquivo = open(nome_arquivo, 'r', encoding='utf-8')
  leitura = arquivo.readlines()
  exibir_balanco(leitura)
  gerar_balanco(leitura)

def cadastro(classificacao, preco, nome_produto, nome_arquivo):
  if classificacao == "AC":

        dado_formatado = classificacao + " " + nome_produto + " " + str(preco)

        salvar = input("Deseja salvar as informações ? (s/n)\n ").lower()
        match (salvar):
          case "s":
            salva_arquivo(dado_formatado, nome_arquivo)

  if classificacao == "ANC":
        dado_formatado = classificacao + " " + nome_produto + " " + str(preco)
        salvar = input("Deseja salvar as informações ? (s/n)\n ").lower()
        match (salvar):
          case "s":
            salva_arquivo(dado_formatado, nome_arquivo)

  if classificacao == "PC":
        dado_formatado = classificacao + " " + nome_produto + " " + str(preco)
        salvar = input("Deseja salvar as informações ? (s/n)\n ").lower()
        match (salvar):
          case "s":
            salva_arquivo(dado_formatado, nome_arquivo)

  if classificacao == "PNC":
        dado_formatado = classificacao + " " + nome_produto + " " + str(preco)
        salvar = input("Deseja salvar as informações ? (s/n)\n ").lower()
        match (salvar):
          case "s":
            salva_arquivo(dado_formatado, nome_arquivo)

  if classificacao == "PL":
        dado_formatado = classificacao + " " + nome_produto + " " + str(preco)
        salvar = input("Deseja salvar as informações ? (s/n)\n ").lower()
        match (salvar):
          case "s":
            salva_arquivo(dado_formatado, nome_arquivo)

            # colocar versao alternativa ao SIM

            #colocar versao alternativa ao SIM


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