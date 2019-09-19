dic = {1:8.5, 2:3.25, 3:4.60}

lista = []

print("Escolha o seu produto:")
print("1 - Banana\n 2- Pera\n3 - Melancia ")

lista.append(1) # [1]
lista.append(2) # [1, 2]
lista.append(3) # [1, 2, 3]

for elemento in lista:
    total += dic[elemento] 

print(dic[1]) # 8.5




