from colorama import init
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
        # Gerar elementos na Ilha
        ilha = gerar_elementos()

        print("Você chegou a ilha!\n")
        print("Essas são as informações iniciais:")

        # # Inicializar o Explorador
        # explorador = Explorador()
        #
        # # Imprimir informações do Explorador
        # explorador.__str__()
        #
        # # explorador.movimentacao()
        #
        # for criatura in ilha.criaturas:
        #     criatura.__str__()
        #     explorador.lutar_criatura(criatura)

        # criatura1 = sortear_criatura()
        # criatura1 = Criatura(criatura1['tipo'], criatura1['pontos_vida'], criatura1['pontos_ataque'],
        #                     criatura1['descricao'], 0)
        #
        # criatura2 = sortear_criatura()
        # criatura2 = Criatura(criatura2['tipo'], criatura2['pontos_vida'], criatura2['pontos_ataque'],
        #                     criatura2['descricao'], 0)
        #
        # criatura1.lutar_criatura(criatura2)

        break


# Método para gerar os elementos da ilha
def gerar_elementos():
    # Inicializar o grafo da Ilha
    ilha = Ilha()
    ilha.gerar_ilha()
    ilha.desenhar_ilha('Praia')

    # for i in range(ilha.sortear_qtd_elementos()):
    #     regiao = random.randint(1, ilha.qtd_regioes - 1)
    #
    #     # Sortear Criatura para adicionar a Ilha
    #     criatura = sortear_criatura()
    #     criatura = Criatura(criatura['tipo'], criatura['pontos_vida'], criatura['pontos_ataque'],
    #                         criatura['descricao'], regiao)
    #     ilha.criaturas.append(criatura)
    #
    #     # Sortear Perigos para adicionar a Ilha
    #     perigos = sortear_perigos()
    #     ilha.perigos.append(perigos)
    #
    #     # Sortear Arma para adicionar a Ilha
    #     arma = sortear_arma()
    #     arma = Arma(arma['tipo'], arma['pontos_ataque'], regiao)
    #     ilha.armas.append(arma)

    return ilha


# Iniciar o jogo
if __name__ == "__main__":
    # Inicializar colorama
    init()

    # Inicializar o jogo
    inicializar_jogo()
