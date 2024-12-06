fibonacci = [0, 1] # a sequencia sempre comeca por 0 e 1 
print(fibonacci[-1] + fibonacci[-2])

for i in range(8):
    proximo_numero = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proximo_numero)
print(fibonacci)