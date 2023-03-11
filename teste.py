lista_AC = ["Ativo_Circulante"]
lista_ANC = ["Ativo_Não_Circulante"]
lista_PC = ["Passivo_Circulante"]
lista_PNC = ["Passivo_Não_Circulante"]
lista_PL = ["Passivo_Líquido"]
lista_p = [lista_AC, lista_ANC, lista_PC, lista_PNC, lista_PL]

# lista = ["1","2","3","4"]
nome_arquivo = "oi.txt"

arquivo = open(nome_arquivo, 'w', encoding='utf-8')


dado = input("insira: ")
opc = int(input(" insira a opc: "))
match (opc):
    case 1:
        arquivo.write("AC" + " " + dado)
        arquivo.write("\n")

arquivo.close


# arquivo.write(line[cont])
# arquivo.write("\n")


# lista_AC = ["Ativo_Circulante"]
# lista_ANC = ["Ativo_Não_Circulante"]
# lista_PC = ["Passivo_Circulante"]
# lista_PNC = ["Passivo_Não_Circulante"]
# lista_PL = ["Passivo_Líquido"]
# # lista_p = [lista_AC, lista_ANC, lista_PC, lista_PNC, lista_PL]

# # lista = ["1","2","3","4"]
# nome_arquivo = "oi.txt"

# arquivo = open(nome_arquivo, 'w', encoding='utf-8')


# dado = input("insira: ")
# classi = int(input("Insira a classificacao: "))


# for i in lista_AC: 
#     print(i)
#     # arquivo.write(i)
#     # arquivo.write("\n")