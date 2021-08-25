#ESSA FUNÇÃO ABRE O ARQUIVO E ADICIONA OS VALORES NA LISTA DADOS
from classe_verifica import Verifica

def conferencia():
    #encontra_caminho(dados)
    nome_arquivo = "paradaxtag.txt"
    nome_arquivo_parada = "operacoes_paradas.txt"
    dados = []
    dados2 = []
    correto = True
    target = 2

    verifica_parada = Verifica(dados2, correto, nome_arquivo_parada)
    verifica_parada.encontra_caminho()

    parada_x_tag = Verifica(dados, correto, nome_arquivo)
    parada_x_tag.encontra_caminho()
    parada_x_tag.verifica_campos(target)

    if(parada_x_tag.correto):
        parada_x_tag.verifica_vinculos(verifica_parada.dados, 0, "operacoes_paradas")
        parada_x_tag.verifica_virgula_todo()

    parada_x_tag.esta_correto()

if(__name__ == "__main__"):
    conferencia()



