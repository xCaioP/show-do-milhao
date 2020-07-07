import os


def limparTela():
    """
    Essa função limpa a tela no cmd, usando o módulo os.
    return: None
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def colocarLinha(quantidade=30):
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
    colocarLinha()
    print("\nBaseado na primeira versão", "\n")
    colocarLinha()
    print("\nShow do Milhão")
    print("Sejam muito bem-vindos!", "\n")
    colocarLinha()
    print("\nPreparados para uma diversão?")
    print("Vamos começar com perguntas bem fáceis e depois vamos dificultar um pouco :)")
    print("Estão preparados? ", "\n")
    colocarLinha()
    input("\nPressione ENTER para iniciar")
    limparTela()


def mostrarValorProximaPergunta(valorAcertar):
    """
    Essa função serve para mostrar o valor da proxima pergunta.
    param: valorAcertar: double
    return: None
    """
    print("Proxima pergunta: ", valorAcertar)


def mostrarValorParar(valorParar):
    """
    Essa função serve para mostrar o valor caso o jogador queira parar, e a cada pergunta esse valor muda ou altera.
    param: valorParar: double
    return: None
    """
    print("Parar: ", valorParar)


def mostrarValorPergunta(valorAcertar):
    """
    Essa função mostra ao usuário o valor da pergunta atual.
    param: valorAcertar: double
    return: None
    """
    print("Valor da pergunta atual: ", valorAcertar)


def mostrarValorAoTerminarJogo(valorFinal):
    """
    Essa função mostra o valor final recebido pelo usuário.
    param: valorFinal: double
    return: None
    """
    print("Você voltará com: ", valorFinal)

dados = (
    {"pergunta": "Primeira pergunta: \nQue personagem do folclore brasileiro tem uma perna só?",
     "opcoes": ("A) Cuca ", "B = Curupira", "C = Boitatá", "D = Saci-pererê"), "resposta": "D", "valorAcertar": 1000},

    {"pergunta": "Qual animal da fauna brasileira está retratado na nota de dez reais?", 
    "opcoes": ("Jabuti", "Onça", "Arara", "Tucano"), "resposta": "C", "valorAcertar": 3000, "valorErrar": 1000, "valorParar": 2000},

    {"pergunta": "Qual é a capital dos Estados Unidos?", 
    "opcoes": ("Nova York", "Miami", "Chicago", "Washington"), "resposta": "D", "valorAcertar": 5000, "valorErrar": 2000, "valorParar": 4000},

    {"pergunta": "Qual a matéria-prima do ketchup?",
    "opcoes": ("Abacate", "Tomate", "Cereja", "Pessego"), "resposta": "B", "valorAcertar": 20000, "valorErrar": 5000, "valorParar": 4000},

    {"pergunta": "Quem descobriu o Brasil?", 
    "opcoes": ("Pedro A", "Rodolfo", "Adriel", "Joao"), "resposta": "C", "valorAcertar": 10000, "valorErrar": 500},
    
    {"pergunta": "Quem descobriu o Brasil?", 
    "opcoes": ("Pedro A", "Rodolfo", "Adriel", "Joao"), "resposta": "A", "valorAcertar": 50000, "valorErrar": 500},
   
    {"pergunta": "Quem descobriu o Brasil?", 
    "opcoes": ("Pedro A", "Rodolfo", "Adriel", "Joao"), "resposta": "D", "valorAcertar": 100000, "valorErrar": 500},
  
    {"pergunta": "Quem descobriu o Brasil?", 
    "opcoes": ("Pedro A", "Rodolfo", "Adriel", "Joao"), "resposta": "A", "valorAcertar": 150000, "valorErrar": 500},
   
    {"pergunta": "Quem descobriu o Brasil?", 
    "opcoes": ("Pedro A", "Rodolfo", "Adriel", "Joao"), "resposta": "B", "valorAcertar": 1000000},
   
    {"pergunta": "Quem descobriu o Brasil?", 
    "opcoes": ("Pedro A", "Rodolfo", "Adriel", "Joao"), "resposta": "C", "valorAcertar": 1000000},
   
    {"pergunta": "Quem descobriu o Brasil?", 
    "opcoes": ("Pedro A", "Rodolfo", "Adriel", "Joao"), "resposta": "B", "valorAcertar": 1000000, "valorErrar": 5000, "valorParar": 500000}
)