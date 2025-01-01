import time

def cronometro(tempo):
    """
    funcao que cria um conometro, que conta ate o tempo especificado
    """
    
    print("Iniciando cronometro...")
    
    for segundo in range(tempo + 1):
        print(f'tempo: {segundo} segundos', end="\r")
        time.sleep(1)
        
    print("\nCronometro FInalizado")
        
if __name__ == "__main__":
    tempo = 10
    cronometro(tempo)