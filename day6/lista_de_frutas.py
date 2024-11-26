#listas de frutas
#frutas = ["uva", "maça", "mamão", "banana"]

#or frutas in frutas:
  #  print(frutas)
  
frutas = []
while True:
    fruta = input("Digite o nome da fruta:") 
    if fruta == "sair":
        break
    frutas.append(fruta)
    
print(frutas)