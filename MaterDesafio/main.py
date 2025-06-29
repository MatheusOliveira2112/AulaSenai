print("Sistema de Verificação de Elegibilidade para Desconto em Cursos")
nome = input("Qual seu nome? ")
idade = int(input("Qual é a sua idade? "))

if (idade < 18):
    print("Você não tem acesso ao desconto")

else:
    
    situacao = input("Qual a sua situação estudante, desempregado ou trabalhando?")
    conhecimento = input("Você participa de alguma comunidade de TI sim ou não?")
    desconto = 0

if (situacao == "estudante"):
    desconto += 10
elif (situacao == "desempregado"):
    desconto += 15  

if (conhecimento == "sim"):
    desconto += 20

print("Aluno: ", nome, "\nidade: ", idade, "\nSua situação profissional é: ", situacao, "\nPossui conhecimento em TI ", conhecimento)
print(nome, " seu desconto será de: ", desconto, "%")