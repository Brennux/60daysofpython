def eh_palidromo(texto):
    """
    verificar se um numero, texto ou palavra eh um palidrmo 
    :param texto: palavra, texto ou numero
    :return: uma mensagem indicando se eh um palidromo ou não 
    
    """
    texto = str(texto).replace(" ","").lower()
    
    if texto == texto[::-1]:
        return f"{texto} eh um palidromo"
    return f"{texto} não eh um palidromo"

print(eh_palidromo("breno"))