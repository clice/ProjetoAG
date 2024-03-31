import time

from colorama import Fore, Style, init
from helpers.gerador import *
from helpers.opcoes import *


# Função para inicializar o jogo
def iniciar_jogo():
    ilha = gerar_ilha()  # Gerar Ilha
    explorador = gerar_explorador(ilha.qtd_movimentos)  # Gerar Explorador

    print("Bem-vindo(a) Explorador(a)! Você está chegando a ilha. Lembre-se que lá há muitos perigos.")
    print(f"Na ilha estão espalhados criaturas, perigos, plantas medicinais e armas. Há {ilha.qtd_itens} de cada.")
    print("O tesouro pirata que foi escondido na ilha já atraiu muitos, porém nenhum retornou.")
    print("Espero que você consiga retornar ao menos com alguma parte do tesouro.")
    print("Boa sorte!\n")

    time.sleep(1)  # Pausa de 1 segundo

    print(Fore.YELLOW + "OBS: Toda vez que você for perguntado se quer mudar para uma região aleatória,")
    print("você pode optar por uma das seguinte opções fixas:")
    print("1 - Usar planta medicinal")
    print("2 - Jogar arma fora\n")

    time.sleep(1)  # Pausa de 1 segundo

    explorador.mostrar_regiao()  # Mostrar localização atual

    iniciar_contador(ilha, explorador)  # Iniciar contador


# Função para iniciar o contador do jogo
def iniciar_contador(ilha, explorador):
    print("Informações:")
    explorador.__str__()  # Imprimir informações do Explorador

    time.sleep(1)  # Pausa de 1 segundo

    while explorador.qtd_movimentos > 0:
        print(Fore.BLUE + f"Movimentos disponíveis: {explorador.qtd_movimentos}/{ilha.qtd_movimentos}.")
        print(Style.RESET_ALL)  # Restaurar cores

        # ilha.desenhar_mapa(explorador.regiao.tipo)  # Mostrar mapa da Ilha

        mover_explorador(explorador, ilha)  # Realizar a movimentação do Explorador

        # Caso o Explorador consiga voltar a Praia com algum percentual do tesouro
        if explorador.regiao.tipo == 'Praia':
            if explorador.qtd_movimentos < ilha.qtd_movimentos and explorador.tesouro > 0:
                print(f"VOCÊ CHEGOU A PRAIA! Conseguiu resgatar {explorador.tesouro}% do tesouro.\n")
                break
        # Caso o Explorador consiga encontrar o Tesouro
        elif explorador.regiao.tipo == 'Tesouro':
            explorador.regiao.encontrar_tesouro(explorador)
        # Quando o Explorador vai para outra Região
        else:
            # Caso o Explorador também chegue a um Checkpoint guardar seus dados
            if explorador.regiao.tipo in ilha.checkpoints:
                explorador.adicionar_backup()
                
            # Caso haja uma Criatura na Região
            if explorador.regiao.criaturas:
                for criatura in explorador.regiao.criaturas:
                    explorador.encontrar_criatura(criatura)
            
            # Caso haja Itens na Região
            if explorador.regiao.itens:                    
                for item in explorador.regiao.itens:
                    # Caso o Explorador encontre um Perigo
                    if item.tipo == 'perigo':
                        item.encontrar_perigo(explorador)
                    # Caso o Explorador encontre uma Planta Medicinal
                    elif item.tipo == 'planta_medicinal':
                        item.encontrar_planta_medicinal(explorador)
                    # Caso o Explorador encontre uma Arma
                    elif item.tipo == 'arma':
                        item.encontrar_arma(explorador)
                        
            # Caso não haja nada na Região
            if not explorador.regiao.criaturas and not explorador.regiao.itens:
                print("Nada na região. Continue procurando...\n")
            
        explorador.remover_qtd_movimentos()  # Remover um movimento disponível
        explorador.__str__()

        if explorador.qtd_movimentos == 0:
            print("FIM DE JOGO! Não há mais movimentos disponíveis.\n")
            break


# Função para iniciar o jogo
if __name__ == "__main__":
    init()  # Iniciar colorama

    print(Fore.LIGHTYELLOW_EX + "JUMANJI: A ILHA DO TESOURO")
    print(Style.RESET_ALL)  # Restaurar cores

    while True:
        resposta = input("Deseja começar o jogo (S/Outro)? ")
        print()

        if resposta.upper() != "S":
            print(Fore.LIGHTYELLOW_EX + "FIM DE JOGO!")
            break
    
        iniciar_jogo()  # Iniciar jogo
