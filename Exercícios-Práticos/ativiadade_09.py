dicionarios = []

dic1 = {
    "nome" : input("Digite seu nome: "),
    "idade" : int(input("Digite sua idade: "))
}

dic2= {
    "nome" : input("Digite seu nome: "),
    "idade" : int(input("Digite sua idade: "))
}

dic3= {
    "nome" : input("Digite seu nome: "),
    "idade" : int(input("Digite sua idade: "))
}

dicionarios.append(dic1)
dicionarios.append(dic2)
dicionarios.append(dic3)

for pessoa in dicionarios:
    if pessoa["idade"] > 18:
        print("Nome:", pessoa["nome"], "/", "Idade:", pessoa["idade"])
