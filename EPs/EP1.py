# ALUNA: Luiza Pauli de Castro

from os import system , name

def limpaTela():
    """
    Função responsável por limpar o terminal.
    """
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def iteracao(i = 1):
    """
    Função responsável por contar as iterações do programa e limpar o terminal após cada uma.
    """
    limpaTela()
    if i >= 5: # Finaliza o programa após 5 iterações
        print()
        print("Obrigada pela preferência!")
        print("Volte sempre! :D")
        print()
        exit()

def bemVindo():
    """
    Função responsável por imprimir a tela de boas vindas.
    """
    RST     = '\033[00m'
    VIOLET  = '\033[35m'
    YELLOW  = '\033[33m'

    print(VIOLET)
    print(" ____  ____    __   __     ____  ____  _  _       _  _  __  __ _  ____   __ ")
    print("/ ___)(  __) _(  ) / _\   (  _ \(  __)( \/ ) ___ / )( \(  )(  ( \(    \ /  \ ")
    print("\___ \ ) _) / \) \/    \   ) _ ( ) _) / \/ \(___)\ \/ / )( /    / ) D ((  O )")
    print("(____/(____)\____/\_/\_/  (____/(____)\_)(_/      \__/ (__)\_)__)(____/ \__/ ")
    print(RST)
    print(YELLOW)
    input(">> Aperte Enter para continuar... <<")
    print(RST)

def menuInicial(p1, p2, p3, p4, p5):
    """
    Função responsável por imprimir o Menu Inicial de acordo com a disponibilidade dos produtos.

    Parâmetros:
        p1: Quantidade do produto 1
        p2: Quantidade do produto 2
        p3: Quantidade do produto 3
        p4: Quantidade do produto 4
        p5: Quantidade do produto 5
    """
    # WHITE  = '\033[37m'
    # YELLOW = '\033[33m'
    # GRAY   = '\033[30m'
    VIOLET   = '\033[35m'
    RST      = '\033[00m'

    p1a = p2a = p3a = p4a = p5a = 0
    p1a = "\033[30mINDISPONÍVEL\033[35m  " if p1 == 0 else "R$ 15,00      "
    p2a = "\033[30mINDISPONÍVEL\033[35m  " if p2 == 0 else "R$ 10,00      "
    p3a = "\033[30mINDISPONÍVEL\033[35m  " if p3 == 0 else "R$ 25,00      "
    p4a = "\033[30mINDISPONÍVEL\033[35m  " if p4 == 0 else "R$ 6,00      "
    p5a = "\033[30mINDISPONÍVEL\033[35m  " if p5 == 0 else "R$ 5,00      "


    print(VIOLET)


    print("\033[33m  \ /                                              \ /")
    print("-- o --\033[35m------------PRODUTOS DISPONÍVEIS----------\033[33m-- o --\033[35m")
    print("   |                                                |")
    print(f"   | 1 - \033[37mLámen Ichiraku\033[35m...............{p1a}|")
    print("   |                                                |")
    print(f"   | 2 - \033[37mMitarashi\033[35m....................{p2a}|")
    print("   |                                                |")
    print(f"   | 3 - \033[37mCurry Rock Lee\033[35m...............{p3a}|")
    print("   |                                                |")
    print(f"   | 4 - \033[37mOnigri Uchiha\033[35m.................{p4a}|")
    print("   |                                                |")
    print(f"   | 5 - \033[37mPílulas Sakura\033[35m................{p5a}|")
    print("   |                                                |")
    print("   +--------------------SABER MAIS------------------+")
    print("   |                                                |")
    print("   | 6 - \033[37mInformações Internas\033[35m                       |")
    print("   | 7 - \033[37mFinalizar\033[35m                                  |")
    print("\033[33m-- o --\033[35m------------------------------------------\033[33m-- o --")
    print("  / \                                              / \ ")
    print()
    
    print(RST)

