numero = input("Coloque o numero ")

try: #tente rodar
    numero = int(numero)
    if numero % 2 == 0:
        print("numero par")
    else:
        print("numnero impar")
except ValueError:
    print("voce não passou um numero inteiro!")