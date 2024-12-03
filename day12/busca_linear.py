def buscar_linear(lista, numero_procurado):
    """
    procurar um numero dentro de uma lista utilizando a busca linear

    :param lista: LISTA DE NUMEROS
    :PARAM numero_procurado: o numero que procurar
    """
    for i, numero in enumerate(lista):#funcao nativa do python enumerate
    #enumerate passa por cada item dentro de uma lista enquanto contabiliza
        if numero == numero_procurado:
            return i
    return -1

lista = [10,2,4,7,6,23,56,48]
numero_prcurado = 10

buscando_numero = buscar_linear(lista, numero_prcurado)
print(buscando_numero)

if buscando_numero != -1:
    print(f"o numero encontradono indice: {buscando_numero}")
else:
    print("numero não encontrado")