def opcaoEscolha():
    """
    Função responsável por receber a escolha do usuário e verificar se o valor é válido.

    Retorno:
        opcao: Opção válida escolhida pelo cliente
    """
    GREEN   = '\033[32m'
    RED     = '\033[31m'
    RST     = '\033[00m'

    while True:
        opcao = input("Escolha a opção desejada: ")

        try:
            opcao = int(opcao)
            if opcao > 0 and opcao <= 7:
                print(GREEN)
                print("Opção escolhida")
                print(RST)
                return opcao
            else:
                print(RED)
                print("Opção Inválida! Digite um número inteiro de 1 a 7.")
                print(RST)
        except:
            print(RED)
            print("Opção Inválida! Digite um número inteiro de 1 a 7.")
            print(RST)

def pagamento(valor, n20, n10, n5, n2, m1, m50):
    """
    Função responsável por receber o produto escolhido, somar o valor das notas/moedas inseridas pelo cliente
    e contar quantas notas/moedas de cada valor foram inseridas.

    Parâmetros:
        valor: Valor do produto selecionado
        n20: Quantidade de notas de 20 reais
        n10: Quantidade de notas de 10 reais
        n5: Quantidade de notas de 5 reais
        n2: Quantidade de notas de 2 reais
        m1: Quantidade de moedas de 1 real
        m50: Quantidade de moedas de 50 centavos

    Retorno:
        precisaTroco: True/False de acordo com a necessidade de troco
        v: Valor total pago pelo cliente
        n20: Quantidade de notas de 20 reais
        n10: Quantidade de notas de 10 reais
        n5: Quantidade de notas de 5 reais
        n2: Quantidade de notas de 2 reais
        m1: Quantidade de moedas de 1 real
        m50: Quantidade de moedas de 50 centavos
        trocoValor: Valor do troco necessário
        aum20: Váriavel contadora da respectiva nota
        aum10: Váriavel contadora da respectiva nota
        aum5: Váriavel contadora da respectiva nota
        aum2: Váriavel contadora da respectiva nota
        aum1: Váriavel contadora da respectiva moeda
        aum50: Váriavel contadora da respectiva moeda

    """
    GREEN   = '\033[32m'
    RED     = '\033[31m'
    RST     = '\033[00m'

    v = 0
    while True:
        print(GREEN)
        n = input("Insira a nota/moeda: R$ ")
        print(RST)
        try:
            n = round(float(n), 2)

            if n != 20.00 and n != 10.00 and n != 5.00 and n != 2.00 and n != 1.00 and n != 0.50:
                print(RED)
                print("Valor não reconhecido!")
                print(RST)
            else:
                v += n
                if v == valor:
                    precisaTroco = False
                    trocoValor = 0
                    n20, n10, n5, n2, m1, m50, aum20, aum10, aum5, aum2, aum1, aum50  = aumentarNotas(n, n20, n10, n5, n2, m1, m50)
                    return precisaTroco, v, n20, n10, n5, n2, m1, m50, trocoValor, aum20, aum10, aum5, aum2, aum1, aum50
                elif v > valor:
                    precisaTroco = True
                    trocoValor = v - valor
                    n20, n10, n5, n2, m1, m50, aum20, aum10, aum5, aum2, aum1, aum50 = aumentarNotas(n, n20, n10, n5, n2, m1, m50)
                    return precisaTroco, v, n20, n10, n5, n2, m1, m50, trocoValor, aum20, aum10, aum5, aum2, aum1, aum50
                else:
                    n20, n10, n5, n2, m1, m50, aum20, aum10, aum5, aum2, aum1, aum50 = aumentarNotas(n, n20, n10, n5, n2, m1, m50)
                    continue
        except:
            print(RED)
            print("Tipo inválido!")
            print(RST)

