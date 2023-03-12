from persistencias import *
from telas import *
from inicializacao import *

parada_arquivo = True
parada_leitura = True

while parada_arquivo:
  nome_arquivo = inicializar()
  while parada_leitura:
    menu(nome_arquivo)
    parada_leitura = deseja_continuar(parada_leitura)
  ler_arquivo(nome_arquivo)
  parada_arquivo = deseja_continuar(parada_arquivo)