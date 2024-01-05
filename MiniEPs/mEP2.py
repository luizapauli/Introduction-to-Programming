flag = True

peso = float(input())
idade = int(input())

if idade >= 16 and idade < 18:
    doc_autorizacao = input()
  
saude = input()
drogas = input()
_1doacao = input()

if _1doacao == "N" or _1doacao == "n":
    ultimadoacao = int(input())
    doacao_ano = int(input())

sexo = input()

if sexo == "F" or sexo == "f":
    gravidez = input()
    amamentando = input()
    if amamentando == "S" or amamentando == "s":
        idadebebe = int(input())

print(f"Peso: {peso}")
print(f"Idade: {idade}")

if idade >= 16 and idade < 18:
    print(f"Documento de autorizacao: {doc_autorizacao}")

print(f"Boa saude: {saude}")
print(f"Uso de drogas injetaveis: {drogas}")
print(f"Primeira doacao: {_1doacao}")

if _1doacao == "N" or _1doacao == "n":
    print(f"Meses desde ultima doacao: {ultimadoacao}")
    print(f"Doacoes nos ultimos 12 meses: {doacao_ano}")

print(f"Sexo biologico: {sexo}")

if sexo == "F" or sexo == "f":
    print(f"Gravidez: {gravidez}")
    print(f"Amamentando: {amamentando}")
    if amamentando == "S" or amamentando == "s":
        print(f"Meses bebe: {idadebebe}")

if peso < 50:
    print("Impedimento: abaixo do peso minimo.")
    flag = False  
if idade < 16:
    print("Impedimento: menor de 16 anos.")
    flag = False
elif idade < 18 and (doc_autorizacao == "N" or doc_autorizacao == "n"):
    print("Impedimento: menor de 18 anos, sem consentimento dos responsaveis.")
    flag = False
elif idade > 60 and idade <= 69 and (_1doacao == "S" or _1doacao == "s"):
    print("Impedimento: maior de 60 anos, primeira doacao.")
    flag = False
elif idade > 69:
    print("Impedimento: maior de 69 anos.")
    flag = False

if saude == "N" or saude == "n":
    print("Impedimento: nao esta em boa saude.")
    flag = False
if drogas == "S" or drogas == "s":
    print("Impedimento: uso de drogas injetaveis.")
    flag = False
  
if (sexo == "M" or sexo == "m") and (_1doacao == "N" or _1doacao == "n"):
    if ultimadoacao < 2:
        print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
        flag = False
    if doacao_ano >=4:
        print("Impedimento: numero maximo de doacoes anuais foi atingido.")
        flag = False
elif sexo == "F" or sexo =="f":
    if _1doacao == "N" or _1doacao == "n":
        if ultimadoacao < 3:
            print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
            flag = False
        if doacao_ano >=3:
            print("Impedimento: numero maximo de doacoes anuais foi atingido.")
            flag = False
    if gravidez == "S" or gravidez == "s":
        print("Impedimento: gravidez.")
        flag = False
    if (amamentando == "S" or amamentando == "s") and idadebebe <= 12:
        print("Impedimento: amamentacao.")
        flag = False

if flag is True:
  print("Procure um hemocentro.")