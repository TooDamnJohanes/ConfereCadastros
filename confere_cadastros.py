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

def confere_cadastros():
    relatorio = open("DIAGNÓSTICO.TXT", "w", encoding="utf8")
    relatorio.write("**********************************************\n")
    relatorio.write("******** DIAGNOSTICO PASTA CADASTROS! ********\n")
    relatorio.write("**********************************************\n\n")
    relatorio.close()

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

    relatorio = open("DIAGNÓSTICO.TXT", "a")
    relatorio.write("**********************************************\n")
    relatorio.write("************ SHEEEEEEEEEEEESH BRO! ***********\n")
    relatorio.write("**********************************************\n\n")
    relatorio.close()

if(__name__ == "__main__"):
    confere_cadastros()
