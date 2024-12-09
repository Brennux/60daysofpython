def media_notas(calculo):
    """
    calculando media de notas a partir de uma lista de notas
    
    arg:
    notas (lista)
    
    return:
    float da media das notas 
    """
    
    media = sum(calculo) / len(calculo)
    #round arredonda a nossa media para duas casas decimais
    return round(media, 2)
print(media_notas([10,5,8]))