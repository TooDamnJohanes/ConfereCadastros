#ESSA FUNÇÃO ABRE O ARQUIVO E ADICIONA OS VALORES NA LISTA DADOS
from classe_verifica import Verifica

def conferencia():
    #Abrir o arquivo
    nome_arquivo = "jornada.txt"
    dados = []
    correto = True
    target = 5

    jornada = Verifica(dados, correto, nome_arquivo)
    jornada.encontra_caminho()
    jornada.verifica_campos(target)

    if(jornada.correto):
        jornada.verifica_entrada_nula()
        jornada.verifica_virgula_todo()

    jornada.esta_correto()

if(__name__ == "__main__"):
    conferencia()



