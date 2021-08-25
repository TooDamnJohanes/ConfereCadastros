#ESSA FUNÇÃO ABRE O ARQUIVO E ADICIONA OS VALORES NA LISTA DADOS
from classe_verifica import Verifica

def conferencia():
    # Abrir o arquivo
    nome_arquivo = "DetalhesManutencao.txt"
    dados = []
    correto = True
    target = 6
    nao_olhar = 1

    detalhes_manutencao = Verifica(dados, correto, nome_arquivo)
    detalhes_manutencao.encontra_caminho()
    detalhes_manutencao.verifica_campos(target)

    if(detalhes_manutencao.correto):
        detalhes_manutencao.verifica_entrada_nula()
        detalhes_manutencao.verifica_virgula_todo(nao_olhar)
        detalhes_manutencao.verifica_caractere(nao_olhar)

    detalhes_manutencao.esta_correto()

if(__name__ == "__main__"):
    conferencia()



