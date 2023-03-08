from persistencias import *
from telas import *

while True:
    def inicializar():
        gerar_nome_arquivo = input("Digite o nome do arquivo: ")
        nome_arquivo = gerar_nome_arquivo + ".txt"
        gerar_arquivo(nome_arquivo)
        menu()
        
    def menu():
        opcoes = int(input(" 1 - Inserir Item\n 2 - Alterar Item\n 3 - Remover Item\n 4 - Salvar Arquivo\n 5 - Fechar\n "))
        print(10*"-=")
        items(opcoes)
        
        
        # opcoes3 = input(" 1 - Criar Novo Balanço\n 2 - Abrir Balanço ")


    inicializar()
    