# Declaração de variáveis:

# Letra e)
total_compra = 0

# Letra a) exigência de cód 1/8:
print("Olá, seja bem vindo a Loja de Guilherme Lima\n")
print("Cardápio:")
print("----------------------------------")
print("|Tamanhos:|Cupuaçu (CP)|Açai (AC)|")
print("|   P     |    R$9,00  | R$11,00 |")
print("|   M     |   R$14,00  | R$16,00 |")
print("|   G     |   R$18,00  | R$20,00 |")
print("----------------------------------")

while True:

    # Letra b) Exigência de código 2/8:
    while True:
        print(f"No momento, o valor total da compra é de: R${total_compra}")

        sabor = input("Selecione um sabor... (Digite: CP para Cupuaçu ou AC para Açai)   ")
        if (sabor != "CP" and sabor != "AC" and sabor != "cp" and sabor != "ac"):
            print("Sabor inválido, tente novamente!\n")
            continue
        else:
            break

    # Letra c) Exigência de código 3/8:
    while True:
        tam = input("Selecione um tamanho...(Digite P = pequeno ou M = Médio ou G = Grande)")
        if tam != "P" and tam != "p" and tam != "M" and tam != "m" and tam != "G" and tam != "g":
            print("Tamanho inválido, tente novamente!\n")
            continue

        else:
            break

    # Letra d) Exigência de código 4/8:
    if sabor == "CP" or sabor == "cp":

        if tam == "P" or tam == "p":
            preco = 9
            total_compra += preco
        elif tam == "M" or tam == "m":
            preco = 14
            total_compra += preco
        else:
            preco = 18
            total_compra += preco

    if sabor == "AC" or sabor == "ac":

        if tam == "P" or tam == "p":
            preco = 11
            total_compra += preco
        elif tam == "M" or tam == "m":
            preco = 16
            total_compra += preco
        else:
            preco = 20
            total_compra += preco

    # Letra e) Exigência de código 5/8:
    # Acumulador feito através da criação da variável total_compra na linha 2


    # Letra f) Exigência de código 6/8
    while True:

        outro = input("Deseja pedir mais alguma coisa?\nS = Sim\nN = Não\n")
        if outro == "S" or outro == "s":
            break
        elif outro == "N" or outro == "n":
            break
        else:
            print("Resposta inválida, tente novamente!")
            continue
    if outro == "S" or outro == "s":
        continue
        # Esse print é apenas para pular uma linha antes do início de outro pedido
        print("")

    elif outro == "N" or outro == "n":
        break

print(f"Finalizando a compra...\nSua compra terminou com o total de R${total_compra}")