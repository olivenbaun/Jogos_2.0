#	lançamento de x dados de n faces
import random
print("Bem-vindo(a) ao lançamento de dados versão 2.0")

x = int(input("Quantos dados você deseja lançar? "))    #Quantidade de dados lançados de uma vez
n = int(input("Quantas faces possui o dado que deseja lançar? "))   #Número de faces que o dado terá sendo 6 o número mínimo de faces de um dado

lancamento = 1

while lancamento <= x:
    resultado = random.randint(1, n)
    print(f'Dado {lancamento}: número sorteado = {resultado}')
    lancamento = lancamento + 1