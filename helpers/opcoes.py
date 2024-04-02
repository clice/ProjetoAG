import random

from helpers.gerador import sortear_criatura
from colorama import Fore, Style
from objetos.criatura import Criatura


# Função para o remover os pontos de vida do atacado com base nos pontos de ataque do atacante
def atacar(atacante, atacado):
    dano = random.randint(1, atacante.pontos_ataque)
    atacado.pontos_vida -= dano
    return dano


# LUTA ENTRE O EXPLORADOR E UMA CRIATURA

# Função para a luta entre o Explorador e a Criatura
def lutar(ilha, explorador, criatura):
    while True:
        resposta = input(f"Deseja lutar com {criatura.nome} (S/Outro)? ")

        # Verificar resposta do Explorador
        if resposta.upper() != "S":
            # Gerar dano no Explorador
            dano = atacar(criatura, explorador)
            print(Fore.RED + f"Você sofreu {dano} de dano!")
            print(Style.RESET_ALL)  # Restaurar cores

            # Caso o Explorador morra com o ataque
            if not explorador.esta_vivo():
                explorador.reviver()
            else:
                print(f"Você agora tem {explorador.pontos_vida} pontos de vida.")

            break

        rodada = 1  # Rodada inicial

        # Se o Explorador optar por lutar contra a Criatura
        while rodada <= 3:
            print(f"\nROUND {rodada}")

            # Condições para os ataques
            # Primeiro o Explorador ataca a Criatura
            if explorador.esta_vivo() and criatura.esta_viva():
                dano = atacar(explorador, criatura)  # Calcular o dano gerado pelo Explorador
                item = explorador.tem_armas()        # Se o Esplorador tem armas para

                if item:
                    explorador.item[0].remover_qtd_uso()  # Diminuir a quantidade de uso do Item

                    # Caso a quantidade de uso seja menor que 1
                    if item.qtd_uso == 0:
                        print(Fore.YELLOW + f"{explorador.item[0].nome} já foi usada ao máximo!")
                        print(Style.RESET_ALL)  # Restaurar cores
                        explorador.remover_item(item)

                print(Fore.GREEN + f"Você atacou! Houve {dano} de dano.")

                # Teste para saber se a Criatura morreu com o ataque
                if not criatura.esta_viva():
                    print(Fore.YELLOW + f"\n{criatura.nome.upper()} MORREU!")
                    print(Style.RESET_ALL)  # Restaurar cores
                    
                    # Reviver a mesma Criatura em outra região 
                    regiao = random.choice(ilha.regioes[1:-1])
                    criatura = sortear_criatura()  # Sortear Criatura para adicionar a Região
                    criatura = Criatura(
                        criatura['nome'], criatura['tipo'], criatura['pontos_vida'],
                        criatura['pontos_ataque'], criatura['descricao'], regiao
                    )  # Objeto Criatura
                    regiao.adicionar_criatura(criatura) 
                    
                    break
                else:
                    print(f"{criatura.nome} agora tem {criatura.pontos_vida} pontos de vida.")

            # Segundo a Criatura ataca o Explorador
            if criatura.esta_viva() and explorador.esta_vivo():
                dano = atacar(criatura, explorador)
                print(Fore.RED + f"{criatura.nome.upper()} ATACOU! Houve {dano} de dano.")

                # Teste para saber se o Explorador morreu com o ataque
                if not explorador.esta_vivo():
                    explorador.reviver()
                    break
                else:
                    print(f"Você agora tem {explorador.pontos_vida} pontos de vida.")

            print(Style.RESET_ALL)  # Restaurar cores

            # Se as três rodadas ainda não terminaram nem o Explorador ou Criatura morreram
            if rodada <= 2:
                # Perguntar novamente para continuar a luta
                resposta = input(f"Deseja continuar lutando com {criatura.nome}? (S/Outro)? ")

                # Verificar resposta do Explorador
                if resposta.upper() != "S":
                    break

            rodada += 1  # Acrescentar rodada concluida

        # Se os pontos de vida do Explorador chegarem a zero
        if not explorador.esta_vivo() or not criatura.esta_viva():
            print(Style.RESET_ALL)  # Restaurar cores
            break


# MÉTODOS PARA A LUTA ENTRE CRIATURAS


# Método para a luta entre as Criaturas
def encontrar_criaturas(ilha):
    regioes_criaturas = {}  # Lista das regiões das Criaturas na Ilha
    
    # Laço para percorrer todas as Criaturas da Ilha
    for criatura in ilha.criaturas:
        regiao_criatura = criatura.regiao.tipo  # Pegar o tipo de Região da Criatura

        # Se a Região já está na lista de Regiões
        if regiao_criatura in regioes_criaturas:
            regioes_criaturas[regiao_criatura] += 1  # Contador de regiões
        else:
            regioes_criaturas[regiao_criatura] = 1  # Contador inicial de regiões

    # Encontrar os casos duplicador de regiões quando tiver mais de 1 caso
    regioes_duplicadas = [regiao for regiao, qtd_regioes in regioes_criaturas.items() if qtd_regioes > 1]
    
    criaturas = []  # Lista das Criaturas nas regiões duplicadas

    # Caso haja regiões duplicadas
    if regioes_duplicadas:
        # Laço para percorrer as Criaturas da Ilha e buscar as que estão na mesma Região
        for criatura in ilha.criaturas:
            for regiao_duplicada in regioes_duplicadas:
                if criatura.regiao.tipo == regiao_duplicada:
                    criaturas.append(criatura)
                        
    return criaturas


# Método para a luta encontre as Criaturas
def lutar_criaturas(ilha):
    criaturas = encontrar_criaturas(ilha)
    
    if criaturas:
        # Encontrar a Criatura com o maior pontos de ataque da lista
        criatura_mais_forte = max(criaturas, key=lambda criatura: criatura.pontos_ataque)

        # Encontrar a Criatura com o menor pontos de ataque da lista
        criatura_mais_fraca = min(criaturas, key=lambda criatura: criatura.pontos_ataque)
    
        # Caso essas Criaturas estejam na mesma Região
        if criatura_mais_forte.regiao.tipo == criatura_mais_fraca.regiao.tipo:
            dano = atacar(criatura_mais_fraca, criatura_mais_forte)
            print(Fore.GREEN + f"{criatura_mais_forte.nome} agora tem {criatura_mais_forte.pontos_vida} pontos de vida.")
            print(f"Sofreu {dano} de dano.")
            print(Style.RESET_ALL)  # Restaurar cores
            
            # Reviver a mesma Criatura em outra região 
            regiao = random.choice(ilha.regioes[1:-1])
            criatura = sortear_criatura()  # Sortear Criatura para adicionar a Região
            criatura = Criatura(
                criatura['nome'], criatura['tipo'], criatura['pontos_vida'],
                criatura['pontos_ataque'], criatura['descricao'], regiao
            )  # Objeto Criatura
            regiao.adicionar_criatura(criatura)
    