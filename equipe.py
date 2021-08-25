#ESSA FUNÇÃO ABRE O ARQUIVO E ADICIONA OS VALORES NA LISTA DADOS
from classe_verifica import Verifica

def conferencia():
    #Abrir o arquivo
    nome_arquivo = "equipe.txt"
    dados = []
    correto = True
    target = 2
    nao_olhar = 1

    equipe = Verifica(dados, correto, nome_arquivo)
    equipe.encontra_caminho()
    equipe.verifica_campos(target)

    if(equipe.correto):
        equipe.verifica_entrada_nula()
        equipe.verifica_virgula_todo(nao_olhar)
        equipe.verifica_caractere(nao_olhar)
        equipe.verifica_duplicados()

    equipe.esta_correto()

if(__name__ == "__main__"):
    conferencia()