def troco(v, n20, n10, n5, n2, m1, m50, opcao, p1, p2, p3, p4, p5, aum20, aum10, aum5, aum2, aum1, aum50):
    """
    Função responsável por receber o valor do troco a ser retornado e imprimir
    na tela as notas que o compõe.

    Parâmetros:
        v: Valor do troco
        n20: Quantidade de notas de 20 reais
        n10: Quantidade de notas de 10 reais
        n5: Quantidade de notas de 5 reais
        n2: Quantidade de notas de 2 reais
        m1: Quantidade de moedas de 1 real
        m50: Quantidade de moedas de 50 centavos
        opcao: Número referente à opção escolhida
        p1: Quantidade do produto 1
        p2: Quantidade do produto 2
        p3: Quantidade do produto 3
        p4: Quantidade do produto 4
        p5: Quantidade do produto 5
        aum20: Váriavel contadora da respectiva nota
        aum10: Váriavel contadora da respectiva nota
        aum5: Váriavel contadora da respectiva nota
        aum2: Váriavel contadora da respectiva nota
        aum1: Váriavel contadora da respectiva moeda
        aum50: Váriavel contadora da respectiva moeda
    
    Retorno:
        n20: Quantidade de notas de 20 reais
        n10: Quantidade de notas de 10 reais
        n5: Quantidade de notas de 5 reais
        n2: Quantidade de notas de 2 reais
        m1: Quantidade de moedas de 1 real
        m50: Quantidade de moedas de 50 centavos
        p1: Quantidade do produto 1
        p2: Quantidade do produto 2
        p3: Quantidade do produto 3
        p4: Quantidade do produto 4
        p5: Quantidade do produto 5
    """
    GREEN   = '\033[32m'
    RST     = '\033[00m'

    vaux = v
    v20 = v10 = v5 = v2 = v1 = v50 = 0
    valido20 = valido10 = valido5 = valido2 = valido1 = valido50 = True

    # Verifica quais notas/moedas podem ser devolvidas no troco piorizando o maior valor 
    # possível e verifica a disponbilidade das notas/moedas no estoque
    while True: 
        if vaux - 20.00 >= 0.00 and valido20 == True:
            v20 += 1
            vaux -= 20.00
            if v20 > n20:
                v20 -= 1
                vaux += 20  
                valido20 = False      
        elif vaux - 10.00 >= 0.00 and valido10 == True:
            v10 += 1
            vaux -= 10.00
            if v10 > n10:
                v10 -= 1
                vaux += 10
                valido10 = False
        elif vaux - 5.00 >= 0.00 and valido5 == True:
            v5 += 1
            vaux -= 5.00
            if v5 > n5:
                v5 -= 1
                vaux += 5
                valido5 = False     
        elif vaux - 2.00 >= 0.00 and valido2 == True:
            v2 += 1
            vaux -= 2.00
            if v2 > n2:
                v2 -= 1
                vaux += 2
                valido2 = False           
        elif vaux - 1.00 >= 0.00 and valido1 == True:
            v1 += 1
            vaux -= 1.00
            if v1 > m1:
                v1 -= 1
                vaux += 1
                valido1 = False    
        elif vaux - 0.50 >= 0.00 and valido50 == True:
            v50 += 1
            vaux -= 0.50
            if v50 > m50:
                v50 -= 1
                vaux += 0.50
                valido50 = False
        elif vaux == 0.00:
            break
        elif valido20 == False or valido10 or False or valido5 or False or valido1 == False or valido50 == False:
            break
        else:
            continue
        
    if vaux == 0:
        print(GREEN)
        print("Receba seu troco:")
        print(RST)
        n20 = trocoAux1(20.00, v20, n20)
        n10 = trocoAux1(10.00, v10, n10)
        n5 = trocoAux1(5.00, v5, n5)
        n2 = trocoAux1(2.00, v2, n2)
        m1 = trocoAux1(1.00, v1, m1)
        m50 = trocoAux1(0.50, v50, m50)

        return n20, n10, n5, n2, m1, m50, p1, p2, p3, p4, p5
    else: 
        n20, n10, n5, n5, m1, m50, p1, p2, p3, p4, p5 = trocoAux2(v, vaux, v20, v10, v5, v2, v1, v50, n20, n10, n5, n2, m1, m50, opcao, p1, p2, p3, p4, p5, aum20, aum10, aum5, aum2, aum1, aum50) 
        
        return n20, n10, n5, n5, m1, m50, p1, p2, p3, p4, p5
                
