from personagem import Personagem
import json
from heroi import Heroi
from vilao import Vilao
import sys
import os
import time
import random
import pyfiglet

with open(r"herois.json", "r", encoding="utf-8") as arquivo:
    
    # quando usa json.load o arquivo json é transformado em dicionário python
    """
    o objetivo dessa parte do código é abrir o arquivo json e salvar os dicionários em python,facilitando a manipulação
    """
    arquivo_lido = json.load(arquivo)
    dados_vida = arquivo_lido["vida"]
    dados_dano = arquivo_lido["dano"]
    dados_especial = arquivo_lido["especial"]
    dados_arma = arquivo_lido["arma"]


with open(r"viloes.json", "r", encoding="utf-8") as arquivo:
    
    # quando usa json.load o arquivo json é transformado em dicionário python
    """
    o objetivo dessa parte do código é abrir o arquivo json e salvar os dicionários em python,facilitando a manipulação
    """
    arquivo_lido_vilao = json.load(arquivo)
    dados_vida_vilao = arquivo_lido_vilao["vida"]
    dados_dano_vilao = arquivo_lido_vilao["dano"]
    dados_arma_vilao = arquivo_lido_vilao["arma"]



def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_sair_ou_voltar():
    limpar_tela()
    print("\n╔════════════════════════════════════════════════════╗")
    print("║              ❓ O QUE DESEJA FAZER AGORA? ❓         ║")
    print("║      Escolha uma das opções abaixo para continuar  ║")
    print("╠════════════════════════════════════════════════════╣")
    print("║ 1. Voltar para a tela inicial 🔄                  ║")
    print("║ 2. Sair do sistema 🚪                              ║")
    print("╚════════════════════════════════════════════════════╝")

    tentativas = 3
    while tentativas != 0:
        opcao = input("Digite o número da opção desejada: ").strip()

        if opcao == "1":
            print("\n🔄 Retornando à tela inicial...")
            tela_inicial()  # Substitua pelo nome real da sua função principal
            break

        elif opcao == "2":
            print("\n📢 Sistema encerrado pelo usuário. Até logo!")
            sys.exit()

        else:
            tentativas -= 1
            print("❌ Opção inválida. Por favor, escolha entre 1 ou 2.")
            print(f"🔁 Tentativas restantes: {tentativas}")

    else:
        print("\n⚠️ Limite de tentativas atingido. Sistema encerrado automaticamente.")
        sys.exit()


def tela_inicial():
    limpar_tela()
    print("\n╔════════════════════════════════════════════════════╗")
    print("║          🔥⚔️  BEM-VINDO AO  BATTLE PY  ⚔️🔥         ║")
    print("║         🌟 Heróis e Vilões em Confronto Épico 🌟     ║")
    print("╠════════════════════════════════════════════════════╣")
    print("║ O que você deseja fazer agora?                    ║")
    print("║                                                  ║")
    print("║ 1. Jogar 🎮                                       ║")
    print("║ 2. Ver personagens 📜                             ║")
    print("║ 3. Cadastrar personagem 📝                         ║")
    print("║ 4. Sair 🚪                                        ║")
    print("╚════════════════════════════════════════════════════╝")

    tentativas = 3  
    while tentativas != 0:
        opcao = input("Digite o número da opção desejada: ").strip()
        if opcao == "1":
            print("\n🎮 Iniciando o jogo...")
            Game.escolher_heroi()
            return
            break

        elif opcao == "2":
            ShowCharacter.ver_atributos_personagens()
            return
            break

        elif opcao == "3":
            print("\n📝 Cadastro de novo personagem...")
            NewCharacter.cadastrar_novo_personagem()
            return
            break

        elif opcao == "4":
            print("\n📢 Sistema encerrado pelo usuário. Até logo!")
            sys.exit()

        else:
            tentativas -= 1
            print("\n❌ Opção inválida. Por favor, escolha de 1 a 4.")
            print(f"🔁 Tentativas restantes: {tentativas}")

    else:
        print("\n⚠️ Limite de tentativas atingido. Sistema encerrado automaticamente.")
        sys.exit()






class NewCharacter:
    @staticmethod
    def cadastrar_novo_personagem():
        limpar_tela()
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
                tela_inicial()
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
        limpar_tela()
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

        limpar_tela()
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



