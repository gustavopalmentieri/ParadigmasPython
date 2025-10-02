valores= []

qtd_valores = 5

for i in range(qtd_valores): 

    valor = int(input(("Digite 5 números: ")))
    valores.append(valor)

for numero in valores:
    if numero > 50:
        print (numero)