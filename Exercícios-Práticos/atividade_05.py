valores = []

while True:

    saques = float(input("Digite o valor que deseja sacar: "))

    if saques == 0:
        break

    valores.append(saques)


print("Total Sacado: ", sum(valores))
    
    