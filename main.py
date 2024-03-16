from helpers.sorteio import *
from objetos.ilha import Ilha
from objetos.arma import Arma
from objetos.criatura import Criatura
from objetos.explorador import Explorador


# Função para inicializar o jogo
def inicializar_jogo():
    print("Bem-vindo(a) Explorador(a)! Você está chegando a ilha. Lembre-se que lá há muitos perigos.")
    print("O tesouro pirata que foi escondido na ilha já atraiu muitos, porém nenhum retornou.")
    print("Espero que você consiga retornar ao menos com alguma parte do tesouro.")
    print("Boa sorte!\n")

    while True:
        inicializar_elementos()
        break


# Método para inicializar os elementos na Ilha
def inicializar_elementos():
    # Inicializar o grafo da Ilha
    ilha = Ilha()
    ilha.gerar_ilha()
    ilha.desenhar_ilha("Praia")

    # Gerar elementos na Ilha
    gerar_elementos(ilha)

    print("Você chegou a ilha. Essas são as informações iniciais:")

    # Inicializar o Explorador
    explorador = Explorador()

    # Imprimir informações do Explorador
    explorador.__str__()


# Método para gerar os elementos da ilha
def gerar_elementos(ilha):
    for i in range(ilha.sortear_qtd_elementos()):
        regiao = random.randint(1, ilha.qtd_regioes - 1)

        # Sortear Criatura para adicionar a Ilha
        criatura = sortear_criatura()
        criatura = Criatura(criatura['tipo'], criatura['pontos_vida'], criatura['pontos_ataque'],
                            criatura['descricao'], regiao)
        ilha.criaturas.append(criatura)

        # Sortear Perigos para adicionar a Ilha
        perigos = sortear_perigos()
        ilha.perigos.append(perigos)

        # Sortear Arma para adicionar a Ilha
        arma = sortear_arma()
        arma = Arma(arma['tipo'], arma['pontos_ataque'], regiao)
        ilha.armas.append(arma)


# Iniciar o jogo
if __name__ == "__main__":
    inicializar_jogo()

# import random
#
# def guess_the_number():
#     print("Welcome to Guess the Number!")
#     print("I'm thinking of a number between 1 and 100.")
#     secret_number = random.randint(1, 100)
#     attempts = 0
#
#     while True:
#         try:
#             guess = int(input("Enter your guess: "))
#             attempts += 1
#
#             if guess < secret_number:
#                 print("Too low! Try again.")
#             elif guess > secret_number:
#                 print("Too high! Try again.")
#             else:
#                 print(f"Congratulations! You guessed the number in {attempts} attempts!")
#                 break
#         except ValueError:
#             print("Invalid input. Please enter a number.")
#
# if __name__ == "__main__":
#     guess_the_number()
