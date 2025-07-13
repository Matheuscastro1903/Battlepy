from personagem import Personagem
import json


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
    






class Heroi(Personagem):
    """
    A classe Vilao representa as características de um vilão no jogo.
    Herda da classe Personagem.
    """
    def __init__(self, nome,vida,dano,arma,especial):
        super().__init__(nome,vida)
        self.dano=dano
        self.especial=especial
        self.arma=arma
        self.salvar_heroi()

    def salvar_heroi(self):
        dados_vida[self.nome] = self.vida
        dados_dano[self.nome] = self.dano
        dados_especial[self.nome] = self.especial
        dados_arma[self.nome] = self.arma
        

        # PARA ARQUIVO TIPO JSON É MELHOR USAR "w" pois qualquer errinho de formatação pode quebrar o sistema
        with open(r"herois.JSON", "w", encoding="utf-8") as arquivo:
            # Aqui, estamos criando um dicionário com duas chaves:
            json.dump({"vida": dados_vida, "dano": dados_dano, "especial": dados_especial, "arma": dados_arma,}, 
                      arquivo, indent=4, ensure_ascii=False)
        
        print("Herói cadastrado com sucesso.")
        