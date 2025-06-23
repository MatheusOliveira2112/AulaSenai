print("CALCULADORA")
print("Escolha a operação que deseja fazer: ")

print("1: soma\n2: subtração\n3: multiplicação\n4: divisão")
pergunta = input()

def soma( a, b):
    return a + b
     

def subtracao( a, b):
    return a - b 
    

def multiplicacao( a, b):
    return a * b
    

def divisao( a, b):
    return a / b 
    

if (pergunta >= "5"):
    print("Erro, você selecionou a opção errada")
elif (pergunta == "1"):
    print("insira o primeiro valor: ")
    valor1 = float(input())

    print("insira o segundo valor: ")
    valor2 = float(input())

    calculo = soma(valor1,valor2)
    print("O resultado dos valores é: ", calculo)
elif (pergunta == "2"):    
    print("insira o primeiro valor: ")
    valor1 = float(input())

    print("insira o segundo valor: ")
    valor2 = float(input())

    calculo = subtracao(valor1, valor2)
    print("O resultado dos valores é: ", calculo)
elif (pergunta == "3"):
    print("insira o primeiro valor: ")
    valor1 = float(input())

    print("insira o segundo valor: ")
    valor2 = float(input())

    calculo = multiplicacao(valor1, valor2)
    print("O resultado dos valores é: ", calculo)
else: 
    print("insira o primeiro valor: ")
    valor1 = float(input())

    print("insira o segundo valor: ")
    valor2 = float(input())
    calculo = divisao(valor1, valor2)
    print("O resultado dos valores é: ", calculo)
    

   
