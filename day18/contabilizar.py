def contar_palavras(texto):
    """
    contar palavras em uma string
    :param texto: string de entrada
    :return: numero de palavras
    """
    palavras  = texto.split()#vai separar as palavras usando o espaço do texto entre as palavras
    
    return len(palavras)

print(contar_palavras("ola breno"))