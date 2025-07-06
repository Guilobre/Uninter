# Letra A) Boas vindas ao cliente
print("Bem vindo a Loja de Guilherme Lima")


# Letra B) Solicitação de informações do produto e compra e cálculo do valor bruto:
# Utilizei o float ao invés do int por preços com valores quebrados e caso não se compre um produto inteiro, um bolo ou uma fatia dele, por exemplo.
valor_prod = float(input("Por gentileza, entre com o valor unitário do produto:\n"))
quant_prod = float(input("Por gentileza, entre com a quantidade do produto:\n"))
valor_bruto = valor_prod * quant_prod


# Letra C  Aplicação do desconto em cada caso específico:
if (valor_bruto < 2500):
    desconto = 0
elif (valor_bruto >= 2500 and valor_bruto < 6000):
    desconto = 4
elif (valor_bruto >= 6000 and valor_bruto < 10000):
    desconto = 7
else:
    desconto = 11


# Letra D) Cálculo e exibição dos valores totais com e sem desconto:
valor_final = valor_bruto * ((100 - desconto)/100)
print(f"Valor total da compra SEM descontos: R${valor_bruto}")
print(f"Valor total da compra COM desconto de {desconto}%: R${valor_final}")
