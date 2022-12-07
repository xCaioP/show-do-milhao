import os


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def colocar_linha():
    print("-" * 40)


def introducao():
    colocar_linha()
    print("Show do Milhão\n")
    print("Seja bem-vindo(a)!", "\n")
    colocar_linha()
    print("\nSerá que você consegue ganhar o prêmio máximo de 1 MILHÃO DE REAIS??????")
    print("As perguntas vão aumentando de dificuldade de acordo com o progresso", "\n")
    colocar_linha()
    print("\nEstão preparados? ", "\n")
    input("\nPressione ENTER para iniciar")
    limpar_tela()


def mostrar_valor_proxima_pergunta(valor_acertar):
    print('Proxima pergunta vale: {} reais\n' .format(valor_acertar))
    colocar_linha()


def mostrar_valor_parar(valor_parar):
    colocar_linha()
    print("\nParar: {} reais" .format(valor_parar))


def mostrar_valor_pergunta(valor_acertar):
    print("Essa pergunta vale: {} reais ".format(valor_acertar))


def mostrar_valor_ao_terminar_jogo(valor_final):
    print('\nVocê recebeu {} reais \n' .format(valor_final))


def explicacao():
    print("Como funciona o jogo: \n")
    print("O jogo consiste em três rodadas e uma pergunta final: \n")
    print("* A primeira rodada contém 5 perguntas, cada uma valendo R$ 1000 cumulativos. ")
    print("* A segunda rodada contém 5 perguntas, cada uma valendo R$ 10 mil cumulativos. ")
    print("* A terceira rodada contém 5 perguntas, cada uma valendo R$ 100 mil reais cumulativos. ")
    print("* A última pergunta vale R$ 1 milhão.", "\n")
    global nome_jogador
    nome_jogador = input("Digite seu nome para começar: ")
    limpar_tela()


def contador_perguntas(numero_pergunta):
    print("Pergunta: {} de {} \n" .format(numero_pergunta, len(dados)))


dados = (
    {"pergunta": "Que personagem do folclore brasileiro tem uma perna só? ",
     "opcoes": ("A) Cuca ", "B) Curupira", "C) Boitatá", "D) Saci-pererê"),
     "resposta": 4, "valor_acertar": 1000},

    {"pergunta": "Qual animal da fauna brasileira está retratado na nota de dez reais?",
     "opcoes": ("A) Jabuti", "B) Onça", "C) Arara", "D) Tucano"),
     "resposta": 3, "valor_acertar": 2000, "valor_parar": 1000, "valor_errar": 500},

    {"pergunta": "Qual a matéria-prima do ketchup?",
     "opcoes": ("A) Abacate", "B) Tomate", "C) Cereja", "D) Pessego"),
     "resposta": 2, "valor_acertar": 3000, "valor_parar": 2000, "valor_errar": 1000},

    {"pergunta": "Qual é a maior floresta do planeta? ",
     "opcoes": ("1) Amazônica", "2) De Sherwood", "3) Da Tijuca", "4) Negra"),
     "resposta": 1, "valor_acertar": 4000, "valor_parar": 3000, "valor_errar": 1500},

    {"pergunta": "Qual casal foi expulso do Paraíso?",
     "opcoes": ("1) Sansão e Dalila", "2) José e Maria", "3) Sara e Abraão", "4) Adão e Eva"),
     "resposta": 4, "valor_acertar": 5000, "valor_parar": 4000, "valor_errar": 2000},

    {"pergunta": "Qual é o inseto que transmite a doença de Chagas??",
     "opcoes": ("1) Abelha", "2) Barata", "3) Barbeiro", "4) Pulga"),
     "resposta": 3, "valor_acertar": 10000, "valor_parar": 5000, "valor_errar": 2500},

    {"pergunta": "Quantos eram os anões da história “A branca de neve”?",
     "opcoes": ("A) Seis ", "B) Sete", "C) Oito", "D) Nove"),
     "resposta": 2, "valor_acertar": 20000, "valor_parar": 10000, "valor_errar": 5000},

    {"pergunta": "Qual é a capital dos Estados Unidos?",
     "opcoes": ("A) Nova York", "B) Miami", "C) Chicago", "D) Washington"),
     "resposta": 4, "valor_acertar": 30000, "valor_parar": 20000, "valor_errar": 10000},

    {"pergunta": "O que é um croissant??",
     "opcoes": ("A) Licor", "B) Doce", "C) Tempero", "D) Pão"),
     "resposta": 4, "valor_acertar": 40000, "valor_parar": 30000, "valor_errar": 15000},

    {"pergunta": "Quantos anos tem um milênio??",
     "opcoes": ("A) 100", "B) 500", "C) 1.000", "D) 10.000"),
     "resposta": 3, "valor_acertar": 50000, "valor_parar": 40000, "valor_errar": 20000},

    {"pergunta": "Um por todos e todos por um, é o grito de qual destes grupos? ",
     "opcoes": ("A) Extraterrestres", "B) Família Robinson", "C) Power Rangers", "D) Três Mosqueteiros"),
     "resposta": 4, "valor_acertar": 100000, "valor_parar": 50000, "valor_errar": 25000},

    {"pergunta": "Qual destes órgãos não faz parte do sistema digestivo?",
     "opcoes": ("A) Brônquios", "B) Boca", "C) Faringe", "D) Intestino"),
     "resposta": 1, "valor_acertar": 200000, "valor_parar": 100000, "valor_errar": 50000},

    {"pergunta": "Nas religiões afro-brasileiras, quem é o Deus da Guerra??",
     "opcoes": ("A) Tupã", "B) OGum", "C) Senhor do Bonfim", "D) Zeus"),
     "resposta": 2, "valor_acertar": 300000, "valor_parar": 200000, "valor_errar": 100000},

    {"pergunta": "O que é andrômeda?",
     "opcoes": ("A) Bactéria", "B) Verdura", "C) Constelação", "D) Doença"),
     "resposta": 3, "valor_acertar": 400000, "valor_parar": 300000, "valor_errar": 150000},

    {"pergunta": "Quem fundou a Microsoft?",
     "opcoes": ("A) Sultão de Brunei", "B) Steve Jobs", "C) Bill Gates", "D) Princípe Charles"),
     "resposta": 3, "valor_acertar": 500000, "valor_parar": 400000, "valor_errar": 200000},

    {"pergunta": "A pergunta do milhão: \nQual destes instrumentos musicais não possui teclado? ",
     "opcoes": ("A) Espineta", "B) Clavicórdio", "C) Eufônio", "D) Cravo"),
     "resposta": 3, "valor_acertar": 1000000, "valor_parar": 500000}
)
