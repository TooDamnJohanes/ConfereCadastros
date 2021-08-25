#ESSA FUNÇÃO ABRE O ARQUIVO E ADICIONA OS VALORES NA LISTA DADOS
from classe_verifica import Verifica

def conferencia():
    #Abrir o arquivo
    nome_arquivo = "ImplementoxOperacao.txt"
    nome_arquivo_implemento = "C_IMPLEMENTO.txt"
    nome_arquivo_operacao = "Operacoes_produtivas.txt"
    dados = []
    dados2 = []
    dados3 = []
    correto = True
    target = 2

    verifica_implemento = Verifica(dados2, correto, nome_arquivo_implemento)
    verifica_implemento.encontra_caminho()

    verifica_operacao_produtiva = Verifica(dados3, correto, nome_arquivo_operacao)
    verifica_operacao_produtiva.encontra_caminho()

    implemento_x_operacao = Verifica(dados, correto, nome_arquivo)
    implemento_x_operacao.encontra_caminho()
    implemento_x_operacao.verifica_campos(target)

    if(implemento_x_operacao.correto):
        implemento_x_operacao.verifica_vinculos(verifica_implemento.dados, 0, "C_IMPLEMENTO")
        implemento_x_operacao.verifica_vinculos(verifica_operacao_produtiva.dados, 1, "Operacoes_produtivas")
        implemento_x_operacao.verifica_virgula_todo()

    implemento_x_operacao.esta_correto()


if(__name__ == "__main__"):
    conferencia()



