
from heroi import Heroi
from vilao import Vilao
import sys

import time



class NewCharacter:
    @staticmethod
    def cadastrar_novo_personagem():
        print("\n╔════════════════════════════════════════════════════╗")
        print("║            ✍️ MENU DE CADASTRO DE PERSONAGEM ✍️     ║")
        print("║     Escolha o tipo de personagem que deseja criar  ║")
        print("╠════════════════════════════════════════════════════╣")
        print("║ 1. Cadastrar Herói 👼                             ║")
        print("║ 2. Cadastrar Vilão 😈                             ║")
        print("║ 3. Voltar ao menu anterior 🔙                    ║")
        print("╚════════════════════════════════════════════════════╝")

        tentativas = 3 
        while tentativas != 0:
            opcao = input("Digite o número da opção desejada: ").strip()

            if opcao == "1":
                print("\n🦸 Cadastro de herói selecionado...")
                NewCharacter.cadastrar_heroi()
                break

            elif opcao == "2":
                print("\n🦹 Cadastro de vilão selecionado...")
                NewCharacter.cadastrar_vilao()
                break

            elif opcao == "3":
                print("\n🔙 Retornando ao menu principal...")
                
                break

            else:
                tentativas -= 1
                print("\n❌ Opção inválida. Por favor, escolha de 1 a 3.")
                print(f"🔁 Tentativas restantes: {tentativas}")

        else:
            print("\n⚠️ Limite de tentativas atingido. Sistema encerrado automaticamente.")
            sys.exit()

    @staticmethod
    def cadastrar_heroi():
        nome = input("Digite o nome do seu herói: ")

        tentativas1 = 3
        while tentativas1 != 0:
            vida = int(input("ATENÇÃO!! Valor da vida influencia diretamente no dano.\n"
                             "Digite o dano básico do seu personagem (200/300/400): "))
            if vida in [200, 300, 400]:
                break
            else:
                print("Tentativa inválida. Escolha entre (200/300/400):")
                print(f"Tentativas restantes: {tentativas1}")
                tentativas1 -= 1
        else:
            print("As suas tentativas acabaram. Fechando o sistema...")
            sys.exit()

        if vida == 400:
            dano = 20
        elif vida == 300:
            dano = 30
        elif vida == 200:
            dano = 50

        tentativas2 = 3
        while tentativas2 != 0:
            arma = input("ATENÇÃO!! A arma influencia diretamente no valor de velocidade.\n"
                         "Qual arma seu personagem utilizará (Espada, lança, Arco)? ").strip().lower()
            if arma in ["espada", "lança", "lanca", "arco"]:
                break
            else:
                print("Tentativa inválida. Escolha entre (Espada, lança, Arco):")
                print(f"Tentativas restantes: {tentativas2}")
                tentativas2 -= 1
        else:
            print("As suas tentativas acabaram. Fechando o sistema...")
            sys.exit()

        if arma == "lança" or arma == "lanca":
            dano_final = (dano + 50) * 2
        elif arma == "espada":
            dano_final = (dano + 30) * 3
        elif arma == "arco":
            dano_final = (dano + 20) * 5

        nome_arma = input("Digite o nome especial da arma (ex: BatEspada): ")

        dano = dano_final
        especial = dano * 2
        arma = nome_arma


        heroi_cadastrado = Heroi(nome, vida, dano, arma, especial)
        time.sleep(3)

        menu_sair_ou_voltar()

    @staticmethod
    def cadastrar_vilao():
        limpar_tela()
        nome = input("Digite o nome do seu vilão: ")

        tentativas1 = 3
        while tentativas1 != 0:
            vida = int(input("ATENÇÃO!! Valor da vida influencia diretamente no dano.\n"
                             "Digite a vida  do seu personagem (200/300/400): "))
            if vida in [200, 300, 400]:
                break
            else:
                print("Tentativa inválida. Escolha entre (200/300/400):")
                print(f"Tentativas restantes: {tentativas1}")
                tentativas1 -= 1
        else:
            print("As suas tentativas acabaram. Fechando o sistema...")
            sys.exit()

        if vida == 400:
            dano = 20
        elif vida == 300:
            dano = 30
        elif vida == 200:
            dano = 50

        tentativas2 = 3
        while tentativas2 != 0:
            arma = input("ATENÇÃO!! A arma influencia diretamente no valor de velocidade.\n"
                         "Qual arma seu personagem utilizará (Adaga/Machado/Besta)? ").strip().lower()
            if arma in ["adaga","machado","besta"]:
                break
            else:
                print("Tentativa inválida. Escolha entre (Espada, lança, Arco):")
                print(f"Tentativas restantes: {tentativas2}")
                tentativas2 -= 1
        else:
            print("As suas tentativas acabaram. Fechando o sistema...")
            sys.exit()

        if arma == "besta":
            dano_final = (dano + 50) * 2
        elif arma == "adaga":
            dano_final = (dano + 30) * 3
        elif arma == "machado":
            dano_final = (dano + 20) * 5

        nome_arma = input("Digite o nome especial da arma (ex: Espada Sombria): ")

        tentativas3=3
        while tentativas3 != 0:
            nivel_maldade = input("ATENÇÃO!! A maldade influencia diretamente no valor do dano e vida.\n"
                         "Qual nível de maldade do seu personagem(Baixa/Média/Alta)? ").strip().lower()
            if nivel_maldade in ["baixa", "baixo", "média", "médio","media","medio","alto","alta"]:
                break
            else:
                print("Tentativa inválida. Escolha entre (Baixa/Média/Alta):")
                print(f"Tentativas restantes: {tentativas2}")
                tentativas2 -= 1
        else:
            print("As suas tentativas acabaram. Fechando o sistema...")
            sys.exit()
        
        if nivel_maldade in ["baixo","baixa"]:
            vida+=20
        elif nivel_maldade in ["média", "médio","media","medio"]:
            vida+=10
            dano_final+=10
        elif  nivel_maldade in ["alto","alta"]:
            dano_final+=20


        dano = dano_final
        especial = dano * 2
        arma = nome_arma

        limpar_tela()
        vilao_cadastrado = Vilao(nome, vida, dano, arma, nivel_maldade)
        time.sleep(3)

        menu_sair_ou_voltar()
