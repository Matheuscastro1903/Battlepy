

from heroi import Heroi
from vilao import Vilao
import sys



class ShowCharacter:
   
    @staticmethod
    def ver_atributos_personagens():
        limpar_tela()
        print("\n╔════════════════════════════════════════════════════╗")
        print("║            📜 MENU DE ATRIBUTOS DOS PERSONAGENS    ║")
        print("║     Escolha qual grupo de personagens deseja ver   ║")
        print("╠════════════════════════════════════════════════════╣")
        print("║ 1. Ver Heróis 👼                                   ║")
        print("║ 2. Ver Vilões 😈                                   ║")
        print("║ 3. Voltar ao menu anterior 🔙                      ║")
        print("╚════════════════════════════════════════════════════╝")

        tentativas = 3
        while tentativas != 0:
            opcao = input("Digite o número da opção desejada: ").strip()

            if opcao == "1":
                print("\n👼 Atributos dos Heróis:\n")
                ShowCharacter.mostrar_atributos_herois()
                
                break

            elif opcao == "2":
                print("\n😈 Atributos dos Vilões:\n")
                ShowCharacter.mostrar_atributos_viloes()
                break

            elif opcao == "3":
                print("\n🔙 Retornando ao menu principal...")
                tela_inicial()
                break

            else:
                tentativas -= 1
                print("\n❌ Opção inválida. Por favor, escolha de 1 a 3.")
                print(f"🔁 Tentativas restantes: {tentativas}")

        else:
            print("\n⚠️ Limite de tentativas atingido. Sistema encerrado automaticamente.")
            sys.exit()


        pass
        

    @staticmethod
    def mostrar_atributos_herois():
        import json
        with open("herois.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        vida = dados["vida"]
        dano = dados["dano"]
        especial = dados["especial"]
        arma = dados["arma"]

        #Esse loop percorrerá cada chave do dicionário vida
        print("\n╔══════════════════════ FICHAS DOS PERSONAGENS ══════════════════════╗")
        for nome in vida:
            print("╠════════════════════════════════════════════════════════════════════╣")
            print(f"║ 🧝 Nome: {nome}")
            print(f"║ ❤️ Vida: {vida[nome]}")
            print(f"║ 💥 Dano: {dano[nome]}")
            print(f"║ ✨ Especial: {especial[nome]}")
            print(f"║ 🗡️ Arma: {arma[nome]}")
            print("╚════════════════════════════════════════════════════════════════════╝\n")

        while True:
            tecla=input("Pressione espaço '1' para voltar para tela anterior:")
            if tecla=="1":
                ShowCharacter.ver_atributos_personagens()
                break



        pass
    
    
    @staticmethod
    def mostrar_atributos_viloes():
        import json
        with open("viloes.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        vida = dados["vida"]
        dano = dados["dano"]
        maldade = dados["maldade"]
        arma = dados["arma"]

        #Esse loop percorrerá cada chave do dicionário vida
        print("\n╔══════════════════════ FICHAS DOS PERSONAGENS ══════════════════════╗")
        for nome in vida:
            print("╠════════════════════════════════════════════════════════════════════╣")
            print(f"║ 🧝 Nome: {nome}")
            print(f"║ ❤️ Vida: {vida[nome]}")
            print(f"║ 💥 Dano: {dano[nome]}")
            print(f"║ ✨ Especial: {maldade[nome]}")
            print(f"║ 🗡️ Arma: {arma[nome]}")
            print("╚════════════════════════════════════════════════════════════════════╝\n")

        while True:
                tecla=input("Pressione espaço '1' para voltar para tela anterior:")
                if tecla=="1":
                    ShowCharacter.ver_atributos_personagens()
                    break

        pass

