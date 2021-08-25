#ESSA FUNÇÃO ABRE O ARQUIVO E ADICIONA OS VALORES NA LISTA DADOS
from classe_verifica import Verifica

def conferencia():
    #Abrir o arquivo
    nome_arquivo = "C_IMPLEMENTO.txt"
    dados = []
    correto = True
    target = 8
    nao_olhar = 1

    c_implemento = Verifica(dados, correto, nome_arquivo)
    c_implemento.encontra_caminho()
    c_implemento.verifica_campos(target)

    if(c_implemento.correto):
        c_implemento.verifica_virgula_todo(nao_olhar)
        c_implemento.verifica_entrada_nula()
        c_implemento.verifica_tag()
        c_implemento.verifica_caractere(nao_olhar)
        c_implemento.verifica_duplicados()

    c_implemento.esta_correto()

if(__name__ == "__main__"):
    conferencia()



