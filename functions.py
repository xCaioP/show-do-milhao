import os


def limpar_tela():
    """
    Essa função limpa a tela no cmd, usando o módulo os.
    return: None
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def colocar_linha(quantidade=40):
    """
    Essa função adiciona hífens para ter uma aparência melhor via CMD.
    return: None
    """
    print("-" * quantidade)


def introducao():
    """
    Essa função cria a Tela inicial do jogo,
    dando uma breve descrição e interagindo com o jogador.
    return: None
    """
    colocar_linha()
    print("\nBaseado na primeira versão", "\n")
    colocar_linha()
    print("\nShow do Milhão")
    print("Sejam muito bem-vindos!", "\n")
    colocar_linha()
    print("\nPreparados para uma diversão?")
    print("Vamos começar com perguntas bem fáceis e depois vamos dificultar um pouco :)", "\n")
    colocar_linha()
    print("\nEstão preparados? ", "\n")
    input("\nPressione ENTER para iniciar")
    limpar_tela()


def mostrar_valor_proxima_pergunta(valor_acertar):
    """
    Essa função serve para mostrar o valor da proxima pergunta.
    param: valor_acertar: double
    return: None
    """
    print("Proxima pergunta valerá:", valor_acertar, "reais", "\n")
    colocar_linha()


def mostrar_valor_parar(valor_parar):
    """
    Essa função serve para mostrar o valor caso o jogador queira parar, e a cada pergunta esse valor muda ou altera.
    param: valor_parar: double
    return: None
    """
    colocar_linha()
    print("\nParar: ", valor_parar, "reais")


def mostrar_valor_pergunta(valor_acertar):
    """
    Essa função mostra ao usuário o valor da pergunta atual.
    param: valor_acertar: double
    return: None
    """
    print("Essa pergunta vale: ", valor_acertar, "reais")


def mostrar_valor_ao_terminar_jogo(valor_final):
    """
    Essa função mostra o valor final recebido pelo usuário.
    param: valor_final: double
    return: None
    """
    print("Você recebeu:", valor_final, "reais")


dados = (
    {"pergunta": "Primeira pergunta: \nQue personagem do folclore brasileiro tem uma perna só? ",
     "opcoes": ("1) Cuca ", "2) Curupira", "3) Boitatá", "4) Saci-pererê"), "resposta": "4", "valor_acertar": 1000},

    {"pergunta": "Qual animal da fauna brasileira está retratado na nota de dez reais?",
    "opcoes": ("1) Jabuti", "2) Onça", "3) Arara", "4) Tucano"), "resposta": "3", "valor_acertar": 2000, "valor_errar": 500, "valor_parar": 2000},

    {"pergunta": "Qual a matéria-prima do ketchup?",
    "opcoes": ("1) Abacate", "2) Tomate", "3) Cereja", "4) Pessego"), "resposta": "2", "valor_acertar": 3000, "valor_errar": 1000, "valor_parar": 2000},

    {"pergunta": "Qual é a maior floresta do planeta? ",    
    "opcoes": ("1) Negra", "2) De Sherwood", "3) Da Tijuca", "4) Amazônica"), "resposta": "4", "valor_acertar": 4000, "valor_errar": 500, "valor_parar": 000},

    {"pergunta": "Qual casal foi expulso do Paraíso?",
    "opcoes": ("1) Sansão e Dalila", "2) José e Maria", "3) Sara e Abraão", "4) Adão e Eva"), "resposta": "4", "valor_acertar": 5.000, "valor_errar": 500},

    {"pergunta": "Qual é o inseto que transmite a doença de Chagas??",
    "opcoes": ("1) Abelha", "2) Barata", "3) Barbeiro", "4) Pulga"), "resposta": "3", "valor_acertar": 10000, "valor_errar": 500},

    {"pergunta": "Quantos eram os anões da história “A branca de neve”?",
    "opcoes": ("1) Seis ", "2) Sete", "3) Oito", "4) Nove"), "resposta": "2", "valor_acertar": 20000, "valor_errar": 500},

    {"pergunta": "Qual é a capital dos Estados Unidos?",
    "opcoes": ("1) Nova York", "2) Miami", "3) Chicago", "4) Washington"), "resposta": "4", "valor_acertar": 30000, "valor_errar": 2000, "valor_parar": 4000},

    {"pergunta": "O que é um croissant??",
    "opcoes": ("1) Licor", "2) Doce", "3) Tempero", "4) Pão"), "resposta": "4", "valor_acertar": 40000},

    {"pergunta": "Quantos anos tem um milênio??",
    "opcoes": ("1) 100", "2) 500", "3) 1.000", "4) 10.000"), "resposta": "4", "valor_acertar": 50000},
    
    {"pergunta": "Um por todos e todos por um, é o grito de qual destes grupos? ", 
    "opcoes": ("1) Extraterrestres", "2) Família Robinson", "3) Power Rangers", "4) Três Mosqueteiros"),"resposta": "4", "valor_acertar": 100000},
    
    {"pergunta": "Qual destes órgãos não faz parte do sistema digestivo?",
    "opcoes": ("1) Brônquios", "2) Boca", "3) Faringe", "4) Intestino"), "resposta": "1", "valor_acertar": 200000},
    
    {"pergunta": "Nas religiões afro-brasileiras, quem é o Deus da Guerra??",
    "opcoes": ("1) Tupã", "2) OGum", "3) Senhor do Bonfim", "4) Zeus"), "resposta": "2", "valor_acertar": 300000},
    
    {"pergunta": "O que é andrômeda?",
    "opcoes": ("1) Bactéria", "2) Verdura", "3) Constelação", "4) Doença"), "resposta": "3", "valor_acertar": 400000},
     
    {"pergunta": "Quem fundou a Microsoft?",
    "opcoes": ("1) Sultão de Brunei", "2) Akio Morita", "3) Bill Gates", "4) Princípe Charles"), "resposta": "3", "valor_acertar": 500000},
    
    {"pergunta": "A pergunta do milhão: \nQual destes instrumentos musicais não possui teclado? ",
    "opcoes": ("1) Espineta", "2) Clavicórdio", "3) Eufônio", "4) Cravo"), "resposta": "3", "valor_acertar": 1000000}
    )