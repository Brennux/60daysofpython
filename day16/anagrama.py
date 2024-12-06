def anagrama(palavra1, palavra2):
    """
    verificar se duas palavras sao um anagrama ou nao 
    :param palavra1: primeria palavra
    :param palavra2: segunda palavra 
    return true se a plavra forem um anagrama
    """
    
    # Removendo espaços e convertendo para letras minusculas
    palavra1 = palavra1.replace(" ", "").lower()
    palavra2 = palavra2.replace(" ", "").lower()
    
    if sorted(palavra1) == sorted(palavra2):
        return f"essas palavras sao anagramas"
    return f"essas palavras nao sao anagramas"

print(anagrama("roma", "uva"))