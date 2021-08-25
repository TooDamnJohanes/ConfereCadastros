#ESSA FUNÇÃO ABRE O ARQUIVO E ADICIONA OS VALORES NA LISTA DADOS
from classe_verifica import Verifica

def conferencia():
    #Abrir o arquivo
    nome_arquivo = "CLIMA.txt"
    nome_arquivo_operacao = "Operacoes_produtivas.txt"
    dados = []
    dados2 = []
    correto = True
    target = 25

    clima = Verifica(dados, correto, nome_arquivo)
    clima.encontra_caminho()
    clima.verifica_campos(target)

    if(clima.correto):
        verifica_operacao_produtiva = Verifica(dados2, correto, nome_arquivo_operacao)
        verifica_operacao_produtiva.encontra_caminho()

        clima.verifica_vinculos(verifica_operacao_produtiva.dados, 0, "OPERACOES_PRODUTIVAS")

        clima.verifica_virgula_todo()
        clima.verifica_parametros()
        clima.verifica_duplicados()

    clima.esta_correto()

if(__name__ == "__main__"):
    conferencia()



