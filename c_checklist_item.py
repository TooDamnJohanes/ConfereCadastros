#ESSA FUNÇÃO ABRE O ARQUIVO E ADICIONA OS VALORES NA LISTA DADOS
from classe_verifica import Verifica

def conferencia():
    # encontra_caminho(dados)
    nome_arquivo = "C_CHECKLIST_ITEM.txt"
    dados = []
    correto = True
    target = 3
    nao_olhar = 2

    c_checklist_item = Verifica(dados, correto, nome_arquivo)
    c_checklist_item.encontra_caminho()
    c_checklist_item.verifica_campos(target)

    if(c_checklist_item.correto):
        c_checklist_item.verifica_entrada_nula()
        c_checklist_item.verifica_virgula_todo(nao_olhar)
        c_checklist_item.verifica_caractere(nao_olhar)
        c_checklist_item.verifica_caractere(nao_olhar)

    c_checklist_item.esta_correto()

if(__name__ == "__main__"):
    conferencia()



