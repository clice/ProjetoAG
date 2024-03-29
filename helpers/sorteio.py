import random


# Métofo para sortear um
def sortear_regiao(regioes_usadas):
    regioes = [
        'Montanha', 'Lago', 'Paredão de Rocha', 'Riacho', 'Floresta',
        'Deserto', 'Caverna', 'Planície', 'Selva'
    ]

    # Se a lista de regiões não estiver vazia
    if regioes_usadas:
        # Busca os itens de `regioes` que não estão na `lista_regioes` e
        # adiciona a lista lista a variável `regioes`
        regioes = [regiao for regiao in regioes if regiao not in regioes_usadas]

    return random.choice(regioes)


# Método para sortear uma Criatura
def sortear_criatura():
    # Lista das Criaturas na Ilha
    criaturas = (
        {
            "nome": "Crocodilo Gigante",
            "pontos_vida": 50,
            "pontos_ataque": 10,
            "descricao": "Tem 8 metros de comprimento, possui pele dura, "
                         "bastante força e mordida poderosa"
        },
        {
            "nome": "Formiga Quimera",
            "pontos_vida": 50,
            "pontos_ataque": 10,
            "descricao": "Podem desossar um boi em poucos minutos "
                         "apesar de frágeis individualmente"
        },
        {
            "nome": "Onça Pintada",
            "pontos_vida": 50,
            "pontos_ataque": 10,
            "descricao": "Consegue se camuflar quase que perfeitamente, "
                         "e possui o tamanho de um touro, com garras "
                         "e dentes poderosos"
        }
    )

    return random.choice(criaturas)


# Método para sortear um Perigo
def sortear_perigo():
    # Lista das Plantas Venenosas
    plantas_venenosas = (
        {
            "nome": "Fonte de gás venenoso",
            "tipo": "planta_venenosa",
            "pontos": 5
        },
        {
            "nome": "Poço de piche",
            "tipo": "planta_venenosa",
            "pontos": 10
        },
        {
            "nome": "Areia movediça",
            "tipo": "planta_venenosa",
            "pontos": 15
        },
        {
            "nome": "Rochas deslizantes",
            "tipo": "planta_venenosa",
            "pontos": 15
        },
        {
            "nome": "Planta venenosa",
            "tipo": "planta_venenosa",
            "pontos": 15
        }
    )

    return random.choice(plantas_venenosas)


# Método para sortear uma Planta Medicinal
def sortear_planta_medicinal():
    # Lista das Plantas Medicinais
    plantas_medicinais = (
        {
            "nome": "Planta Medicinal 1",
            "tipo": "planta_medicinal",
            "pontos": 5
        },
        {
            "nome": "Planta Medicinal 2",
            "tipo": "planta_medicinal",
            "pontos": 10
        },
        {
            "nome": "Planta Medicinal 3",
            "tipo": "planta_medicinal",
            "pontos": 15
        }
    )

    return random.choice(plantas_medicinais)


# Método para sortear uma Arma
def sortear_arma():
    # Lista das Armas na Ilha
    armas = (
        {
            "nome": "Faca",
            "tipo": "arma",
            "pontos": 5,

        },
        {
            "nome": "Espada",
            "tipo": "arma",
            "pontos": 10
        },
        {
            "nome": "Pistola",
            "tipo": "arma",
            "pontos": 15
        }
    )
    
    return random.choice(armas)
