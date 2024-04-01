import random
from colorama import Fore, Style


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
                    item.remover_qtd_uso()  # Diminuir a quantidade de uso do Item

                    # Caso a quantidade de uso seja menor que 1
                    if item.qtd_uso == 0:
                        explorador.remover_item(item)

                print(Fore.GREEN + f"Você atacou! Houve {dano} de dano.")

                # Teste para saber se a Criatura morreu com o ataque
                if not criatura.esta_viva():
                    print(Fore.YELLOW + f"\n{criatura.nome.upper()} MORREU!")
                    criatura.reviver(ilha)
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


# MÉTODOS PARA A ENTRE ENTRE CRIATURAS


# Método para a luta entre as Criaturas
def encontrar_criaturas(ilha):
    regioes_criaturas = {}
    
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

    if regioes_duplicadas:
        print(f"Regiões duplicadas: {regioes_duplicadas}")
    else:
        print("Nenhuma região duplicada.")
        
    criaturas = []
    
    for criatura in ilha.criaturas:
        for regiao_duplicada in regioes_duplicadas:
            if criatura.regiao.tipo == regiao_duplicada:
                criaturas.append(criatura)
                
    print(criaturas)
