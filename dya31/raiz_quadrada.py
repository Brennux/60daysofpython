import math

def raiz_quadrada(numero):
    """
    
    """
    if numero < 0:
        raise ValueError("Não foi possivel calcular, coloque numeros positivos")
    
    return round(math.sqrt(numero), 2)

if __name__ == "__main__":
    print(raiz_quadrada(4))