def trocoAux1(a, a1, a2):
    """
    Função responsável por auxiliar a função 'troco' na impressão dos valores do troco.

    Parâmetros:
        a: Valor da nota;
        a1: Quantidade de notas do valor 'a' a serem dadas ao cliente como troco;
        a2: Quantidade de notas existentes no caixa.
    
    Retorno:
        a2: Quantidade de notas/moedas do valor 'a'
    """

    i = 1
    while i <= a1:
        print(f"R$ {a:.2f}")
        i += 1
        a2 -=1
    
    return a2
        
def trocoAux2 (v, vaux, v20, v10, v5, v2, v1, v50, n20, n10, n5, n2, m1, m50, opcao, p1, p2, p3, p4, p5, aum20, aum10, aum5, aum2, aum1, aum50):
    """
    Função responsável por verificar se o cliente gostaria de receber o produto mesmo não recebendo o troco total 
    devido e continuar ou cancelar a venda de acordo com a resposta do cliente.
    
    Parâmetros:
        v: Valor do troco total
        vaux: Valor do troco devido
        v20: Quantidade de notas de 20 a serem dadas ao cliente como troco
        v10: Quantidade de notas de 10 a serem dadas ao cliente como troco
        v5: Quantidade de notas de 5 a serem dadas ao cliente como troco
        v2: Quantidade de notas de 2 a serem dadas ao cliente como troco
        v1: Quantidade de moedas de 1 a serem dadas ao cliente como troco
        v50: Quantidade de moedas de 0.50 a serem dadas ao cliente como troco
        n20: Quantidade de notas de 20 reais
        n10: Quantidade de notas de 10 reais
        n5: Quantidade de notas de 5 reais
        n2: Quantidade de notas de 2 reais
        m1: Quantidade de moedas de 1 real
        m50: Quantidade de moedas de 50 centavos
        opcao: Número referente ao produto escolhido
        p1: Quantidade do produto 1
        p2: Quantidade do produto 2
        p3: Quantidade do produto 3
        p4: Quantidade do produto 4
        p5: Quantidade do produto 5
        aum20: Váriavel contadora da respectiva nota
        aum10: Váriavel contadora da respectiva nota
        aum5: Váriavel contadora da respectiva nota
        aum2: Váriavel contadora da respectiva nota
        aum1: Váriavel contadora da respectiva moeda
        aum50: Váriavel contadora da respectiva moeda
        
    Retorno
        n20: Quantidade de notas de 20 reais
        n10: Quantidade de notas de 10 reais
        n5: Quantidade de notas de 5 reais
        n2: Quantidade de notas de 2 reais
        m1: Quantidade de moedas de 1 real
        m50: Quantidade de moedas de 50 centavos
        p1: Quantidade do produto 1
        p2: Quantidade do produto 2
        p3: Quantidade do produto 3
        p4: Quantidade do produto 4
        p5: Quantidade do produto 5
    """
    VIOLET  = '\033[35m'
    YELLOW  = '\033[33m'
    GREEN   = '\033[32m'
    RED     = '\033[31m'
    CYAN    = '\033[36m'
    RST     = '\033[00m'
    
    divida = v - vaux
    print(RED)
    print("Não há troco suficiente!")
    print(RST)
    print(f"Temos apenas R$ {divida:.2f} para voltar de troco.")
    
    while True:
        print(YELLOW)
        x = input("Deseja continuar a compra? (S/N) ")
        print(RST)
        try:
            x = x.lower()
            if x == "s" or x == "sim":
                print(GREEN)
                print("Receba seu troco:")
                print(RST)
                n20 = trocoAux1(20.00, v20, n20)
                n10 = trocoAux1(10.00,v10, n10)
                n5 = trocoAux1(5.00,v5, n5)
                n2 = trocoAux1(2.00,v2, n2)
                m1 = trocoAux1(1.00,v1, m1)
                m50 = trocoAux1(0.50,v50, m50)
                print(VIOLET)
                print("Obrigada pela compra!")
                print(RST)

                return n20, n10, n5, n2, m1, m50, p1, p2, p3, p4, p5
            
            elif x == "n" or x == "nao":
                n20, n10, n5, n2, m1, m50, p1, p2, p3, p4, p5 = trocoAux3(n20, n10, n5, n2, m1, m50, opcao, p1, p2, p3, p4, p5, aum20, aum10, aum5, aum2, aum1, aum50)
                print(CYAN)
                print("Lamentamos pelo ocorrido. Volte sempre!")
                print(RST)

                return n20, n10, n5, n2, m1, m50, p1, p2, p3, p4, p5
            
            else:
                print(RED)
                print("Resposta inválida!")
                print(RST)

        except:
            print(RED)
            print("Resposta inválida!")
            print(RST)

