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
    
    