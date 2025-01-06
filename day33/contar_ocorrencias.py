from collections import Counter

def contar_ocorrencia(lista):
    """
    contas as ocorrencias de cada elemento em uma list
    arg:
        lista(list): a lista de elemento a ser analisada
        return:
            counter: um objeto do tipo int
    """
    
    contagem = Counter(lista)
    
    for elemento, quantidade in contagem.items():
        
        print(f"{elemento}: {quantidade}")
    return "Contagem realizada com sucesso"

if __name__ == "__main__":
    lista_exemplo = ['banana','uva','uva','maça','maça','laranaja','pera']
    
    print(contar_ocorrencia(lista_exemplo)) 