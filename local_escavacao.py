#ESSA FUNÇÃO ABRE O ARQUIVO E ADICIONA OS VALORES NA LISTA DADOS
from classe_verifica import Verifica

def conferencia():
    #Abrir o arquivo
    nome_arquivo = "local_escavacao.txt"
    dados = []
    correto = True
    target = 2

    local_escavacao = Verifica(dados, correto, nome_arquivo)
    local_escavacao.encontra_caminho()
    local_escavacao.verifica_campos(target)

    if(local_escavacao.correto):
        local_escavacao.verifica_entrada_nula()
        local_escavacao.verifica_virgula_todo()
        local_escavacao.verifica_duplicados()

    local_escavacao.esta_correto()

if(__name__ == "__main__"):
    conferencia()



