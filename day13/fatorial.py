# o que eh um fatorial
#fatorial eh um calculo em matematica onde multiplicamos os valores a partir do numero passado
#5! = 5 x 4 x 3 x 2 x 1 = 120
def fatorial(n):
    """
    calcula o fatorial de um numero usando recursão.
    
    :param n: numero inteiro não negativo.
    :return: fatorial de n.
    """
    if n < 0:
        raise ValueError("o numero deve ser positivo")
    
    #entao essa condicional retorna 1 se caso o numero da funcao for 0 ou 1
    if n == 0 or n == 1:
        return 1
    
    # recursividade
    return n * fatorial(n-1)
print(fatorial(-2))