def trocoAux3(n20, n10, n5, n2, m1, m50, opcao, p1, p2, p3, p4, p5, aum20, aum10, aum5, aum2, aum1, aum50):
    """
    Função responsável por auxiliar a função 'trocoAux2' no cancelamento da compra, assim realizando a devolução
    do produto ao estoque e do dinheiro recebido como pagamento anteriormente.

    Parâmetros:
        n20: Quantidade de notas de 20 reais
        n10: Quantidade de notas de 10 reais
        n5: Quantidade de notas de 5 reais
        n2: Quantidade de notas de 2 reais
        m1: Quantidade de moedas de 1 real
        m50: Quantidade de moedas de 50 centavos
        opcao: Número referente ao produto escolhido
        p1: Quantidade do produto 1
        p2: Quantidade do produto 2
        p3: Quantidade do produto 3
        p4: Quantidade do produto 4
        p5: Quantidade do produto 5
        aum20: Váriavel contadora da respectiva nota
        aum10: Váriavel contadora da respectiva nota
        aum5: Váriavel contadora da respectiva nota
        aum2: Váriavel contadora da respectiva nota
        aum1: Váriavel contadora da respectiva moeda
        aum50: Váriavel contadora da respectiva moeda

    Retorno:
        n20: Quantidade de notas de 20 reais
        n10: Quantidade de notas de 10 reais
        n5: Quantidade de notas de 5 reais
        n2: Quantidade de notas de 2 reais
        m1: Quantidade de moedas de 1 real
        m50: Quantidade de moedas de 50 centavos
        p1: Quantidade do produto 1
        p2: Quantidade do produto 2
        p3: Quantidade do produto 3
        p4: Quantidade do produto 4
        p5: Quantidade do produto 5        
    """
    GREEN   = '\033[32m'
    RST     = '\033[00m'

    p1 += 1 if opcao == 1 else 0
    p2 += 1 if opcao == 2 else 0
    p3 += 1 if opcao == 3 else 0
    p4 += 1 if opcao == 4 else 0
    p5 += 1 if opcao == 5 else 0

    print(GREEN)
    print("Receba seu dinheiro de volta:")
    print(RST)

    # Se aum(x) for diferente de 0, significa que a respectiva nota/moeda foi recebida como pagamento
    # anteriormente, ou seja, adicionada ao estoque de notas/moedas. O bloco a seguir realiza a retida
    # desses valores do estoque.
    if aum20 != 0:
        n20 = diminuirrNotas(20.00, aum20, n20)
    if aum10 != 0:
        n10 = diminuirrNotas(10.00, aum10, n10)
    if aum5 != 0:
        n5 = diminuirrNotas(5.00, aum5, n5)
    if aum2 != 0:
        n2 = diminuirrNotas(2.00, aum2, n2)
    if aum1 != 0:
        m1 = diminuirrNotas(1.00, aum1, m1)
    if aum50 != 0:
        m50 = diminuirrNotas(0.50, aum50, m50)

    return n20, n10, n5, n2, m1, m50, p1, p2, p3, p4, p5

