from colorama import Fore, Style, init
from helpers.gerador import *


# Função para inicializar o jogo
def iniciar_jogo(ilha, explorador):
    print(Fore.MAGENTA + f"Localização atual: {explorador.regiao.tipo}.")
    print(Style.RESET_ALL)  # Restaurar cores
    
    while explorador.qtd_movimentos > 0:
        print(Fore.BLUE + f"Movimentos disponíveis: {explorador.qtd_movimentos}/{ilha.qtd_movimentos}.")
        print(Style.RESET_ALL)  # Restaurar cores

        # ilha.desenhar_mapa(explorador.regiao.tipo)  # Mostrar mapa da Ilha

        explorador.atualizar_regiao(ilha)  # Realizar a movimentação do Explorador

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
                    criatura.encontrar_criatura(explorador)
            
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
    init()          # Iniciar colorama
    
    # Inicializar a Ilha
    ilha = gerar_ilha()

    print("Bem-vindo(a) Explorador(a)! Você está chegando a ilha. Lembre-se que lá há muitos perigos.")
    print(f"Na ilha estão espalhados criaturas, perigos, plantas medicinais e armas. Há {ilha.qtd_itens} de cada.")
    print("O tesouro pirata que foi escondido na ilha já atraiu muitos, porém nenhum retornou.")
    print("Espero que você consiga retornar ao menos com alguma parte do tesouro.")
    print("Boa sorte!\n")
    print("OBS: Toda vez que você for perguntado se quer mudar para uma região aleatória,")
    print("você pode optar por uma das seguinte opções fixas:")
    print("1 - Usar planta medicinal")
    print("2 - Jogar arma fora")

    print("Você está chegando a ilha!\n")

    explorador = gerar_explorador(ilha.qtd_movimentos)  # Gerar Explorador
    
    iniciar_jogo(ilha, explorador)  # Iniciar jogo
