from persistencias import *
from telas import *
from inicializacao import *

parada = True
while parada:
  nome_arquivo = inicializar()
  menu(nome_arquivo)
  ler_arquivo(nome_arquivo)
  parada = deseja_continuar(parada)

parada = 1
while parada:
  nome_arquivo = inicializar()
  menu()
  ler_arquivo(nome_arquivo)
  op = input("Deseja continuar: ")
  if(op == 'n'):
    parada = 0

