import functions

functions.introducao()

saldoJogador = 0
dados = (
    {"pergunta": "Que personagem do folclore brasileiro tem uma perna só?", "opcoes": ("A = Cuca ", "B = Curupira", "C = Boitatá", "D = Saci-pererê"), "resposta": "D", "valorAcertar": 1000},
    {"pergunta": "Qual animal da fauna brasileira está retratado na nota de dez reais?", "opcoes": (
        "Jabuti", "Onça", "Arara", "Tucano"), "resposta": "C", "valorAcertar": 3000, "valorErrar": 1000, "valorParar": 2000},
    {"pergunta": "Qual é a capital dos Estados Unidos?", "opcoes": (
        "Nova York", "Miami", "Chicago", "Washington"), "resposta": "D", "valorAcertar": 5000, "valorErrar": 2000, "valorParar": 4000},
    {"pergunta": "Qual a matéria-prima do ketchup?",
        "opcoes": ("Abacate", "Tomate", "Cereja", "Pessego"), "resposta": "B", "valorAcertar": 20000, "valorErrar": 5000, "valorParar": 4000},
    {"pergunta": "Quem descobriu o Brasil?", "opcoes": (
        "Pedro A", "Rodolfo", "Adriel", "Joao"), "resposta": "C", "valorAcertar": 10000, "valorErrar": 500},
    {"pergunta": "Quem descobriu o Brasil?", "opcoes": (
        "Pedro A", "Rodolfo", "Adriel", "Joao"), "resposta": "A", "valorAcertar": 50000, "valorErrar": 500},
    {"pergunta": "Quem descobriu o Brasil?", "opcoes": (
        "Pedro A", "Rodolfo", "Adriel", "Joao"), "resposta": "D", "valorAcertar": 100000, "valorErrar": 500},
    {"pergunta": "Quem descobriu o Brasil?", "opcoes": (
        "Pedro A", "Rodolfo", "Adriel", "Joao"), "resposta": "A", "valorAcertar": 150000, "valorErrar": 500},
    {"pergunta": "Quem descobriu o Brasil?", "opcoes": (
        "Pedro A", "Rodolfo", "Adriel", "Joao"), "resposta": "B", "valorAcertar": 1000000},
    {"pergunta": "Quem descobriu o Brasil?", "opcoes": (
        "Pedro A", "Rodolfo", "Adriel", "Joao"), "resposta": "C", "valorAcertar": 1000000},
    {"pergunta": "Quem descobriu o Brasil?", "opcoes": (
        "Pedro A", "Rodolfo", "Adriel", "Joao"), "resposta": "B", "valorAcertar": 1000000, "valorErrar": 5000, "valorParar": 500000}
)

for indice, dado in enumerate(dados):
    if indice != 0:
        functions.mostrarValorParar(saldoJogador)
        functions.mostrarValorProximaPergunta(dado["valorAcertar"])
        desejaContinuar = input("Deseja continuar? [S/N]")
        functions.limparTela()
    else:
        desejaContinuar = "S"

    if desejaContinuar.upper() == "S":
        functions.colocarLinha()
        functions.mostrarValorPergunta(dado["valorAcertar"])
        functions.colocarLinha()
        print(dado["pergunta"], "\n")
        for opcao in dado["opcoes"]:
            print(opcao)
        respostaJogador = input("\nEscolha uma opção [A,B,C,D]: ")
        if respostaJogador.upper() == dado["resposta"]:
            print("\nReposta correta!")
            saldoJogador = dado["valorAcertar"]
        else:
            if "valorErrar" not in dado:
                saldoJogador = 0
            else:
                saldoJogador = dado["valorErrar"]

            print("\nReposta errada")
            print("O jogo acabou")
            functions.mostrarValorAoTerminarJogo(saldoJogador)
            break
    else:
        print("Jogo finalizado")
        functions.mostrarValorAoTerminarJogo(dado["valorParar"])

        break
    
if saldoJogador == 1000000:
    print("Você venceu o jogo!")
    print("Você é novo m")