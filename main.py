from outros import *
from ilha import Ilha
from explorador import Explorador


# Função para inicializar o jogo
def inicializar_jogo():
    # print("Bem-vindo(a) Explorador(a)! Você está chegando a ilha. Lembre-se que lá há muitos perigos.")
    # print("O tesouro pirata que foi escondido na ilha já atraiu muitos, porém nenhum retornou.")
    # print("Espero que você consiga retornar ao menos com alguma parte do tesouro.")
    # print("Boa sorte!\n")

    while True:
        inicializar_elementos()
        break


# Método para inicializar os elementos na Ilha
def inicializar_elementos():
    # Inicializar o grafo da Ilha
    ilha = Ilha()
    # ilha.gerar_ilha()
    # ilha.desenhar_ilha("Praia")

    # Gerar porcentagem de elementos na Ilha
    porcentagem = random.randint(20, 30)
    qtd_elementos = round(ilha.qtd_regioes * (porcentagem / 100))

    # Gerar elementos na Ilha
    for i in range(qtd_elementos):
        regiao = random.randint(1, ilha.qtd_regioes - 1)

        # Sortear Criatura para adicionar a Ilha
        criatura = sortear_criatura()
        criatura = Criatura(criatura['tipo'], criatura['pontos_vida'], criatura['pontos_ataque'],
                            criatura['descricao'], regiao)
        ilha.criaturas.append(criatura)

    print("Você chegou a ilha. Essas são as informações iniciais:")

    # Inicializar o Explorador
    explorador = Explorador()

    # Imprimir informações do Explorador
    explorador.__str__()


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
