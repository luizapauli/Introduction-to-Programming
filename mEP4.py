######################################################
# Introdução a Programação (2023/2)
# miniEP4 - Simulador do Jogo da Velha
# Nome: Luiza Pauli de Castro
# Matrícula: ----------
######################################################

######################################################
# LEMBRE-SE:
# - Neste miniEP, você não pode usar variáveis globais
#   nem funções recursivas;
# - Você deve seguir o código base disponibilizado, 
#   não sendo permitido a alteração do nome e/ou
#   lista de parâmetros das funções dadas;
# - Caso precise, você *PODE* criar outras funções;
# - Não é permitido a utilização de lista, tuplas 
#   ou qualquer outro tipo estruturado para 
#   “facilitar” a manipulação dos dados. Você deve 
#   sempre trabalhar com as 9 variáveis que 
#   representam as posições no tabuleiro;
#
# Dica: Leia o docstring de cada função para saber o
#       que cada uma deve fazer e retornar.
######################################################

def imprimeTabuleiro(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e imprime o tabuleiro
    """

    print(f" {p7} | {p8} | {p9} ")
    print("---+---+---")
    print(f" {p4} | {p5} | {p6} ")
    print("---+---+---")
    print(f" {p1} | {p2} | {p3} ")




def entradaValida(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e
    verifica se os valores são válidos, ou seja, retorna True
    se cada variável possui " " ou "x" ou "o" e False, caso contrário.
    """

    if p1 != "x" and p1 != "o" and p1 != " ":
        entradaVal = False
    elif p2 != "x" and p2 != "o" and p2 != " ":
        entradaVal = False
    elif p3 != "x" and p3 != "o" and p3 != " ":
        entradaVal = False
    elif p4 != "x" and p4 != "o" and p4 != " ":
        entradaVal = False
    elif p5 != "x" and p5 != "o" and p5 != " ":
        entradaVal = False
    elif p6 != "x" and p6 != "o" and p6 != " ":
        entradaVal = False
    elif p7 != "x" and p7 != "o" and p7 != " ":
        entradaVal = False
    elif p8 != "x" and p8 != "o" and p8 != " ":
        entradaVal = False
    elif p9 != "x" and p9 != "o" and p9 != " ":
        entradaVal = False
    else:
        entradaVal = True

    return entradaVal

def jogadaValida(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e
    verifica se os valores formam uma jogada válida.
    Retorna True se a jogada for válida e False, caso contrário
    """
    jogadaVal = True
    bola, xis = quantidadeJogadas(p1, p2, p3, p4, p5, p6, p7, p8, p9)

    if bola > xis + 1 or xis > bola + 1:
        jogadaVal = False
    
    return jogadaVal

        

def verificaJogada(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e
    imprime se um jogador ("x" ou "o") venceu a jogada. 
    """
    #Complete o código da função

    bola, xis = quantidadeJogadas(p1, p2, p3, p4, p5, p6, p7, p8, p9)
    
    if p1 == p2 == p3 and p1 != " ":
        print(f"O jogador '{p1}' venceu!")
    elif p1 == p4 == p7 and p1 != " ":
        print(f"O jogador '{p1}' venceu!")
    elif p1 == p5 == p9 and p1 != " ":
        print(f"O jogador '{p1}' venceu!")
    elif p9 == p6 == p3 and p9 != " ":
        print(f"O jogador '{p9}' venceu!")
    elif p9 == p8 == p7 and p9 != " ":
        print(f"O jogador '{p9}' venceu!")
    elif p5 == p7 == p3 and p5 != " ":
        print(f"O jogador '{p5}' venceu!")
    elif p5 == p4 == p6 and p5 != " ":
        print(f"O jogador '{p5}' venceu!")
    elif p5 == p8 == p2 and p5 != " ":
        print(f"O jogador '{p5}' venceu!")
    elif bola + xis == 9:
        print("Empate!")
    else:
        print("O jogo nao terminou!")
    


def leEntrada():
    """
    Função responsável pela leitura dos dados do tabuleiro. 
    A função deve retornar 9 valores, indicando o simbolo de cada
    posição no tabuleiro de um Jogo da Velha.
    """
    jogadasRealizadas = int(input())
    i = 0
    t1 = t2 = t3  = t4 = t5 = t6 = t7 = t8 = t9 = " "
    while i < jogadasRealizadas:
        posicao, simbolo = input().split()
        if int(posicao) == 1:
            t1 = simbolo
        elif int(posicao) == 2:
            t2 = simbolo
        elif int(posicao) == 3:
            t3 = simbolo
        elif int(posicao) == 4:
            t4 = simbolo
        elif int(posicao) == 5:
            t5 = simbolo
        elif int(posicao) == 6:
            t6 = simbolo
        elif int(posicao) == 7:
            t7 = simbolo
        elif int(posicao) == 8:
            t8 = simbolo
        else:
            t9 = simbolo
        i +=1
    return t1, t2, t3, t4, t5, t6, t7, t8, t9

def quantidadeJogadas(q1, q2, q3, q4, q5, q6, q7, q8, q9):
    xis = 0
    bola = 0
    if q1 == "x":
        xis +=1
    elif q1 == "o":
         bola += 1

    if q2 == "x":
        xis +=1
    elif q2 == "o":
        bola += 1

    if q3 == "x":
        xis +=1
    elif q3 == "o":
        bola += 1

    if q4 == "x":
        xis +=1
    elif q4 == "o":
        bola += 1

    if q5 == "x":
        xis +=1
    elif q5 == "o":
        bola += 1

    if q6 == "x":
        xis +=1
    elif q6 == "o":
        bola += 1

    if q7 == "x":
        xis +=1
    elif q7 == "o":
        bola += 1

    if q8 == "x":
        xis +=1
    elif q8 == "o":
        bola += 1

    if q9 == "x":
        xis +=1
    elif q9 == "o":
        bola += 1

    return bola, xis
######################################################
## NÃO ALTERE A FUNÇÃO 'main'                       ##
######################################################
def main():
    t1, t2, t3, t4, t5, t6, t7, t8, t9 = leEntrada()
    imprimeTabuleiro(t1, t2, t3, t4, t5, t6, t7, t8, t9)
    if entradaValida(t1, t2, t3, t4, t5, t6, t7, t8, t9) == False:
        print("Entrada invalida!")
    elif jogadaValida(t1, t2, t3, t4, t5, t6, t7, t8, t9) == False:
        print("Jogada invalida!")
    else:
        verificaJogada(t1, t2, t3, t4, t5, t6, t7, t8, t9)

main()
