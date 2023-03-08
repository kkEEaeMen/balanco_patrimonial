def classificacao():
    classificacoes = int(input(" 1 - Ativo Circulante\n 2 - Ativo Não Circulante\n 3 - Passivo Circulante\n 4 - Passivo Não Circulante\n 5 - Patrimônio Liquido\n "))

def items(opcao):
    if ( opcao == 1):
        opcoes2 = int(input(" 1 - Caixa\n 2 - Imoveis\n 3 - Contas a Pagar\n 4 - Capital Social\n 5 - Novo\n 0 - Voltar\n "))
        match opcoes2:
            case 1:
                preco_produto = float(input("Digite o valor do item cadastrado:\n "))
                classificacao()


    