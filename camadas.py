#ESSA FUNÇÃO ABRE O ARQUIVO E ADICIONA OS VALORES NA LISTA DADOS
from classe_verifica import Verifica

def conferencia():
    # Abrir o arquivo
    nome_arquivo = "camada.txt"
    dados = []
    correto = True
    target = 2
    nao_olhar = 1
    camada = Verifica(dados, correto, nome_arquivo)

    camada.encontra_caminho()

    if(camada.correto):
        camada.verifica_campos(target)
        camada.verifica_entrada_nula()
        camada.verifica_virgula_todo(nao_olhar)
        camada.verifica_caractere(nao_olhar)
        camada.verifica_duplicados()

    camada.esta_correto()

if(__name__ == "__main__"):
    conferencia()



