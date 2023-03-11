from persistencias import *
from telas import *
from inicializacao import *

parada = True
while parada:
  nome_arquivo = inicializar()
  menu(nome_arquivo)
  ler_arquivo(nome_arquivo)
  parada = deseja_continuar(parada)

