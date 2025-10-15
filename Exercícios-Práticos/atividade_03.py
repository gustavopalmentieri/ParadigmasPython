num = int(input("Digite um número:"))

if num < 0:
    print ("NEGATIVO!!")
elif (num % 2 == 0) or num == 0:
    print ("PAR!!")
else:
    print ("IMPAR!!")
