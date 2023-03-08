from telas import *

elementos = []

def gerar_arquivo(nome_arquivo):
   with open(nome_arquivo,'w', encoding='utf-8') as arquivo:
      print("Arquivo criado com sucesso !")

def gravar_arquivo():
  pass

def ler_arquivo(nome_arquivo):
   arquivo = open(nome_arquivo, 'r', encoding='utf-8')
   leitura = arquivo.readlines()
   for i in leitura:
      print(i)

def cadastro(classificao):
  pass