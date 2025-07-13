from personagem import Personagem  # Importa a classe Personagem
import json
# Abrindo e carregando os dados do vilao.json no início do programa

with open(r"viloes.json", "r", encoding="utf-8") as arquivo:
    arquivo_lido_vilao = json.load(arquivo)
    dados_vida_vilao = arquivo_lido_vilao["vida"]
    dados_dano_vilao = arquivo_lido_vilao["dano"]
    dados_maldade_vilao = arquivo_lido_vilao["maldade"]
    dados_arma_vilao = arquivo_lido_vilao["arma"]


# Classe Vilao com herança da classe Personagem
class Vilao(Personagem):
    """
    A classe Vilao representa as características de um vilão no jogo.
    Herda da classe Personagem.
    """
    def __init__(self, nome, vida, dano, arma,nivel_maldade):
        super().__init__(nome, vida)
        self.dano = dano
        self.maldade = nivel_maldade
        self.arma = arma
        self.salvar_vilao()

    def salvar_vilao(self):
        dados_vida_vilao[self.nome] = self.vida
        dados_dano_vilao[self.nome] = self.dano
        dados_maldade_vilao[self.nome] = self.maldade
        dados_arma_vilao[self.nome] = self.arma

        # Salvando os dados no arquivo JSON
        with open(r"viloes.json", "w", encoding="utf-8") as arquivo:
            json.dump({
                "vida": dados_vida_vilao,
                "dano": dados_dano_vilao,
                "maldade": dados_maldade_vilao,
                "arma": dados_arma_vilao
            }, arquivo, indent=4, ensure_ascii=False)

        print("Vilão cadastrado com sucesso.")
