#ESSA FUNÇÃO ABRE O ARQUIVO E ADICIONA OS VALORES NA LISTA DADOS
from classe_verifica import Verifica

def conferencia():
    #Abrir o arquivo
    nome_arquivo = "local_de_descarregamento.txt"
    dados = []
    correto = True
    target = 2

    local_de_descarregamento = Verifica(dados, correto, nome_arquivo)
    local_de_descarregamento.encontra_caminho()
    local_de_descarregamento.verifica_campos(target)

    if(local_de_descarregamento.correto):
        local_de_descarregamento.verifica_entrada_nula()
        local_de_descarregamento.verifica_virgula_todo()
        local_de_descarregamento.verifica_duplicados()

    local_de_descarregamento.esta_correto()

if(__name__ == "__main__"):
    conferencia()



