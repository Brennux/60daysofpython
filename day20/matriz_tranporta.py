def transpor_matriz(matriz):
    """
    gerar uma matriz trnsposta de 3x3
    substitui colunas horizontais por verticais
    
    [1,2,3]
    [1,2,3]
    [1,2,3]
    
    [1,1,1]
    [2,2,2]
    [3,3,3]
    
    arg: matrix que vao listas de 3 numeros na horizontal e vertical
    return: matriz transposta
    raises: valueError: se a matriz nao ter 3x3
    """
    
    #verificador se a matriz eh 3x3
    if len(matriz) != 3 or not all(len(linha) == 3 for linha in matriz):
        raise ValueError("A matriz nao possui o tamanho 3x3")
    # gerar a matriz transposta
    
    transposta = [[matriz [j] [i] for j in range(3) for i in range(3)]]
    
    return transposta

    #explicação da nossa matriz transposta utilizando iteradores e listas 
matriz = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    
transposta = []
    
for i in range(3):
    #iniciando uma nova linha
    nova_linha = []
        
    for j in range(3):
            #adiciona o elemento corresponde a matriz original
            nova_linha.append(matriz[j][i])
            
    #print(nova_linha)
    transposta.append(nova_linha)
    
for linha in transpor_matriz(matriz):
    print(linha)
