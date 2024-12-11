def convewrsor_moeda(valor, taxa_cambio, tipo_conversao):
    """
    essa funcao converte dolar em reais e visse e versa
    
    args:
    valor: (float): valor a ser convertido (monetario)
    taxa_cambio: A taxa de cambio atual
    tipo_conversao: dolar para real e real para dolar
    
    return 
       float: o valor convetido, arredondado para 2 casas decimais
       
    raises:
        ValueError: se o tipo de conversao for errado    
     """
    if tipo_conversao == 'dolar_real':
        return round(valor * taxa_cambio, 2)
    elif tipo_conversao =='real dolar':
        return round(valor / taxa_cambio, 2)
    else:
        return ValueError("tipo de conversao invalida")
    
print(convewrsor_moeda(12,6.10, 'real dolar'))
    
         