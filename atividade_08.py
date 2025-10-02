dic1 = {"nome" : "Vídeo Game",
        "preço" : "2700"}

dic2 = {"nome" : "Computador",
        "preço" : "4500"}

dic3 = {"nome" : "Geladeira",
        "preço" : "1800"}

produtos = []

produtos.append(dic1)
produtos.append(dic2)
produtos.append(dic3)

nome = input("Digite o nome do produto:")

for produto in produtos:
    if produto["nome"] == nome:
        print("Esse é o valor do produto:", produto["preço"]) #FALTA TERMINAR!!!!!!!!!!!!!!!!!!!!!!!!