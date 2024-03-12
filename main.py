from ilha import Ilha
from explorador import Explorador


# Função para inicializar o jogo
def inicializar_jogo():
    print("Você chegou a ilha. Essas são as informações iniciais:")

    # Inicializar o grafo da Ilha
    ilha = Ilha()
    ilha.gerar_ilha()
    ilha.desenhar_ilha()

    # Inicializar o Explorador
    explorador = Explorador()

    # Imprimir informações do Explorador
    explorador.__str__()


# Iniciar o jogo
if __name__ == "__main__":
    print("Bem-vindo(a) Explorador(a)! Você está chegando a ilha. Lembre-se que lá há muitos perigos.")
    print("O tesouro pirata que foi escondido na ilha já atraiu muitos, porém nenhum retornou.")
    print("Espero que você consiga retornar ao menos com alguma parte do tesouro.")
    print("Boa sorte!\n")

    inicializar_jogo()
