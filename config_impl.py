#ESSA FUNÇÃO ABRE O ARQUIVO E ADICIONA OS VALORES NA LISTA DADOS
from classe_verifica import Verifica

def conferencia():
    #Abrir o arquivo
    nome_arquivo = "ConfigImpl.txt"
    nome_arquivo_implemento = "C_IMPLEMENTO.txt"
    nome_arquivo_operacao = "Operacoes_produtivas.txt"
    dados = []
    dados2 = []
    dados3 = []
    correto = True
    target = 13

    verifica_implemento = Verifica(dados2, correto, nome_arquivo_implemento)
    verifica_implemento.encontra_caminho()

    verifica_operacao_produtiva = Verifica(dados3, correto, nome_arquivo_operacao)
    verifica_operacao_produtiva.encontra_caminho()

    configImpl = Verifica(dados, correto, nome_arquivo)
    configImpl.encontra_caminho()
    configImpl.verifica_campos(target)

    if(configImpl.correto):
        configImpl.verifica_vinculos(verifica_implemento.dados, 1, "C_IMPLEMENTO")
        configImpl.verifica_vinculos(verifica_operacao_produtiva.dados, 2, "OPERACOES_PRODUTIVA")
        configImpl.verifica_virgula_todo()
        configImpl.verifica_entradas_fixas()

    configImpl.esta_correto()

if(__name__ == "__main__"):
    conferencia()



