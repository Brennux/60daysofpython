import time

def cronometro_de_10seg():
    """
    Realiza um cronometro de 10 segundos
    """
    
    print("Cronometro de 10 segundos")
    
    tempo = 10
    
    while tempo > 0:
        print(f"Tempo Restante: {tempo} segundos", end="\r", flush=True)
        time.sleep(1)
        tempo -= 1
        
    print("\nCronometro Finalizado")
    
if __name__ == "__main__":
    cronometro_de_10seg()