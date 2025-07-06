#Funções:

#Letra B) Função escolha_serviço:
def escolha_servico ():
    # Menu para opções, se houver uma digitação de escolha errada o usuário poderá digitar novamente
    while True:
        # Tentativa de captação de escolha do serviço para o usuário
        try:
            # impressão opções
            print("Escolha um dos Serviços Abaixo:")
            print("DIG = Digitalização ------------------- R$1,10")
            print("ICO = Impressão Colorida -------------- R$1,00")
            print("IPB = Impressão em Preto e Branco------ R$0,40")
            print("FOT = Fotocópia ----------------------- R$0,20")
            # retorno da escolha do usuário
            servico = input("Digite o serviço desejado: (Por gentileza digitar com letras maiúsculas)\n")
            # Caso o usuário tenha digitado corretamente uma das opções o loop acaba, independentemente da tentativa. Senão o loop reiniciará
            if servico == "DIG" or servico == "ICO" or servico == "IPB" or servico == "FOT":
                return servico
            else:
                print("Serviço Inválido. Tente novamente!")
                continue
        # Caso ocorra uma falha no valor digitado e ele não seja nem mesmo uma string, o loop reinicia e dá nova chance ao usuário
        except ValueError:
            print("Tipo de dado digitado inválido. Tente novamente!")
            continue
        # Caso o loop do try e while sejam finalizados a função escolha_servico acaba com o retorno do servico desejado

# Letra C) Função num_paginas
def num_pagina():
    # While para que caso haja uma digitação errada, assim o usuário poderá digitar novamente
    while True:
        # Tentativa de captação de escolha do serviço para o usuário
        try:
            print("Agora escreva a quantidade de páginas desejadas...")
            # retorno da escolha do usuário
            pags = int(input())
            # De acordo com a resposta do usuário sobre a quantidade de páginas, o programa aplicará uma quantidade espedífica de desconto. O programa não permite um valor abaixo de 1 e acima de 20000
            if pags <= 0:
                print("Valor inválido. Tente novamente!")
                continue
            elif (pags > 1 and pags < 20):
                return pags
            elif (pags >= 20 and pags < 200):
                desconto = 15
                pags = pags * ((100 - desconto) / 100)
            elif (pags >= 200 and pags < 2000):
                desconto = 20
                pags = pags * ((100 - desconto) / 100)
            elif (pags >= 2000 and pags <= 20000):
                desconto = 25
                pags = pags * ((100 - desconto) / 100)
            else:
                print("Não aceitamos tantas páginas de uma vez! Limite de 20000 por pedido")
                continue
        except ValueError:
            print("Valor inserido inválido. Tente novamente!")
            continue
        else:
            return pags

# Letra D) Função servico_extra
def servico_extra():
    # Menu para opções, se houver uma digitação de escolha errada o usuário poderá digitar novamente
    while True:
        # Tentativa de captação de escolha do serviço para o usuário
        try:
            # impressão opções
            print("Deseja algum serviço extra?")
            print("0 - Nenhum ---------------------- R$0,00")
            print("1 - Encadernação simples--------- R$15,00")
            print("2 - Encadernação de capa dura---- R$40,00")
            # retorno da escolha do usuário
            adicional = int(input("Digite o número desejado...\n"))
            # Caso o usuário tenha digitado corretamente uma das opções o loop acaba, independentemente da tentativa. Senão o loop reiniciará
            if (adicional == 0):
                valor_add = 0
                return valor_add
            elif (adicional == 1):
                valor_add = 15
            elif (adicional == 2):
                valor_add = 40
            else:
                print('Serviço extra inválido. Tente novamente!')
                continue

        # Caso ocorra uma falha no valor digitado e ele não seja nem mesmo um int, o loop reinicia e dá nova chance ao usuário
        except ValueError:
            print("Valor inserido inválido. Tente novamente!")
            continue
        # Caso o loop do try e while sejam finalizados, a função servico_extra acaba com o retorno do servico extra desejado
        else:
            return valor_add



#Programa Principal:

#Letre A) Mensagem de boas vindas:
print("Olá, seja bem vindo a Loja do Guilherme Lima")
# Letra B) Aplicação em variável do retorno da função escolha_servico:
servico = escolha_servico()
# Letra C) Aplicação em variável do retorno da função num_pagina:
paginas = num_pagina()
# Letra D) Aplicação em variável do retorno da função servico_extra:
extra = servico_extra()
# Letra E) Implementação do valor de pagamento:
pag_val = 0
if servico == "DIG":
    pag_val = 1.10
elif servico == "ICO":
    pag_val = 1.00
elif servico == "IPB":
    pag_val = 0.40
elif servico == "FOT":
    pag_val = 0.20

total_pagar = (paginas * pag_val) + extra
print(f"Serviço escolhido é de R${pag_val:.2f} por {paginas} páginas e com a solicitação de um extra de: {extra:.2f}")
print(f"Pedido finalizado, o total a pagar é de R${total_pagar:.2f}")
