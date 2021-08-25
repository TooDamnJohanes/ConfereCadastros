#ESSA FUNÇÃO ABRE O ARQUIVO E ADICIONA OS VALORES NA LISTA DADOS
from classe_verifica import Verifica

def conferencia():
    #Abrir o arquivo
    nome_arquivo = "C_FASE.txt"
    dados = []
    correto = True

    c_fase = Verifica(dados, correto, nome_arquivo)
    c_fase.encontra_caminho()

    c_fase.verifica_entrada_nao_nula()

    c_fase.esta_correto()

if(__name__ == "__main__"):
    conferencia()



