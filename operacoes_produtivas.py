#ESSA FUNÇÃO ABRE O ARQUIVO E ADICIONA OS VALORES NA LISTA DADOS
from classe_verifica import Verifica

def conferencia():
    #Abrir o arquivo
    nome_arquivo = "Operacoes_produtivas.txt"
    dados = []
    correto = True
    target = 10
    nao_olhar = 1

    operacoes_produtivas = Verifica(dados, correto, nome_arquivo)
    operacoes_produtivas.encontra_caminho()
    operacoes_produtivas.verifica_campos(target)

    if(operacoes_produtivas.correto):
        operacoes_produtivas.verifica_entrada_nula()
        operacoes_produtivas.verifica_virgula_todo(nao_olhar)
        operacoes_produtivas.verifica_reservados()
        operacoes_produtivas.verifica_valores()
        operacoes_produtivas.verifica_caractere(nao_olhar)
        operacoes_produtivas.verifica_cd_especial()
        operacoes_produtivas.verifica_duplicados()

    operacoes_produtivas.esta_correto()

if(__name__ == "__main__"):
    conferencia()



