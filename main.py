"""
Desenvolvido por Caio Ponte

"""

import functions

saldo_jogador = 0

functions.introducao()
functions.explicacao()

for indice, dado in enumerate(functions.dados):
    if indice != 0:
        functions.mostrar_valor_parar(saldo_jogador)
        functions.mostrar_valor_proxima_pergunta(dado["valor_acertar"])
        deseja_continuar = ""

        while (deseja_continuar.upper() != "S" and deseja_continuar.upper() != "N"):
            deseja_continuar = input(
                '\nDeseja continuar?\n\nS para SIM - N para NÃO:  ')
        functions.limpar_tela()
    else:
        deseja_continuar = "S"

    if deseja_continuar.upper() == "S":
        functions.colocar_linha()
        functions.mostrar_valor_pergunta(dado["valor_acertar"])
        functions.colocar_linha()
        functions.contador_perguntas(indice + 1)
        print(dado["pergunta"], "\n")

        for opcao in dado["opcoes"]:
            print(opcao)

        resposta_jogador = 0

        while (resposta_jogador != "A" and resposta_jogador != "B" and resposta_jogador != "C" and resposta_jogador != "D"):
            resposta_jogador = str(
                input('\nEscolha uma opção [A, B, C, D]: ')) .upper()

        if resposta_jogador == dado["resposta"]:
            functions.colocar_linha()
            print("\n\033[32mCerta Reposta!!! \033[0;0m\n")
            saldo_jogador = dado["valor_acertar"]
        else:
            if "valor_errar" not in dado:
                saldo_jogador = 0
            else:
                saldo_jogador = dado["valor_errar"]

            print("\n\033[31mQue pena! Você errou!\033[0;0m\n")
            print("O jogo acabou,", functions.nome_jogador)
            functions.mostrar_valor_ao_terminar_jogo(saldo_jogador)

            break
    else:
        print("Jogo finalizado,", functions.nome_jogador)
        functions.mostrar_valor_ao_terminar_jogo(dado["valor_parar"])

        break

if saldo_jogador == 1000000:
    print("\033[1;93m *" * 40)
    print("VOCÊ VENCEU O JOGO")
    print("VOCÊ GANHOU 1 MILHÃO DE REAISSSSSSSSSSS")
    print("PARABÉNS,", functions.nome_jogador,
          "VOCÊ CONSEGUIU O PRÊMIO MÁXIMO")
    print("\033[1;93m *" * 40)