class Game:
    

    @staticmethod
    def escolher_heroi():
        limpar_tela()
        import json
        with open("herois.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        dados_vida = dados["vida"]
        

        #Esse loop percorrerá cada chave do dicionário vida
        print("\n╔══════════════════════ FICHAS DOS PERSONAGENS ══════════════════════╗")
        for nome in dados_vida:
            print("╠════════════════════════════════════════════════════════════════════╣")
            print(f"║Herói: {nome}")
            print("╚════════════════════════════════════════════════════════════════════╝\n")

        tentativas=3
        while tentativas>0:
            heroi_escolhido=input("Digite o nome do seu herói(Preste atenção na grafia):")
            
            if heroi_escolhido in dados_vida:
                Game.escolher_vilao(heroi_escolhido)
                return
            else:
                print("Tentativa inválida")
                print(f"Tentativas restantes {tentativas}")
                tentativas-=1
        else:
            print("Número de tentativas atingido.")
            print("Fechando o Battlepy")
            sys.exit()


    @staticmethod
    def escolher_vilao(heroi_escolhido):
        print("Sorteando seu inimigo...")
        for i in range(1, 11):
            blocos = "■" * i
            espacos = "□" * (10 - i)
            porcentagem = i * 10
            sys.stdout.write(f"\r[{blocos}{espacos}] {porcentagem}%")
            sys.stdout.flush()
            time.sleep(0.3)  # tempo entre cada etapa
        lista_possiveis_viloes=[]
        for viloes in dados_vida_vilao:
            lista_possiveis_viloes.append(viloes)

        vilao_escolhido=random.choice(lista_possiveis_viloes)
        print()
        print(f"Seu oponente será {vilao_escolhido}")
        Game.comecar_batalha(heroi_escolhido,vilao_escolhido)
        pass

    def comecar_batalha(heroi_escolhido,vilao_escolhido):
        nome_heroi=heroi_escolhido
        vida_heroi=dados_vida[heroi_escolhido]
        dano_heroi=dados_dano[heroi_escolhido]
        arma_heroi=dados_arma[heroi_escolhido]
        especial_heroi=dados_especial[heroi_escolhido]
        player=Jogador(nome_heroi,vida_heroi,dano_heroi,arma_heroi,especial_heroi)
        
        

        vida_vilao=dados_vida_vilao[vilao_escolhido]
        dano_vilao=dados_dano_vilao[vilao_escolhido]
        arma_vilao=dados_arma_vilao[vilao_escolhido]
        adversario=Inimigo(vilao_escolhido,vida_vilao,dano_vilao,arma_vilao)



        print("\n╔════════════════════════════════════════════════════╗")
        print("║                ⚔️ ESCOLHA SUA AÇÃO DE BATALHA ⚔️     ║")
        print("║     Tome uma decisão estratégica para vencer o jogo ║")
        print("╠════════════════════════════════════════════════════╣")
        print("║ 1. Atacar 💥                                      ║")
        print("║ 2. Defender 🛡️                                    ║")
        print("║ 3. Recuar 🔙                                       ║")
        print("║ 4. Encerrar Jogo ❌                               ║")
        print("╚════════════════════════════════════════════════════╝")
        while vida_heroi>0 and vida_vilao>0:
            
            jogada=int(input("Escolha sua próxima jogada:"))
            possiveis_jogadas_inimigo=[1,2,3]
            jogada_vilao=random.choice(possiveis_jogadas_inimigo)

            if jogada==1:
                if jogada==jogada_vilao:
                    print("JOGADA=Ambos atacaram ao mesmo tempo,então receberam dano de 20.")
                    vida_heroi-=20
                    vida_vilao-=20
                    player.diminuir_vida(20)
                    adversario.diminuir_vida(20)
                    print(f"Vida Herói={vida_heroi}")
                    print(f"Vida Vilão={vida_vilao}")
                    print()

                elif jogada_vilao==2:
                    vida_vilao-=dano_heroi/2
                    player.atacar_inimigo(vilao_escolhido)
                    #Se o você atacou e o adversário defendeu,ele recebe um buff de dano e só perde metade do dano que causaria
                    adversario.diminuir_vida(dano_heroi/2)
                    adversario.aumentar_dano(10)
                    print(f"Vida Herói={vida_heroi}")
                    print(f"Vida Vilão={vida_vilao}")
                    print()
                
                elif jogada_vilao==3:
                    player.ataque_errado(vilao_escolhido)
                    #caso o adversário desvie caso após um ataque errado do player,receberá um buff de dano
                    adversario.aumentar_dano(5)
                    print(f"Vida Herói={vida_heroi}")
                    print(f"Vida Vilão={vida_vilao}")
                    print()
                    
                pass

            elif jogada==2:
                if jogada==jogada_vilao:
                    print("JOGADA=Ambos defenderam ao mesmo tempo.Nada acontece.")
                    print()
                elif jogada_vilao==1:
                    vida_heroi-=dano_vilao/2
                    adversario.atacar_inimigo(nome_heroi)
                    #Se você defendeu e o adversário atacou,recebe apenas metade do dano que deveria receber e aumenta o dano
                    player.diminuir_vida(dano_vilao/2)
                    player.aumentar_dano(10)
                    print(f"Vida Herói={vida_heroi}")
                    print(f"Vida Vilão={vida_vilao}")
                    print()

                   
                elif jogada_vilao==3:
                    print("JOGADA=Ambos tiveram postura defensiva.Vilão perde 5 de vida por gasto de estamina")
                    #caso ambos tiverem postura defensiva,aquele que escolher defender invés de recuar,não tomará uma 
                    #"punição" no dano por gasto de estamina
                    adversario.diminuir_vida(5)
                    vida_vilao-=5
                    print(f"Vida Herói={vida_heroi}")
                    print(f"Vida Vilão={vida_vilao}")
                    print()

                    pass
                
                pass

            elif jogada==3:
                if jogada==jogada_vilao:
                    print("JOGADA=Ambos recuaram.Nada acontece.")
                elif jogada_vilao==1:
                    #Caso o player recue quando o adversário errar o ataque,receberá um buff de dano
                    adversario.ataque_errado(nome_heroi)
                    player.aumentar_dano(5)
                    
                elif jogada_vilao==2:
                    print("JOGADA=Ambos tiveram postura defensiva.Herói perde 5 de vida por gasto de estamina")
                    player.diminuir_vida(5)
                    vida_heroi-=5
                    print(f"Vida Herói={vida_heroi}")
                    print(f"Vida Vilão={vida_vilao}")


        else:
            if vida_heroi<=0:
                player.morte()
                
            elif vida_vilao<=0:
                adversario.morte()
                pass
            else:
                banner_empate = pyfiglet.figlet_format("EMPATE")
                print(banner_empate)
            
            time.sleep(5)

            print("\n╔════════════════════════════════════════════════════╗")
            print("║             🔄 O QUE DESEJA FAZER AGORA?           ║")
            print("║    Escolha uma das opções abaixo para continuar    ║")
            print("╠════════════════════════════════════════════════════╣")
            print("║ 1. Voltar para a tela inicial 🏠                   ║")
            print("║ 2. Sair do sistema 🚪                              ║")
            print("╚════════════════════════════════════════════════════╝")

            tentativas = 3
            while tentativas != 0:
        

                escolha = input("Digite o número da opção desejada: ").strip()

                if escolha == "1":
                    print("\n🔁 Retornando à tela inicial...")
                    tela_inicial()  # Certifique-se de que esta função está definida
                    break
                elif escolha == "2":
                    print("\n👋 Encerrando o sistema... Até logo!")
                    sys.exit()
                else:
                    tentativas -= 1
                    print("\n❌ Opção inválida. Escolha entre 1 e 2.")
                    print(f"🔁 Tentativas restantes: {tentativas}")

            else:
                print("\n⚠️ Limite de tentativas atingido. Encerrando o sistema automaticamente.")
                sys.exit()


            
      

    
class Jogador:
    def __init__(self,nome,vida,dano,arma,especial):
        self.nome=nome
        self.vida=vida
        self.dano=dano
        self.arma=arma
        self.especial=especial

    def diminuir_vida(self,dano_inimigo):
        self.vida-=dano_inimigo
        
    
    def atacar_inimigo(self,nome_inimigo):
        print(f"JOGADA={self.nome} atacou com {self.arma} o {nome_inimigo}")

    def ataque_errado(self,nome_inimigo):
        print(f"JOGADA={self.nome} atacou,mas {nome_inimigo} desviou")

    def aumentar_dano(self,aumento):
        self.dano+=aumento

    def morte(self):
        banner_derrota = pyfiglet.figlet_format("DERROTA")
        print(banner_derrota)
        

        



class Inimigo():
    def __init__(self,nome,vida,dano,arma):
        self.nome=nome
        self.vida=vida
        self.dano=dano
        self.arma=arma
    def diminuir_vida(self,dano_inimigo):
        self.vida-=dano_inimigo
        
    
    def atacar_inimigo(self,nome_inimigo):
        print(f"JOGADA={self.nome} atacou com {self.arma} o {nome_inimigo}")

    def ataque_errado(self,nome_inimigo):
        print(f"JOGADA={self.nome} atacou,mas {nome_inimigo} desvio")


    def aumentar_dano(self,aumento):
        self.dano+=aumento

    def morte(self): 
        banner_vitoria = pyfiglet.figlet_format("WIN")
        print(banner_vitoria)
    
    






tela_inicial()












   
