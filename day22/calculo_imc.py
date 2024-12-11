def calcular_imc():
    
    try:
        peso = float(input("Digite seu peso em kilogramas: "))
        
        altura = float(input("Digite sua altura em metros: "))
        
        if peso < 0 or altura < 0:
            print("O peso e altura dever ser maior que 0")
            return #encerrar a funcao
        
        imc = round(peso / (altura ** 2), 2)
        
        if imc <18.5:
            print("voce esta abaixo do peso!")
        elif 18.5 <= imc < 24.9:
            print("voce esta no peso normal!")
        elif 25 <= imc < 29.9:
            print("voce esta sobre peso!")
        else:
            print("Voce esta com obesidade!")
    except ValueError:
        print("entra esta invalida")
        
        def helloword():
            print('ola mundo')
            
    #siginifica que estamos rodando esse codigo internamente
    #apenas roda se eu rodar o meu script calcular imc
if __name__ == "__main__":
    calcular_imc()