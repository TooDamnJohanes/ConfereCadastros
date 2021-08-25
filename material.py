#ESSA FUNÇÃO ABRE O ARQUIVO E ADICIONA OS VALORES NA LISTA DADOS
from classe_verifica import Verifica

def conferencia():
    #Abrir o arquivo
    nome_arquivo = "material.txt"
    dados = []
    correto = True
    target = 2

    material = Verifica(dados, correto, nome_arquivo)
    material.encontra_caminho()
    material.verifica_campos(target)

    if(material.correto):
        material.verifica_entrada_nula()
        material.verifica_virgula_todo()
        material.verifica_duplicados()

    material.esta_correto()

if(__name__ == "__main__"):
    conferencia()



