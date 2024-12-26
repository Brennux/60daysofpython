def celsius_para_fahrenheit(celsius):
    """
    converte a temperatura de celsius para fahrenheit
    
    arg:
    celsius (float): A temperatura em celsius
    
    returns:
    float: A temperatura em fahrenheit
    """
    return round((celsius * 9/5) + 32, 2)

def fahrenheit_para_celsius(fahrenheit):
    """
     converte a temperatura de fahrenheit para celsius
    
    arg:
    fahrenheit (float): A temperatura em fahrenheit
    
    returns:
    float: A temperatura em celsius
    """
    return round((fahrenheit - 32) * 5/9, 2)

def main(temperatura, tipo_conversao):
    """
    funcao principal que recebe a temperatura e o tipo de conversao e retorna
    
    args:
    temperatura (float): A temperatura a ser convertida
    tipo_conversao (str): o tipo de conversao a ser realizada
    
    returns:
    float: A temperatura convertida
    """
    if tipo_conversao == "celsius":
        print(celsius_para_fahrenheit(temperatura))
    elif tipo_conversao == "fahrenheit":
        print(fahrenheit_para_celsius(temperatura))
    else:
        return print("tipo de conversao invalido")
    
if __name__ == "__main__":
    main(20, "celsius")
    main(20, "fahrenheit")