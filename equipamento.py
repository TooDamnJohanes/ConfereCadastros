#ESSA FUNÇÃO ABRE O ARQUIVO E ADICIONA OS VALORES NA LISTA DADOS
from classe_verifica import Verifica

def conferencia():
    # Abrir o arquivo
    nome_arquivo = "equipamento.txt"
    dados = []
    correto = True
    target = 2

    equipamento = Verifica(dados, correto, nome_arquivo)
    equipamento.encontra_caminho()
    equipamento.verifica_campos(target)

    if(equipamento.correto):
        equipamento.verifica_entrada_nula()
        equipamento.verifica_virgula_todo()
        equipamento.verifica_duplicados()

    equipamento.esta_correto()

if(__name__ == "__main__"):
    conferencia()



