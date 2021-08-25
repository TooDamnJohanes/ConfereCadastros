from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

import os
import c_func
import c_implemento
import implemento_operacao
import operacoes_manutencao
import operacoes_parada
import operacoes_produtivas
import parada_tag
import c_checklist_item
import clima
import config_impl
import detalhes_manutencao
import equipe
import estacao
import local_descarregamento
import local_escavacao
import material
import insumos
import camadas
import jornada
import c_fase
import equipamento
from classe_abre_arquivo import Arquivos

nome_arquivo = ""
dados = []
correto = True

arquivos = Arquivos(dados, correto, nome_arquivo)

def confere_cadastros():
    global botao_check
    global dados_input
    global notebook
    main = os.getcwd()
    # ADICIONO O NOME DA PASTA CADASTRO NO DIRETORIO
    diagnostico = os.path.join(main, "DIAGNÓSTICO.TXT")
    detalhado = os.path.join(main, "DETALHES.TXT")
    if botao_check:
        botao_check = False
    else:
        botao_check = True
        arquivos.abre_pastas()
        if arquivos.correto:
            main = os.getcwd()
            diagnostico = os.path.join(main, "DIAGNÓSTICO.TXT")
            detalhado = os.path.join(main, "DETALHES.TXT")
            relatorio = open(diagnostico, "w", encoding="utf8")
            relatorio.write("**********************************************\n")
            relatorio.write("******** DIAGNOSTICO PASTA CADASTROS! ********\n")
            relatorio.write("**********************************************\n\n")
            relatorio.close()

            relatorio_2 = open(detalhado, "w", encoding="utf8")
            relatorio_2.write("**********************************************\n")
            relatorio_2.write("************** ERROS DETALHADOS **************\n")
            relatorio_2.write("**********************************************\n\n")
            relatorio_2.close()

            c_func.conferencia()
            c_implemento.conferencia()
            implemento_operacao.conferencia()
            operacoes_manutencao.conferencia()
            operacoes_parada.conferencia()
            operacoes_produtivas.conferencia()
            parada_tag.conferencia()
            c_checklist_item.conferencia()
            clima.conferencia()
            config_impl.conferencia()
            detalhes_manutencao.conferencia()
            equipe.conferencia()
            estacao.conferencia()
            local_descarregamento.conferencia()
            local_escavacao.conferencia()
            material.conferencia()
            insumos.conferencia()
            camadas.conferencia()
            jornada.conferencia()
            c_fase.conferencia()
            equipamento.conferencia()

        relatorio = open(diagnostico, "a", encoding="utf8")
        relatorio.write("**********************************************\n")
        relatorio.write("********* CENTRAL TECNICA SOLINFTEC **********\n")
        relatorio.write("**********************************************\n\n")
        relatorio.write("\n\n\n\n\n\n\n\n")
        relatorio.close()

        relatorio_2 = open(detalhado, "a", encoding="utf8")
        relatorio_2.write("**********************************************\n")
        relatorio_2.write("********* CENTRAL TECNICA SOLINFTEC **********\n")
        relatorio_2.write("**********************************************\n\n")
        relatorio_2.write("\n\n\n\n\n\n\n\n")
        relatorio_2.close()

        relatorio = open(diagnostico, "r", encoding="utf8")
        texto = relatorio.read().strip().upper()
        text_box2.insert(1.0, texto)
        text_box2.grid(column=0, row=1, padx=2, pady=3)

        relatorio_2 = open(detalhado, "r", encoding="utf8")
        texto2 = relatorio_2.read().strip().upper()
        text_box3.insert(1.0, texto2)
        text_box3.grid(column=0, row=2, padx=2, pady=3)

        messagebox.showinfo(title="CONFERE CADASTROS", message="CONFERENCIA FINALIZADA!\n"
                                                               "OS ARQUIVOS NÃO SÃO CORRIGIDOS!\n"
                                                               "CORRIJA-OS CONFORME DIAGNÓSTICO!")
        botao_check = False

janela = Tk()
width_value = janela.winfo_screenwidth()
height_value = janela.winfo_screenheight()
frame_1 = LabelFrame(janela, bd=1, text="Confere Cadastros")
text_box = Text(frame_1, height=((height_value)-731), width=30)
frame_2 = LabelFrame(janela, bd=1, text="Diagnóstico")
rows = 0
colunas = 0
notebook = ttk.Notebook(frame_2)
page1 = ttk.Frame(notebook)
page2 = ttk.Frame(notebook)
text_box2 = Text(page1, width=((width_value)-1260), height=((height_value)-728))
text_box3 = Text(page2, height=((height_value)-728), width=((width_value)-1260))
teste = ""
dados_input = []
botao_check = False

#PEGO O ARQUIVO DE INSTRUÇÃO, COLOCO EM UMA VARIAVEL, E JOGO NO TEXTO
main = os.getcwd()
# ADICIONO O NOME DA PASTA CADASTRO NO DIRETORIO
cadastros = os.path.join(main, "Cadastros_UTF-8")
instrucoes = os.path.join(cadastros, "files")
final = os.path.join(instrucoes, "INSTRUCOES.txt")
with open(final, "r+", encoding="utf8") as f:
    texto = f.read().strip().upper()


# CONFIGURAÇÃO DA JANELA
janela.geometry(f"{width_value}x{height_value}+0+0")
janela.resizable(False, True)
janela.title("CONFERE CADASTROS - TPL VERSION")

while rows < 500:
    frame_2.rowconfigure(rows, weight=1)
    frame_2.columnconfigure(rows, weight=1)
    frame_1.rowconfigure(rows, weight=1)
    frame_1.columnconfigure(rows, weight=1)
    rows +=1

# CONFIGURAÇÃO DO FRAME DOS BOTÕES
frame_1.place(x=10, y=10, height=((height_value) - 100), width=450)
text_box = Text(frame_1, height=((height_value) - 731), width=230)
text_box.insert(1.0, texto)
text_box.grid(columnspan=rows, rowspan=rows, padx=5, pady=55)

botao = Button(frame_1, text="Conferir Cadastros", command=lambda:confere_cadastros())
botao.grid(column=0, row=0, padx=10, pady=10, sticky="W")

# CONFIGURAÇÃO DO DIAGNÓSTICO

frame_2.place(x=465, y=10, height=((height_value) - 100), width=((width_value) - 498))
#text_box2.insert(1.0, "**********************************************")
#text_box2.insert(1.0, "******** DIAGNOSTICO PASTA CADASTROS! ********")
#text_box2.insert(1.0, "***************************************")
#text_box2.grid(column=0, row=1, padx=2, pady=3)
notebook.grid(row=0,column=0, columnspan=rows, rowspan=rows, sticky='NESW')
notebook.add(page1, text="Pasta Cadastro Diagnóstico")
notebook.add(page2, text="Erros Detalhados")




janela.mainloop()