def aumentarNotas(v, n20, n10, n5, n2, m1, m50):
    """
    Função responsável por aumentar a quantidade das notas inseridas na máquina.
    Parâmetros:
        v: Valor inserido
        n20: Quantidade de notas de 20 reais;
        n10: Quantidade de notas de 10 reais;
        n5: Quantidade de notas de 5 reais;
        n2: Quantidade de notas de 2 reais;
        m1: Quantidade de moedas de 1 real;
        m50: Quantidade de moedas de 50 centavos.
    
    Retorno:
        n20: Quantidade de notas de 20 reais;
        n10: Quantidade de notas de 10 reais;
        n5: Quantidade de notas de 5 reais;
        n2: Quantidade de notas de 2 reais;
        m1: Quantidade de moedas de 1 real;
        m50: Quantidade de moedas de 50 centavos;
        aum20: Váriavel contadora da nota referente;
        aum10: Váriavel contadora da nota referente;
        aum5: Váriavel contadora da nota referente;
        aum2: Váriavel contadora da nota referente;
        aum1: Váriavel contadora da nota referente;
        aum50: Váriavel contadora da nota referente.
    """
    aum20 = aum10 = aum5 = aum2 = aum1 = aum50 = 0
    if v == 20.00:
        n20 += 1
        aum20 += 1
    elif v == 10.00:
        n10 += 1
        aum10 += 1
    elif v == 5.00:
        n5 += 1
        aum5 += 5
    elif v == 2.00:
        n2 += 1
        aum2 += 1
    elif v == 1.00:
        m1 += 1
        aum1 += 1
    else:
        m50 += 1
        aum50 += 1

    return n20, n10, n5, n2, m1, m50, aum20, aum10, aum5, aum2, aum1, aum50

def diminuirrNotas(v, aum, n):
    """
    Função responsável por diminuir a quantidade das notas/moedas existentes no estoque.

    Parâmetros:
        v: Valor da nota/moeda
        aum: Variável contadora da respectiva nota/moeda
        n: Quantidade da nota/moeda
    Retorno:
        n: Quantidade da nota/moeda
    """

    i = 0
    while i < aum:
        print(f"R$ {v}")
        n -= 1
        i += 1

    return n

