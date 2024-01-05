lado1 = int(input())
lado2 = int(input())
lado3 = int(input())

if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    print("Valores invalidos.")
elif lado1 >= lado2 + lado3 or lado2 >= lado1 + lado3 or lado3 >= lado1 + lado2:
    print("Valores nao podem formar um triangulo.")
else:
    if lado1 == lado2 == lado3:
        print("Triangulo equilatero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 ==lado3:
        print("Triangulo isosceles.")
    else:
        print("Triangulo escaleno.")
    
    if lado1 > lado2 and lado1 > lado3:
        if lado1**2 < lado2**2 + lado3**2:
            print("Triangulo acutangulo.")
        elif lado1**2 == lado2**2 + lado3**2:
            print("Triangulo retangulo.")
        else:
            print("Triangulo obtusangulo.")
    elif lado2 > lado1 and lado2 > lado3:
        if lado2**2 < lado1**2 + lado3**2:
            print("Triangulo acutangulo.")
        elif lado2**2 == lado1**2 + lado3**2:
            print("Triangulo retangulo.")
        else:
            print("Triangulo obtusangulo.")
    else:
        if lado3**2 < lado1**2 + lado2**2:
            print("Triangulo acutangulo.")
        elif lado3**2 == lado1**2 + lado2**2:
            print("Triangulo retangulo.")
        else:
            print("Triangulo obtusangulo.")