#ESSA FUNÇÃO ABRE O ARQUIVO E ADICIONA OS VALORES NA LISTA DADOS
from classe_verifica import Verifica

def conferencia():
    #Abrir o arquivo
    nome_arquivo = "operacoes_manutencao.txt"
    dados = []
    correto = True
    target = 3
    nao_olhar = 1

    operacoes_manutencao = Verifica(dados, correto, nome_arquivo)
    operacoes_manutencao.encontra_caminho()
    operacoes_manutencao.verifica_campos(target)

    if(operacoes_manutencao.correto):
        operacoes_manutencao.verifica_entrada_nula()
        operacoes_manutencao.verifica_virgula_todo(nao_olhar)
        operacoes_manutencao.verifica_caractere(nao_olhar)
        operacoes_manutencao.verifica_duplicados()

    operacoes_manutencao.esta_correto()

if(__name__ == "__main__"):
    conferencia()



