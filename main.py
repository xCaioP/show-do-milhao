import functions

functions.introducao()

saldoJogador = 0

for indice, dado in enumerate(functions.dados):
    if indice != 0:
        functions.mostrarValorParar(saldoJogador)
        functions.mostrarValorProximaPergunta(dado["valorAcertar"])
        desejaContinuar = input("\nDeseja continuar? [S/N]")
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