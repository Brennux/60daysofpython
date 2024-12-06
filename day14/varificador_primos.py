numero = int(input("Digite o numero para verificar se ele eh primo:"))

#assumimos como true primeriramento uma variavel eh_primo
eh_primo = True
if numero <= 1:
    eh_primo = False
    
for i in range(2, int(numero ** 0.5) + 1):
    if numero % i == 0:
        eh_primo = False
        break # saimos do loop, pois já encontramos um divisor 
    
if eh_primo:
    print(f"{numero} eh um numero primo")
else:
    print(f"{numero} nao eh um numero primo")