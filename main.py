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

        if explorador.regiao.tipo == 'Praia':
            # Caso o Explorador consiga voltar a Praia com algum percentual do tesouro
            if explorador.qtd_movimentos < ilha.qtd_movimentos and explorador.tesouro > 0:
                print(f"VOCÊ CHEGOU A PRAIA! Conseguiu resgatar {explorador.tesouro}% do tesouro.\n")
                break
        elif explorador.regiao.tipo == 'Tesouro':
            # Caso o Explorador consiga encontrar o Tesouro
            explorador.regiao.encontrar_tesouro(explorador)
        else:
            # Caso o Explorador também chegue a um Checkpoint guardar seus dados
            if explorador.regiao.tipo in ilha.checkpoints:
                explorador.adicionar_backup()
                
            if explorador.regiao.itens:
                for item in explorador.regiao.itens:
                    # Caso o Explorador encontre uma Criatura
                    if item.tipo == 'criatura':
                        print(Fore.RED + f"{item.nome} encontrado(a)! CUIDADO!")
                        print(Style.RESET_ALL)  # Restaurar cores
                        explorador.lutar_criatura(item)
                    # Caso o Explorador encontre um Perigo
                    elif item.tipo == 'perigo':
                        print(Fore.RED + f"{item.nome} encontrado(a)! CUIDADO!")
                        explorador.remover_pontos_vida(item.pontos)  # Remover pontos do Explorador
                        print(f"Você agora tem {explorador.pontos_vida} pontos de vida!")
                        print(Style.RESET_ALL)  # Restaurar cores
                    # Caso o Explorador encontre uma Planta Medicinal
                    elif item.tipo == 'planta_medicinal':
                        print(Fore.GREEN + f"{item.nome} encontrado(a)!")
                        print(Style.RESET_ALL)  # Restaurar cores

                        while True:
                            resposta = input(f"Deseja utilizar ou guardar (S/Outro)? ")
                            print()

                            # Verificar resposta do Explorador
                            if resposta.upper() == "S":
                                explorador.adicionar_item(item)                # Adicionar o elemento a lista
                                explorador.regiao.remover_item(item)           # Remover o item da Região
                                explorador.adicionar_pontos_vida(item.pontos)  # Adicionar pontos de ataque da Arma
                                
                                print(Fore.GREEN + f"Você guardou {item.nome} na mochila!")
                                print(Style.RESET_ALL)  # Restaurar cores
                            
                            break
                    # Caso o Explorador encontre uma Arma
                    elif item.tipo == 'arma':
                        explorador.encontrar_arma(item)
            # Caso não tenha nenhum item na Região
            else:
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

    print("Você está chegando a ilha!\n")

    explorador = gerar_explorador(ilha.qtd_movimentos)  # Gerar Explorador
    
    iniciar_jogo(ilha, explorador)  # Iniciar jogo
