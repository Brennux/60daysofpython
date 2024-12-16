def tabuada():
    """
    essa funcao recebe um numero e retorna a tabuada desse numero
    """
    
    try:
        numero = int(input("Digite um numero: "))
        print(f"\nTabuada de {numero}:")
        #gera a tabuada de 1 a 10
        for i in range(1,11):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")
            
    except ValueError:
        print("entrada invalida. digite um numero.")
if __name__ == "__main__":
    tabuada()