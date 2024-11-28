def pode_dirigir (idade):
    if idade >= 18:
        return True
    else:
        return False
    
print(pode_dirigir(19))

try:
    input_user = int(input("Digite sua idade:"))
    print(pode_dirigir(input_user))
except ValueError:
    print("entrada invalida. por favor, digite um numero inteiro.")