nome_arquivo = "Oi.txt"



b = "AC Caixa 1800.00\n"


def substitui_elemento(leitura, indice, classificacao, nome, valor): 
    """ Faz substituição no array ( fora do txt ) """
    produto = classificacao + " " + nome + " " + valor + "\n"
    leitura.remove(b)
    leitura.insert(indice, produto)
    salva_arquivo(leitura)

def salva_arquivo(leitura_modificada):
    """ Envia de volta todo array, com a respectiva modificação """
    arquivo2 = open(nome_arquivo, 'w', encoding='utf-8')
    for i in leitura_modificada:
        arquivo2.write(i)

def novas_infos():
    """ Pega tudo que tem dentro do arquivo txt e  chama função para modificação dos dados
    fora do arquivo txt """
    arquivo = open(nome_arquivo, 'r', encoding='utf-8')
    leitura = arquivo.readlines()
    for i in range(len(leitura)):
        if leitura[i] == b:
            indice = leitura.index(leitura[i])
            classificacao = input("Classificacao: ")
            nome = input("Nome ")
            valor = input("Valor: ")
            substitui_elemento(leitura, indice, classificacao, nome, valor)
