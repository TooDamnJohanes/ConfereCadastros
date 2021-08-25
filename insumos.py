#ESSA FUNÇÃO ABRE O ARQUIVO E ADICIONA OS VALORES NA LISTA DADOS
from classe_verifica import Verifica

def conferencia():
    #Abrir o arquivo
    nome_arquivo = "insumos.txt"
    dados = []
    correto = True
    target = 5
    nao_olhar = 1

    insumos = Verifica(dados, correto, nome_arquivo)
    insumos.encontra_caminho()
    insumos.verifica_campos(target)

    if(insumos.correto):
        insumos.verifica_entrada_nula()
        insumos.verifica_virgula_todo(nao_olhar)
        insumos.verifica_caractere(nao_olhar)
        insumos.verifica_duplicados()

    insumos.esta_correto()

if(__name__ == "__main__"):
    conferencia()



