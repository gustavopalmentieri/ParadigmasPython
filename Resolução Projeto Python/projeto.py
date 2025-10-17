qtd_pacientes = 3
lista_pacientes = []
IMCs = []
TMBs = []
for paciente in range(qtd_pacientes):

    print(" ---- Dados Cadastrais ----")

    pacientes = {"nome" : input("Informe seu nome completo: "),
                 "peso" : float(input("Informe seu peso em 'KG': ")),
                 "sexo" : input("Digite 'M'- para Masculino e 'F' - para feminino: "),
                 "altura" : int(input("Informe sua altura em 'M': ")),
                 "idade" : int(input("Informe sua idade:"))}
    
    lista_pacientes.append(paciente)
    
for paciente in pacientes:

    paciente['IMC'] = paciente ['peso'] / (paciente['altura'] ** 2)

    if paciente['sexo'] == 'M':
        paciente['TMB']  = 9.99 * paciente['peso'] + 6.25 * paciente['altura'] * 100 - 4,92 * paciente['idade'] + 5

    else:
        paciente['TMB'] = 9.99 * paciente['peso'] + 6.25 * paciente['altura'] * 100 - 4,92 * paciente['idade'] - 161
 

print("\n ----- Menu de Opções ----\n")
print("---> 1 - Maior IMC\n")
print("---> 2 - Maior TMB\n")
print("---> 3 - Menor IMC\n")
print("---> 4 - Menor TMB\n")
print("---> 5 - Encerrar o Programa\n")

escolher = input("Digite a opção de sua preferência: ")

maior_imc = 0

for paciente in lista_pacientes:

  if paciente['IMC'] > maior_imc:
       maior_imc = paciente['IMC']

menor_imc = 1000   #ou pacientes[0]['IMC']

for paciente in lista_pacientes:

   if paciente['IMC'] < menor_imc:
       menor_imc = paciente['IMC']

maior_tmb = 0

for paciente in lista_pacientes:

   if paciente['TMB'] > maior_tmb:
       maior_tmb = paciente['TMB']

menor_tmb = 1000   #ou pacientes[0]['TMB']

for paciente in lista_pacientes:

   if paciente['IMC'] < menor_tmb:
       menor_tmb = paciente['TMB']
     





    



    
