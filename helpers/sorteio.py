import random


# Método para sortear uma Criatura
def sortear_criatura():
    # Lista das Criaturas na Ilha
    criaturas = (
        {
            "tipo": "Crocodilo Gigante",
            "pontos_vida": 50,
            "pontos_ataque": 10,
            "descricao": "Tem 8 metros de comprimento, possui pele dura, "
                         "bastante força e mordida poderosa"
        },
        {
            "tipo": "Formiga Quimera",
            "pontos_vida": 50,
            "pontos_ataque": 10,
            "descricao": "Podem desossar um boi em poucos minutos "
                         "apesar de frágeis individualmente"
        },
        {
            "tipo": "Onça Pintada",
            "pontos_vida": 50,
            "pontos_ataque": 10,
            "descricao": "Consegue se camuflar quase que perfeitamente, "
                         "e possui o tamanho de um touro, com garras "
                         "e dentes poderosos"
        }
    )

    return random.choice(criaturas)


# Método para sortear um Perigo
def sortear_perigos():
    # Lista das Plantas Venenosas
    plantas_venenosas = (
        {
            "tipo": "Fonte de gás venenoso",
            "pontos": 5
        },
        {
            "tipo": "Poço de piche",
            "pontos": 10
        },
        {
            "tipo": "Areia movediça",
            "pontos": 15
        },
        {
            "tipo": "Rochas deslizantes",
            "pontos": 15
        },
        {
            "tipo": "Planta venenosa",
            "pontos": 15
        }
    )

    return random.choice(plantas_venenosas)


# Método para sortear uma Planta Medicinal
def sortear_planta_medicinal():
    # Lista das Plantas Medicinais
    plantas_medicinais = (
        {
            "tipo": "Planta Medicinal 1",
            "pontos": 5
        },
        {
            "tipo": "Planta Medicinal 2",
            "pontos": 10
        },
        {
            "tipo": "Planta Medicinal 3",
            "pontos": 15
        }
    )

    return random.choice(plantas_medicinais)


# Método para sortear uma Arma
def sortear_arma():
    # Lista das Armas na Ilha
    armas = (
        {
            "tipo": "Faca",
            "pontos_ataque": 5,

        },
        {
            "tipo": "Espada",
            "pontos_ataque": 10
        },
        {
            "tipo": "Pistola",
            "pontos_ataque": 15
        }
    )
    
    return random.choice(armas)


# Métofo para sortear um
def sortear_regiao():
    regioes = ('Montanha', 'Lago', 'Paredão de Rocha', 'Riacho', 'Floresta')
    return random.choice(regioes)


# criatura = sortear_criatura()
# criatura = Criatura(criatura['tipo'], criatura['pontos_vida'], criatura['pontos_ataque'], criatura['descricao'], 0)
# resposta = input(f"Deseja lutar com {criatura.tipo} (S/N)? ")
# print(resposta)
