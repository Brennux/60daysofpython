import random

def lancar_dado():
    """
    simular  olançamento de um dado de 1 a 6 
    
    return:
     int: um numero aleatorio de 1 a 6 
    """
    
    return random.randint(1,6)

if __name__ == "__main__":
    print(f"O resultado do dado foi: {lancar_dado()}")