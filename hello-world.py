#comenta no python
'''para comentar 
em um range de linhas '''

x = 2

#para gerar um if, só precisa de : e identação na próxima linha
if x < 1:
    print("Olá, mundo")
else:
    print("Hello World")


# como fazer um for
for i in range (10):
    print(i)


nome = "Ticiani"

for i in nome:
    print(i)


# como fazer uma função 

def somar():
    print(2+2)

somar()

#o método da função fica dentro do parênteses

def somar(x,y):
    print(x+y)

somar(3,2)

# inserindo variável na função
# int é para transformar em número inteiro

def somar(x,y):
    return(x+y)

n1 = int (input ("Digite o número 1: "))
n2 = int (input ("Digite o número 2: "))

print (somar(n1,n2))