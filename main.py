import time

from colorama import Style, Back, init
from helpers.gerador import *
from helpers.opcoes import *


# Função para inicializar o jogoss
def iniciar_jogo():
    ilha = gerar_ilha()  # Gerar Ilha
    explorador = gerar_explorador(ilha.qtd_movimentos)  # Gerar Explorador

    print("Bem-vindo(a) Explorador(a)! Você está chegando a ilha. Lembre-se que lá há muitos perigos.")
    print(f"Na ilha estão espalhados criaturas, perigos, plantas medicinais e armas. Há {ilha.qtd_itens} de cada.")
    
    print(f"Você pode encontrar as seguintes criaturas espalhadas na ilha: ")
    for criatura in ilha.criaturas:
        print(f"{criatura.nome}", end=", ")
    print("e ter que enfrentá-las")
    
    print("O tesouro pirata que foi escondido na ilha já atraiu muitos, porém nenhum retornou.")
    print("Espero que você consiga retornar ao menos com alguma parte do tesouro.")
    print("Boa sorte!\n")

    time.sleep(1)  # Pausa de 1 segundo

    print(Fore.YELLOW + "OBS: Toda vez que você for perguntado se quer mudar para uma região aleatória, \n"
                        "você pode optar por uma das seguinte opções fixas:\n"
                        "1 - Jogar arma fora\n")

    time.sleep(1)  # Pausa de 1 segundo

    explorador.mostrar_regiao()  # Mostrar localização atual

    explorador.__str__()  # Imprimir informações do Explorador

    time.sleep(1)  # Pausa de 1 segundo

    print(Fore.BLUE + f"Movimentos disponíveis: {explorador.qtd_movimentos}/{ilha.qtd_movimentos}.\n")

    # Laço para iniciar o contador do jogo
    while explorador.qtd_movimentos > 0:
        ilha.desenhar_mapa(explorador.regiao.tipo)  # Mostrar mapa da Ilha

        lutar_criaturas(ilha)  # Encontrar as regiões com várias Criaturas 

        explorador.mover(ilha)  # Realizar a movimentação do Explorador

        # Caso o Explorador consiga voltar a Praia com algum percentual do tesouro
        if explorador.regiao.tipo == 'Praia':
            if explorador.qtd_movimentos < ilha.qtd_movimentos and explorador.tesouro > 0:
                print(Fore.CYAN + f"VOCÊ CHEGOU A PRAIA COM PARTE DO TESOURO!")
                print(Fore.CYAN + f"Você conseguiu resgatar {explorador.tesouro}% do tesouro.\n")
                break
        # Caso o Explorador consiga encontrar o Tesouro
        elif explorador.regiao.tipo == 'Tesouro':
            explorador.regiao.encontrar_tesouro(explorador)
        # Quando o Explorador vai para outra Região
        else:
            # Caso o Explorador também chegue a um Checkpoint guardar seus dados
            if explorador.regiao.tipo in ilha.checkpoints:
                explorador.adicionar_backup()
                ilha.remover_checkpoint(explorador.regiao.tipo)

            # Caso não haja nada na Região
            if not explorador.regiao.criaturas and not explorador.regiao.itens:
                print("Nada na região. Continue procurando...\n")
            else:
                # Caso haja uma Criatura na Região
                if explorador.regiao.criaturas:
                    for criatura in explorador.regiao.criaturas:
                        print(Fore.RED + f"{criatura.nome} encontrado(a)! CUIDADO!\n")
                        criatura.__str__()
                        lutar(ilha, explorador, criatura)

                # Caso haja Itens na Região
                if explorador.regiao.itens:
                    for item in explorador.regiao.itens:
                        # Caso o Explorador encontre um Perigo
                        if item.tipo == 'perigo':
                            explorador.encontrar_perigo(item)
                        # Caso o Explorador encontre uma Planta Medicinal
                        elif item.tipo == 'planta_medicinal':
                            explorador.encontrar_planta_medicinal(item)
                        # Caso o Explorador encontre uma Arma
                        elif item.tipo == 'arma':
                            explorador.encontrar_arma(item)
            
        explorador.remover_qtd_movimentos()  # Remover um movimento disponível

        # Caso acabe os movimentos disponíveis para o Explorador
        if explorador.qtd_movimentos == 0:
            print("FIM DE JOGO! Não há mais movimentos disponíveis.\n")
            break
        else:
            explorador.__str__()    # Imprimir informações do Explorador
            ilha.mover_criaturas()  # Mover as Criaturas de Região no mapa da Ilha

            print(Fore.BLUE + f"Movimentos disponíveis: {explorador.qtd_movimentos}/{ilha.qtd_movimentos}.\n")


# Função para iniciar o jogo
if __name__ == "__main__":
    init(autoreset=True)  # Iniciar colorama com autoreset para restaurar padrão

    print(Fore.LIGHTYELLOW_EX + " ☠️    ☠️    ☠️    ☠️ " + Back.YELLOW + Fore.BLACK +
          " A ILHA DO TESOURO PERDIDO (THE GAME) " + Style.RESET_ALL + " ☠️    ☠️    ☠️    ☠️ \n")

    while True:
        resposta = input("Deseja começar o jogo (S/Outro)? ")
        print()

        if resposta.upper() != "S":
            print(Fore.LIGHTYELLOW_EX + "FIM DE JOGO!")
            break
    
        iniciar_jogo()  # Iniciar jogo
