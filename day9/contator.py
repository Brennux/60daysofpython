#um contador que para quando atingir  um valor definido pelo o usuario
def contador_personalizado():
    try:
        limite = int(input("Digite o valor maximo de um contador: "))
        #função range crua uma lista de numnero a partir do 0 
        #até o valor definido pelo usuario
        limite = limite + 1 
        for i in range(limite):
            print(i)
            if i == limite:
                print("contador atingiu o limite")
                break
    except ValueError:
        print("mensagem iválida! Porfavor digite um numero inteiro..")
        
contador_personalizado()