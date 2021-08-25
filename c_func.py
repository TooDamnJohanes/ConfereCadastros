#ESSA FUNÇÃO ABRE O ARQUIVO E ADICIONA OS VALORES NA LISTA DADOS
from classe_verifica import Verifica

def conferencia():
    #Abrir o arquivo
    nome_arquivo = "C_FUNC.txt"
    dados = []
    correto = True
    target = 5
    nao_olhar = 1

    c_func = Verifica(dados, correto, nome_arquivo)
    c_func.encontra_caminho()
    c_func.verifica_campos(target)

    if(c_func.correto):
        c_func.verifica_entrada_nula()
        c_func.verifica_virgula_todo(nao_olhar)
        c_func.verifica_matricula()
        c_func.verifica_tipo()
        c_func.verifica_caractere(nao_olhar)
        c_func.verifica_duplicados()
    c_func.esta_correto()


if(__name__ == "__main__"):
    conferencia()



