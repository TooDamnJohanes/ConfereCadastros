#ESSA FUNÇÃO ABRE O ARQUIVO E ADICIONA OS VALORES NA LISTA DADOS
from classe_verifica import Verifica

def conferencia():
    #Abrir o arquivo
    nome_arquivo = "operacoes_paradas.txt"
    dados = []
    correto = True
    target = 5
    nao_olhar = 1
    dados_cp = []
    correto_cp = True
    nome_arquivo_cp = "CP"

    operacoes_paradas = Verifica(dados, correto, nome_arquivo)
    operacoes_paradas.encontra_caminho()
    operacoes_paradas.verifica_campos(target)

    pasta_cp = Verifica(dados_cp, correto_cp, nome_arquivo_cp)
    pasta_cp.abre_pasta_cp()

    if(operacoes_paradas.correto):
        operacoes_paradas.verifica_entrada_nula()
        operacoes_paradas.verifica_virgula_todo(nao_olhar)
        operacoes_paradas.verifica_tempo_parada()
        operacoes_paradas.verifica_caractere(nao_olhar)
        operacoes_paradas.verifica_cd_especial_parada()
        operacoes_paradas.verifica_duplicados()
        operacoes_paradas.verifica_vinculos_cp(pasta_cp.dados, "PASTA CP")

    operacoes_paradas.esta_correto()

if(__name__ == "__main__"):
    conferencia()



