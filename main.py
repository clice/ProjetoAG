from colorama import Fore, Style, init
from helpers.gerador import *


# Função para inicializar o jogo
def iniciar_jogo():
    # Inicializar a Ilha
    ilha = gerar_ilha()

    print("Bem-vindo(a) Explorador(a)! Você está chegando a ilha. Lembre-se que lá há muitos perigos.")
    print(f"Na ilha estão espalhados criaturas, perigos, plantas medicinais e armas. Há {ilha.qtd_itens} de cada.")
    print("O tesouro pirata que foi escondido na ilha já atraiu muitos, porém nenhum retornou.")
    print("Espero que você consiga retornar ao menos com alguma parte do tesouro.")
    print("Boa sorte!\n")

    print("Você está chegando a ilha!\n")

    explorador = gerar_explorador(ilha.qtd_movimentos)  # Gerar Explorador

    print(Fore.MAGENTA + f"Localização atual: {explorador.regiao.tipo}.")
    print(Style.RESET_ALL)  # Restaurar cores

    while explorador.qtd_movimentos > 0:
        print(Fore.BLUE + f"Movimentos disponíveis: {explorador.qtd_movimentos}/{ilha.qtd_movimentos}.")
        print(Style.RESET_ALL)  # Restaurar cores

        # ilha.desenhar_mapa(explorador.regiao.tipo)  # Mostrar mapa da Ilha

        explorador.atualizar_regiao(ilha)  # Realizar a movimentação do Explorador

        if explorador.regiao.tipo == 'Praia':
            # Caso o Explorador consiga voltar a praia com algum percentual do tesouro
            if explorador.qtd_movimentos < ilha.qtd_movimentos and explorador.tesouro > 0:
                print(f"VOCÊ CHEGOU A PRAIA! Conseguiu resgatar {explorador.tesouro}% do tesouro.")
                break
        elif explorador.regiao.tipo == 'Tesouro':
            explorador.regiao.encontrar_tesouro(explorador)
        elif explorador.regiao.tipo in ilha.checkpoints:
            explorador.adicionar_backup()
            explorador.__str__()

        explorador.remover_qtd_movimentos()  # Remover um movimento disponível
        explorador.__str__()

        if explorador.qtd_movimentos == 0:
            print("FIM DE JOGO! Não há mais movimentos disponíveis.")
            break


# Função para iniciar o jogo
if __name__ == "__main__":
    init()          # Iniciar colorama
    iniciar_jogo()  # Iniciar jogo
