from persistencias import *
from telas import *
from inicializacao import *

<<<<<<< HEAD
parada = True
while parada:
  nome_arquivo = inicializar()
  menu(nome_arquivo)
  ler_arquivo(nome_arquivo)
  parada = deseja_continuar(parada)

=======
parada = 1
while parada:
  nome_arquivo = inicializar()
  menu()
  ler_arquivo(nome_arquivo)
  op = input("Deseja continuar: ")
  if(op == 'n'):
    parada = 0
>>>>>>> d6f4dd2e70822af8e31e120e0a4660ff396b24d9
