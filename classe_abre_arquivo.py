#ESSA FUNÇÃO ABRE O ARQUIVO E ADICIONA OS VALORES NA LISTA DADOS
import os
import chardet
import re
import unidecode

class Arquivos():
    def __init__(self, dados, correto, nome_arquivo = None):
        self._dados = dados
        self._correto = correto
        self._nome_arquivo = nome_arquivo
        self._arquivo_nome = nome_arquivo.upper()
        self._marcador = False
        self._printa = []
        self._printa2 = []
        self._contador = 0
        self._texto = ""
        self.dif = 0
        self._caractere = 32
        self.check = False
        self.code = None
        self.vinculos = []
        self.detalhes = []
        self.marcador_2 = False

    @property
    def printa(self):
        return self._printa

    @property
    def dados(self):
        return self._dados

    @property
    def correto(self):
        return self._correto

    @property
    def nome_arquivo(self):
        return self._nome_arquivo

    '''
    FUNÇÃO RESPONSÁVEL EM PEGAR O NOME DO ARQUIVO, E COLOCAR EM TARGET
    '''

    def encontra_caminho(self):
        self.printa.clear()
        dados_input = []
        target = self._nome_arquivo
        target2 = target
        #PEGO O DIRETÓRIO EM QUE O EXECUTAVEL SE ENCONTRA
        main = os.getcwd()
        #ADICIONO O NOME DA PASTA CADASTRO NO DIRETORIO
        cadastros = os.path.join(main, "Cadastros")

        # PEGO OS NOMES DE TODOS OS ARQUIVOS NA PASTA CADASTRO;
        for i in os.listdir(cadastros):
            dados_input.append(i)

        #COMPARAÇÃO ENTRE OS NOMES QUE EU SETEI COMO TARGET, COM OS NOMES ENCONTRADOS NA PASTA CADASTRO
        for i in range(0, len(dados_input)):
            if (dados_input[i].upper() == target.upper()):
                self.check = True
                target = dados_input[i]
        if(self.check):
            #JUNTO O NOME DO TARGET, NA VARIAVEL PARA ABRIR O ARQUIVO, GARANTINDO ASSIM, QUE O ANALISTA PODE DEIXAR O ARQUIVO COM QUALQUER NOME
            self._nome_arquivo = os.path.join(cadastros, target)
            self.trata_arquivo(target2)
        if(not self.check):
            self._correto = False
            self.printa_sem_arq()
            return self._correto
        self.printa.clear()
    '''
    FUNÇÃO RESPONSÁVEL EM MUDAR A CODIFICAÇÃO DO ARQUIVO PARA UTF-8 E TIRAR ESPAÇOS EM BRANCO
    '''
    def trata_arquivo(self, target):
        main = os.getcwd()
        # ADICIONO O NOME DA PASTA CADASTRO NO DIRETORIO
        cadastros = os.path.join(main, "Cadastros_UTF-8")
        tratado = os.path.join(cadastros, target)

        #NESSE CÓDIGO, EU PEGO QUAL A CODIFICAÇÃO DO ARQUIVO ORIGINAL
        rawdata = open(self._nome_arquivo, "rb").read()
        charenc = chardet.detect(rawdata)
        result = charenc['encoding']

        if (result == None):
            result = 'UTF-8'

        #ABRO O ARQUIVO ORIGINAL
        with open(self._nome_arquivo, 'rb') as source_file:
            #CRIO UM NOVO ARQUIVO
            with open(tratado, 'wb') as dest_file:
                #LEIO O ARQUIVO E JÁ FAÇO UM TRATAMENTO EM DADOS COM ESPAÇOS E ULTIMAS LINHAS EM BRANCO
                #COLOCO TUDO EM MAIUSCULO
                contents = source_file.read().strip().upper()
                #TIRO TODOS OS CARACTERES ESPECIAIS NO MEIO DA PALAVRA
                contents = unidecode.unidecode(contents.decode(result))
                #RETIRO OUTROS CARACTERES ESPECIAIS
                contents = re.sub("[^A-Za-z0-9 \n,;.()/]+", "", contents)
                #ESCREVO ISSO NO ARQUIVO, COM A CODIFICAÇÃO UTF-8
                #dest_file.write(contents.decode(result).encode('UTF-8'))
                dest_file.write(contents.encode('UTF-8'))

        #AQUI EU ABRO O ARQUIVO NOVAMENTE
        with open(tratado, 'r+', encoding="utf-8") as f:
            #LEIO TODAS AS LINHAS
            lines = f.readlines()
            #VOLTO NA POSIÇÃO 0
            f.seek(0)
            #TIRO TODAS AS LINHAS EM BRANCO
            f.writelines(line for line in lines if line.strip())
            f.truncate()

        self._nome_arquivo = tratado
        self.abre_arquivo()

    '''
    FUNÇÃO RESPONSÁVEL EM ABRIR O ARQUIVO TRATADO E ADICIONAR VALORES NO ARRAY
    '''
    def abre_arquivo(self):
        with open(self._nome_arquivo, "r", encoding="utf-8") as arquivo:
            # ABRO O ARQUIVO, COLOCANDO OS DADOS EM UM ARRAY, SEPARANDO ELES POR ";";
            for linha in arquivo:
                self._dados.append(linha.strip().split(";"))
            arquivo.close()

    def abre_pasta_cp(self):
        #PEGO O DIRETÓRIO EM QUE O EXECUTAVEL SE ENCONTRA
        main = os.getcwd()
        #ADICIONO O NOME DA PASTA CADASTRO NO DIRETORIO
        cadastros = os.path.join(main, "Cadastros")
        cp = os.path.join(cadastros, "CP")

        # PEGO OS NOMES DE TODOS OS ARQUIVOS NA PASTA CADASTRO;
        for i in os.listdir(cp):
            self.dados.append(i)

    def abre_pastas(self):
        self.printa.clear()
        folders = ("Cadastros", "Cadastros_UTF-8", "files")
        #PEGO O DIRETÓRIO EM QUE O EXECUTAVEL SE ENCONTRA
        main = os.getcwd()
        for i in os.listdir(main):
            self.dados.append(i)

        #ADICIONO O NOME DA PASTA CADASTRO NO DIRETORIO
        cadastros = os.path.join(main, "Cadastros")
        for i in os.listdir(cadastros):
            self.dados.append(i)

        cadastros_utf8 = os.path.join(main, "Cadastros_UTF-8")
        for i in os.listdir(cadastros_utf8):
            self.dados.append(i)

        for i in range(len(folders)):
            if(folders[i] not in self.dados):
                self.printa.append(folders[i])
                self._correto = False
        if not self._correto and len(self.printa) > 0:
            self.printa_pastas()
            return self.correto


if(__name__ == "__main__"):
    pass