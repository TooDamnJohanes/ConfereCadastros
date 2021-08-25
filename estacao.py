#ESSA FUNÇÃO ABRE O ARQUIVO E ADICIONA OS VALORES NA LISTA DADOS
from classe_verifica import Verifica

def conferencia():
    #Abrir o arquivo
    nome_arquivo = "ESTACAO.txt"
    dados = []
    correto = True
    target = 5
    nao_olhar = 4

    estacao = Verifica(dados, correto, nome_arquivo)
    estacao.encontra_caminho()
    estacao.verifica_campos(target)

    if(estacao.correto):
        estacao.verifica_entrada_nula()
        estacao.verifica_virgula_todo(nao_olhar)
        estacao.duplicados()
        estacao.verifica_caractere(nao_olhar)

    estacao.esta_correto()

if(__name__ == "__main__"):
    conferencia()



