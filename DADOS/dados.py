#	lançamento de x dados de n faces
import random
print("Bem-vindo(a) ao lançamento de dados versão 2.0")
print(" ")


while True:
    x = int(input("Quantos dados você deseja lançar? "))    #Quantidade de dados lançados de uma vez
    if x > 0:
        print("Número válido!")
        break
    else:
        print("Número inválido. Digite um número maior que 0.")


print("Para este jogo são considerados dados com 6 ou mais faces.")

while True:
    n = int(input("Quantas faces possui o dado que deseja lançar? "))

    if n >= 6:
        print("Número válido!")
        break
    else:
        print("Número inválido. Digite um número maior ou igual a 6.")

lancamento = 1

while lancamento <= x:
    resultado = random.randint(1, n)
    print(f'Dado {lancamento}: número sorteado = {resultado}')
    lancamento = lancamento + 1