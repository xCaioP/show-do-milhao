import functions

saldoJogador = 0

functions.introducao()

print("\nUm resumo sobre o jogo : \n")
print("O jogo consiste em três rodadas e uma pergunta final: ")     
print("* A primeira contém 5 perguntas, cada uma valendo mil reais cumulativos. ")
print("* A segunda, de 5 perguntas valendo R$ 10 mil cumulativos cada. ")
print("* A terceira, de 5 perguntas de R$100 mil reais cumulativos cada. ")
print("* A última pergunta valea R$ 1 milhão.", "\n")
nome_jogador = input("Digite seu nome para começar: ")
functions.limpar_tela()

for indice, dado in enumerate(functions.dados):
    if indice != 0:
        functions.mostrar_valor_parar(saldoJogador)
        functions.mostrar_valor_proxima_pergunta(dado["valor_acertar"])
        desejaContinuar = input("\nDeseja continuar? [S/N] ")
        functions.limpar_tela()
    else:
        desejaContinuar = "S"

    if desejaContinuar.upper() == "S":
        functions.colocar_linha()
        functions.mostrar_valor_pergunta(dado["valor_acertar"]) 
        functions.colocar_linha()
        print(dado["pergunta"], "\n")
        for opcao in dado["opcoes"]:
            print(opcao)
        respostaJogador = input("\nEscolha uma opção [1,2,3,4]: ")
        if respostaJogador.upper() == dado["resposta"]:
            print("\nCerta Reposta!!!", "\n")
            saldoJogador = dado["valor_acertar"]
        else:
            if "valorErrar" not in dado:
                saldoJogador = 0
            else:
                saldoJogador = addo["valor_errar"]

            print("\nQue pena! Você errou!")
            print("O jogo acabou, ", nome_jogador)
            functions.mostrar_valor_ao_terminar_jogo(saldoJogador)
            break
    else:
        print("Jogo finalizado")
        functions.mostrar_valor_ao_terminar_jogo(dado["valor_parar"])

        break
    
if saldoJogador == 1000000:
    print("Você venceu o jogo!")
    print("VOCÊ GANHOU 1 MILHÃO DE REAIS")
    print("Parabéns ", nome_jogador, "você conseguiu prêmio máximo!!!")