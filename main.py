from helpers.gerador import *
from helpers.movimento import *
from objetos.regiao import Regiao
from objetos.explorador import Explorador


# Função para inicializar o jogo
def iniciar_jogo():
    print("Bem-vindo(a) Explorador(a)! Você está chegando a ilha. Lembre-se que lá há muitos perigos.")
    print("O tesouro pirata que foi escondido na ilha já atraiu muitos, porém nenhum retornou.")
    print("Espero que você consiga retornar ao menos com alguma parte do tesouro.")
    print("Boa sorte!\n")

    while True:
        # Inicializar a Ilha
        ilha = gerar_ilha()

        print("Você está chegando a ilha!\n")

        print("Essas são as informações iniciais:")
        explorador = Explorador(Regiao(0, 'Praia', 0), ilha.qtd_movimentos)  # Inicializar o Explorador
        explorador.__str__()  # Imprimir informações do Explorador
        ilha.desenhar_mapa(explorador.regiao.tipo)  # Mostrar mapa da Ilha

        mover_explorador(explorador, ilha)  # Realizar a movimentação do Explorador
        break


# Função para iniciar o jogo
if __name__ == "__main__":
    init()          # Iniciar colorama
    iniciar_jogo()  # Iniciar jogo
