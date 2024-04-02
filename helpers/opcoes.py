import random

from helpers.gerador import lista_criaturas
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
        print()

        # Verificar resposta do Explorador
        if resposta.upper() != "S":
            # Gerar dano no Explorador
            dano = atacar(criatura, explorador)
            print(Fore.RED + f"Você sofreu {dano} de dano!")

            # Caso o Explorador morra com o ataque
            if not explorador.esta_vivo():
                explorador.reviver()
            else:
                explorador.remover_tesouro(dano)  # Remover a quantidade do tesouro que ele tem com base no dano sofrido
                print(f"Você agora tem {explorador.pontos_vida} pontos de vida.")
                print(Style.RESET_ALL)  # Restaurar cores

            break

        rodada = 1  # Rodada inicial

        # Se o Explorador optar por lutar contra a Criatura
        while rodada <= 3:
            print(f"ROUND {rodada}")

            # Condições para os ataques
            # Primeiro o Explorador ataca a Criatura
            if explorador.esta_vivo() and criatura.esta_viva():
                dano = atacar(explorador, criatura)  # Calcular o dano gerado pelo Explorador
                print(Fore.GREEN + f"Você atacou! Houve {dano} de dano.")

                if explorador.tem_armas():
                    explorador.item[0].remover_qtd_uso()  # Diminuir a quantidade de uso do Item

                    # Caso a quantidade de uso seja menor que 1
                    if explorador.item[0].qtd_uso <= 0:
                        print(Fore.YELLOW + f"{explorador.item[0].nome} já foi usada ao máximo!")
                        print(Style.RESET_ALL)  # Restaurar cores
                        explorador.remover_item(explorador.item)

                # Teste para saber se a Criatura morreu com o ataque
                if not criatura.esta_viva():
                    criatura.regiao.remover_criatura(criatura)  # Remover Criatura da Região atual
                    print(Fore.YELLOW + f"\n{criatura.nome.upper()} MORREU!")
                    print(Style.RESET_ALL)  # Restaurar cores
                    
                    # Buscar a Criatura desejada para reviver em outra Região
                    for aux_criatura in lista_criaturas():
                        if aux_criatura["nome"] == criatura.nome:
                            # Reviver a mesma Criatura em outra região 
                            regiao = random.choice(ilha.regioes[1:-1])
                            nova_criatura = Criatura(
                                aux_criatura['nome'], aux_criatura['tipo'], aux_criatura['pontos_vida'],
                                aux_criatura['pontos_ataque'], aux_criatura['descricao'], regiao
                            )  # Objeto Criatura
                            regiao.adicionar_criatura(nova_criatura)  # Adicionar Criatura
                            
                            print(Fore.RED + f"{criatura.nome.upper()} FOI REVIVIDO(A)!")
                            print(Style.RESET_ALL)  # Restaurar cores                
                            break
                    
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
                    explorador.remover_tesouro(dano)  # Remover a quantidade do tesouro que ele tem com base no dano sofrido

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
        
        # Verificar resposta do Explorador
        if resposta.upper() != "S":
            print()
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
            dano = atacar(criatura_mais_fraca, criatura_mais_forte)           # Criatura mais fraca ataca
            criatura_mais_fraca.regiao.remover_criatura(criatura_mais_fraca)  # Criatura mais fraca morre
            
            # Para a Criatura mais forte
            if criatura_mais_forte.pontos_vida > 0:
                print(Fore.GREEN + f"{criatura_mais_forte.nome} agora tem {criatura_mais_forte.pontos_vida} pontos de vida.")
                print(f"Sofreu {dano} de dano.")
                print(Style.RESET_ALL)  # Restaurar cores
            else:
                criatura_mais_forte.regiao.remover_criatura(criatura_mais_forte)  # Criatura mais forte morre
                
                # Buscar a Criatura mais forte desejada para reviver em outra Região
                for criatura in lista_criaturas():
                    if criatura["nome"] == criatura_mais_forte.nome:
                        # Reviver a mesma Criatura em outra região 
                        regiao = random.choice(ilha.regioes[1:-1])
                        criatura = Criatura(
                            criatura['nome'], criatura['tipo'], criatura['pontos_vida'],
                            criatura['pontos_ataque'], criatura['descricao'], regiao
                        )  # Objeto Criatura
                        regiao.adicionar_criatura(criatura)  # Adicionar Criatura
                        
                        print(Fore.RED + f"{criatura.nome.upper()} FOI REVIVIDO(A)!")
                        print(Style.RESET_ALL)  # Restaurar cores                
                        break
            
            # Buscar a Criatura mais fraca desejada para reviver em outra Região
            for criatura in lista_criaturas():
                if criatura["nome"] == criatura_mais_fraca.nome:
                    # Reviver a mesma Criatura em outra região 
                    regiao = random.choice(ilha.regioes[1:-1])
                    criatura = Criatura(
                        criatura['nome'], criatura['tipo'], criatura['pontos_vida'],
                        criatura['pontos_ataque'], criatura['descricao'], regiao
                    )  # Objeto Criatura
                    regiao.adicionar_criatura(criatura)  # Adicionar Criatura
                    
                    print(Fore.RED + f"{criatura.nome.upper()} FOI REVIVIDO(A)!")
                    print(Style.RESET_ALL)  # Restaurar cores
                    break
            
    