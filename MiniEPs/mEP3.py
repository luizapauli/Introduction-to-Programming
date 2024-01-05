neutro = 0
agua = 0
fogo = 0
ar = 0
terra = 0

while True:
    elemento = input()
    if elemento != "FIM":
        neutro = int(input())
        if elemento == "AGUA":
            agua = agua + neutro
            if fogo !=0:
                fogo = fogo - (neutro/2)
                if fogo < 0:
                    fogo = 0
        elif elemento == "FOGO":
            fogo = fogo + neutro
            if agua !=0:
                agua = agua - (neutro/2)
                if agua < 0:
                    agua = 0
        elif elemento == "AR":
            ar = ar + neutro
            if terra !=0:
                terra = terra - (neutro/2)
                if terra < 0:
                    terra = 0
        elif elemento == "TERRA":
            terra = terra + neutro
            if ar !=0:
                ar = ar - (neutro/2)
                if ar < 0:
                    ar = 0
        else:
            continue
    else:
        break

print("Pontuacao Final")
print(f"Agua: {agua:.1f}")
print(f"Terra: {terra:.1f}")
print(f"Fogo: {fogo:.1f}")
print(f"Ar: {ar:.1f}")

if agua > 0 and fogo > 0 and ar > 0 and terra > 0:
    print("Treinamento realizado com sucesso.")
else:
    print("Realize mais treinamentos.")