def infoInterna(p1, p2, p3, p4, p5, n20, n10, n5, n2, m1, m50, estoqueInicial):
    """
    Função responsável por imprimir o estoque de produtos e de notas/moedas da máquina.

    Parâmetros:
        p1: Quantidade do produto 1
        p2: Quantidade do produto 2
        p3: Quantidade do produto 3
        p4: Quantidade do produto 4
        p5: Quantidade do produto 5
        n20: Quantidade de notas de 20 reais
        n10: Quantidade de notas de 10 reais
        n5: Quantidade de notas de 5 reais
        n2: Quantidade de notas de 2 reais
        m1: Quantidade de moedas de 1 real
        m50: Quantidade de moedas de 50 centavos
        estoqueInicial: Quantidade inicial

    """
    VIOLET  = '\033[35m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    RST     = '\033[00m'

    print(VIOLET)
    print("v----ESTOQUE DE PRODUTOS----v")
    print(RST)
    print(f"Lámen Ichiraku: {p1} un.")
    print(f"Mitarashi: {p2} un.")
    print(f"Curry Rock Lee: {p3} un.")
    print(f"Onigri Uchiha: {p4} un..")
    print(f"Pílulas Sakura: {p5} un.")
    print(VIOLET)
    print("v----ESTOQUE DE NOTAS/MOEDAS----v")
    print(RST)
    print(f"Notas de R$ 20.00: {n20}")
    print(f"Notas de R$ 10.00: {n10}")
    print(f"Notas de R$ 5.00: {n5}")
    print(f"Notas de R$ 2.00: {n2}")
    print(f"Moedas de R$ 1.00: {m1}")
    print(f"Moedas de R$ 0.50: {m50}")
    print(GREEN)
    print(f"Faturamento: R${estoqueInicial*(15 + 10 + 25 + 6 + 5) - (p1*15 + p2*10 + p3*25 + p4*6 + p5*5):.2f}")
    print(YELLOW)
    input(">> Aperte Enter para voltar ao Menu Inicial <<")
    print(RST)
    
def produtos(p, p1, p2, p3, p4, p5):
    """
    Função responsável por definir em variaveis o valor e o nome do produto escolhido.

    Parâmetros:
        p: Número do produto escolhido
        p1: Quantidade do produto 1
        p2: Quantidade do produto 2
        p3: Quantidade do produto 3
        p4: Quantidade do produto 4
        p5: Quantidade do produto 5
    
    Retorno:
        valor = Valor do produto selecionado
        nome = Nome do produto selecionado
        p1: Quantidade do produto 1
        p2: Quantidade do produto 2
        p3: Quantidade do produto 3
        p4: Quantidade do produto 4
        p5: Quantidade do produto 5
    """
    pSemEstoque = False
    if p == 1:
        valor = 15
        nome = "Lámen Ichiraku"
        if p1 != 0:
            p1 -= 1
        else: 
            pSemEstoque = True
    elif p == 2:
        valor = 10
        nome = "Mitarashi"
        if p2 != 0:
            p2 -= 1
        else: 
            pSemEstoque = True
    elif p == 3:
        valor = 25
        nome = "Curry Rock Lee"
        if p3 != 0:
            p3 -= 1
        else: 
            pSemEstoque = True
    elif p == 4:
        valor = 6
        nome = "Onigri Uchiha"
        if p4 != 0:
            p4 -= 1
        else: 
            pSemEstoque = True
    elif p == 5:
        valor = 5
        nome = "Pílulas Sakura"
        if p5 != 0:
            p5 -= 1
        else: 
            pSemEstoque = True
        

    return valor, nome, p1, p2, p3, p4, p5, pSemEstoque

def main():
    """
    Função responsável por chamar outras funcões para a execução correta do programa.
    """
    VIOLET  = '\033[35m'
    RED     = '\033[31m'
    CYAN    = '\033[36m'
    YELLOW  = '\033[33m'
    RST     = '\033[00m'

    print(RST)
    limpaTela()
    estoqueInicial = 5
    p1 = p2 = p3 = p4 = p5 = n20 = n10 = n5 = n2 = m1 = m50 = estoqueInicial
    bemVindo()
    i = 1
    while True:
        print(RST)
        aum20 = aum10 = aum5 = aum2 = aum1 = aum50 = 0
        menuInicial(p1, p2, p3, p4, p5)
        opcao = opcaoEscolha()
        if opcao >= 1 and opcao <=5:
            valorProd, nomeProd, p1, p2, p3, p4, p5, pSemEstoque = produtos(opcao, p1, p2, p3, p4, p5)

            if pSemEstoque == False:
                print(f"Você escolheu {nomeProd}")
                print(f"Preço: R$ {valorProd:.2f}")

                precisaTroco, valorPago, n20, n10, n5, n2, m1, m50, trocoValor, aum20, aum10, aum5, aum2, aum1, aum50 = pagamento(valorProd, n20, n10, n5, n2, m1, m50)

                print(f"Valor pago: R$ {valorPago:.2f}")
                print(f"Troco: R$ {trocoValor:.2f}")
                print()

                if precisaTroco == True:
                    n20, n10, n5, n2, m1, m50, p1, p2, p3, p4, p5 = troco(trocoValor, n20, n10, n5, n2, m1, m50, opcao, p1, p2, p3, p4, p5, aum20, aum10, aum5, aum2, aum1, aum50)
                    print(YELLOW)
                    input(">> Aperte Enter para continuar... <<")
                    print(RST)
                    iteracao(i)
                    i += 1
                else:
                    print(VIOLET)
                    print("Obrigada pela compra!")
                    print(YELLOW)
                    input(">> Aperte Enter para continuar.. <<")
                    print(RST)
                    iteracao(i)
            else:
                print(RED)
                print(f"Desculpe, mas {nomeProd} está indisponível no momento!")
                print(YELLOW)
                input(">> Aperte Enter para continuar... <<")
                print(RST)
                limpaTela()
                
                i += 1
        elif opcao == 6:
            infoInterna(p1, p2, p3, p4, p5, n20, n10, n5, n2, m1, m50, estoqueInicial)
        else:
            print(CYAN)
            print("Obrigada pela preferência!")
            print("Volte sempre! :D")
            print(RST)
            exit()

main()