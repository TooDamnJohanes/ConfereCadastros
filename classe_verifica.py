#ESSA FUNÇÃO ABRE O ARQUIVO E ADICIONA OS VALORES NA LISTA DADOS
from classe_abre_arquivo import Arquivos
from classe_printa import Printa

class Verifica(Printa, Arquivos):
    '''
    ABAIXO, EXISTEM FUNÇÕES COMUNS PARA TODOS OS ARQUIVOS. CADA UMA DELAS DESCREVE SUAS FUNCIONALIDADES;
    '''

    '''
    FUNÇÃO RESPONSÁVEL EM VERIFICAR SE EXISTE TODOS OS CAMPOS NECESSÁRIOS NO ARQUIVO
    '''
    def verifica_campos(self, target):
        self._printa.clear()
        self.detalhes.clear()

        for linhas in range(0, len(self._dados)):
            if (len(self.dados[linhas]) != target):
                self._printa.append(linhas+1)
                self.detalhes.append(self.dados[linhas])
                self._correto = False

        # FAÇO A VERIFICAÇÃO SE ELE É FALSO E SE TEM ALGO NESSE VETOR
        if (not self._correto and len(self._printa) > 0):
            self.printa_campos()

        self._printa.clear()
        self.detalhes.clear()
        return self._correto

    '''
    FUNÇÃO RESPONSÁVEL POR VERIFICAR SE O ARQUIVO CONTEM ENTRADAS EM BRANCO. ALGUNS ARQUIVOS PRECISARAM DISSO, OUTROS NÃO
    '''
    def verifica_entrada_nula(self):
        self._printa.clear()
        self.detalhes.clear()
        for i in range(0, len(self._dados)):
            # IF RESPONSÁVEL EM VERIFICAR ENTRADAS NULAS NOS ARQUIVOS .TXT;
            if ("" in self._dados[i]):
                #CASO TENHA ENTRADAS VALIDAS, EU ADICIONO O VALOR EM QUE i ESTÁ + 1, EM UM ARRAY;
                #ESTETICAMENTE MELHOR
                data = [word.replace("", "NULO") if word == "" else word for word in self.dados[i]]
                self._printa.append(i+1)
                self.detalhes.append(data)
                self._correto = False

        #SE O ARQUIVO ESTIVER ERRADO, IREI ESCREVER NO DIAGNÓSTICO O QUE ESTÁ ERRADO NELE;
        if(not self._correto and len(self._printa) > 0):
            self.printa_entrada_nula()

        self._printa.clear()
        self.detalhes.clear()
        return self._correto

    '''
    FUNÇÃO RESPONSÁVEL POR VERIFICAR SE O ARQUIVO CONTEM ENTRADAS COM VIRGULA. ALGUNS ARQUIVOS PRECISARAM DISSO, OUTROS NÃO
    '''
    #AQUI EU CRIO DOIS FOR, PORQUE EU PRECISO ANALISAR ITEM POR ITEM DA MATRIZ QUE FOI CRIADA;
    def verifica_virgula_todo(self, nao_olhar = None):
        self._printa.clear()
        self.detalhes.clear()
        if(nao_olhar == None):
            nao_olhar = -1
        for i in range(0, len(self._dados)):
            for j in range(0, len(self._dados[i])):
                if ("," in self._dados[i][j] and j != nao_olhar):
                    # CASO TENHA ENTRADAS VALIDAS, EU ADICIONO O VALOR EM QUE i ESTÁ + 1, EM UM ARRAY;
                    # ESTETICAMENTE MELHOR;
                    self._printa.append(i + 1)
                    self.detalhes.append(self.dados[i])
                    self._correto = False

        # SE O ARQUIVO ESTIVER ERRADO, IREI ESCREVER NO DIAGNÓSTICO O QUE ESTÁ ERRADO NELE;
        if(not self._correto and len(self._printa) > 0):
            self.printa_virgula()

        self._printa.clear()
        self.detalhes.clear()
        return self._correto

    '''
    FUNÇÃO RESPONSÁVEL POR VERIFICAR SE O ARQUIVO ESTÁ VALIDO OU NÃO
    '''
    def esta_correto(self):
        if (not self._correto):
            relatorio = open("DIAGNÓSTICO.TXT", "a", encoding="utf8")
            relatorio.write("\n")
            relatorio.write("****************************************************************************************************\n")
            relatorio.write("\t\t\t\t{} [INVALIDO]!\n".format(self._arquivo_nome).upper())
            relatorio.write("****************************************************************************************************\n\n")
            relatorio.write("\n")
            relatorio.close()

    '''
    ABAIXO, EXISTEM APENAS FUNÇÕES EXCLUSIVAS DE CADA ARQUIVO. CADA UMA DELAS DESCREVE SUAS FUNCIONALIDADES E PARA QUAL ARQUIVO SÃO EXCLUSIVAS;
    '''

    '''
    FUNÇÃO RESPONSÁVEL POR VERIFICAR SE O ARQUIVO C_FASE NÃO ESTÁ EM BRANCO
    '''
    # FUNÇÃO EXCLUSIVA DO C_FASE;
    # ESSA FUNÇÃO VERIFICA SE EXISTEM ENTRADAS NÃO NULAS NO C_FASE;
    def verifica_entrada_nao_nula(self):
        self._printa.clear()
        for i in range(0, len(self._dados)):
            #IF RESPONSÁVEL EM VERIFICAR SEM EXISTEM VALORES NÃO NULOS NO ARQUIVO;
            if (len(self._dados) != 0):
                self._correto = False

        #CASO O self._correto SEJA FALSO, IRÁ ESCREVER QUE O ARQUIVO ESTÁ INVALIDO;
        if(not self._correto and self.check):
            self.printa_nao_nulo()

        self._printa.clear()
        return self._correto

    '''
    FUNÇÃO RESPONSÁVEL POR COMPARAR OS DOIS CAMPOS DE MATRICULA DO ARQUIVO C_FUNC
    '''
    # FUNÇÕES EXCLUSIVAS DO C_FUNC;
    # ESSA FUNÇÃO VERIFICA OS DOIS CAMPOS DE MATRICULA DO OPERADOR NO C_FUNC;
    def verifica_matricula(self):
        self._printa.clear()
        self.detalhes.clear()
        for i in range(0, len(self._dados)):
            # IF RESPONSÁVEL EM VERIFICAR SE A MATRICULA ESTÁ CORRETA EM AMBOS OS CAMPOS;
            if (self._dados[i][0] != self._dados[i][3]):
                self._printa.append(i+1)
                data = [word.replace(self._dados[i][0], "DIFERENTES") if word == self._dados[i][0] else word for word in self.dados[i]]
                data = [word.replace(self._dados[i][3], "DIFERENTES") if word == self._dados[i][3] else word for word in self.dados[i]]
                self.detalhes.append(data)
                self._correto = False

        # SE O ARQUIVO ESTIVER ERRADO, IREI ESCREVER NO DIAGNÓSTICO O QUE ESTÁ ERRADO NELE;
        if (not self._correto and len(self._printa) > 0):
            self.printa_matricula()

        self._printa.clear()
        self.detalhes.clear()
        return self._correto

    '''
    FUNÇÃO RESPONSÁVEL POR VERIFICAR SE OS CAMPOS DO C_FUNC ESTÁ NOS PADROES
    '''
    # FUNÇÕES EXCLUSIVAS DO C_FUNC;
    # ESSA FUNÇÃO VERIFICA SE O TIPO DE OPERADOR ESTÁ CORRETO NO C_FUNC;
    def verifica_tipo(self):
        self._printa.clear()
        self.detalhes.clear()
        for i in range(0, len(self._dados)):
            #IF RESPONSÁVEL EM VERIFICAR SE A DESCRIÇÃO DO OPERADOR ESTÁ CORRETA;
            if (self._dados[i][2] != "O" and self._dados[i][2] != "M"):
                self._printa.append(i+1)
                data = [word.replace(self._dados[i][2], "ERRADO") if word == self._dados[i][2] else word for word in self.dados[i]]
                self.detalhes.append(data)
                self._correto = False
        # SE O ARQUIVO ESTIVER ERRADO, IREI ESCREVER NO DIAGNÓSTICO O QUE ESTÁ ERRADO NELE;
        if(not self._correto and len(self._printa) > 0):
            self.printa_tipo()

        self._printa.clear()
        self.detalhes.clear()
        return self._correto

    '''
    FUNÇÃO RESPONSÁVEL POR VERIFICAR SE EXISTE VINCULO DE TAG COM IMPLEMENTO E OPERAÇÃO
    '''
    #FUNÇÃO EXCLUSIVA DE TAG IMPLEMENTO;
    # ESSA FUNÇÃO VERIFICA OS TAGS E QUAIS VINCULOS FORAM FEITOS;
    def verifica_tag(self):
        self._printa.clear()
        #NESSA PRIMEIRA PARTE, EU VERIFICO SE EXISTEM VINCULOS FEITOS;
        for i in range(0, len(self._dados)):
            # IF RESPONSÁVEL EM VERIFICAR SE EXISTE ALGUM TAG CADASTRADO;
            if (self._dados[i][4] != ""):
                self._printa.append(self._dados[i][4])
        self.printa_tag()
        self._printa.clear()

    '''
    FUNÇÃO RESPONSÁVEL POR VERIFICAR SE OS VALORES MAXIMOS SÃO MENORES QUE OS VALORES MINIMOS
    '''
    # FUNÇÃO EXCLUSIVA DO CLIMA
    # ESSA FUNÇÃO VERIFICA SE OS CAMPOS COM MEDIDAS POSSUEM VIRGULA
    def verifica_parametros(self):
        self._printa.clear()
        self.detalhes.clear()
        vals = [1,2,4,5,6,7,9,10,11,12,13,14,16,17,18,19,21,22,23,24]

        # NESSE FOR EU ENTRO DENTRO DE CADA LINHA DOS DADOS;
        for i in range(0, len(self._dados)):
            # NESSE FOR, EU ENTRO DENTRO DO ARRAY VALS;
            for j in range(0,len(vals)):
                #AQUI EU VOU VERIFICAR ATÉ J+1 SER DO TAMANHO DE VALS, PORQUE AI EU JÁ FIZ TODAS AS COMPARAÇÕES
                if(j + 1 < len(vals)):
                    # IF RESPONSAVEL EM VERIFICAR SE OS VALORES MAXIMOS SÃO MENORES QUE OS VALORES MINIMOS;
                    if(self._dados[i][vals[j]] != "" and self._dados[i][vals[j+1]] != ""):
                        if (self._dados[i][vals[j]] < self._dados[i][vals[j+1]]):
                            data = [word.replace(self._dados[i][vals[j]], "ERRADO") if word == self._dados[i][vals[j]] else word for word in
                                    self.dados[i]]
                            data = [word.replace(self._dados[i][vals[j+1]], "ERRADO") if word == self._dados[i][vals[j+1]] else word for word in
                                    self.dados[i]]
                            #AQUI EU VERIFICO SE JÁ TEM ERRO NAQUELA LINHA, SE NÃO TIVER, EU ADICIONO NO VETOR
                            if((i+1) not in self._printa):
                                self._printa.append(i+1)
                                self.detalhes.append(data)
                            self._correto = False

        # FAÇO A VERIFICAÇÃO SE ELE É FALSO E SE TEM ALGO NESSE VETOR
        if (not self._correto and len(self._printa) > 0):
            self.printa_valor()
        self._printa.clear()
        self.detalhes.clear()
        return self._correto

    '''
    FUNÇÃO RESPONSÁVEL POR VERIFICAR SE AS ENTRADAS ESTÃO COM VALORES CONFIGURADOS FORA DO PADRÃO
    '''
    # FUNÇÃO EXCLUSIVA DO CONFIG_IMPLEMENTO;
    def verifica_entradas_fixas(self):
        self._printa.clear()
        self.detalhes.clear()
        #FOR INICIAL, RESPONSÁVEL POR VERIFICAR OS CAMPOS DA MATRIZ;
        for i in range(0, len(self._dados)):
            #VERIFICO SE O VALOR É DIFERENTE DE NULO, CASO SEJA, VERIFICO SE ELE É DIFERENTE DE 0 OU 1;
            if (self._dados[i][5] != ""):
                if (self._dados[i][5] != "0" or self._dados[i][5] != "1"):
                    self._printa.append(i+1)
                    data = [word.replace(self._dados[i][5], "ERRADO") if word == self._dados[i][5] else word for word in self.dados[i]]
                    self.detalhes.append(data)
                    self._correto = False

        if(not self.correto and len(self._printa) > 0):
            self.printa_ed3()

        self.detalhes.clear()
        self._printa.clear()

        for i in range(0, len(self._dados)):
            # VERIFICO SE O VALOR É DIFERENTE DE NULO, CASO SEJA, VERIFICO SE ELE É DIFERENTE DE 0 OU 1;
            if (self._dados[i][8] != ""):
                if (self._dados[i][8] != "0" or self._dados[i][8] != "1"):
                    self._printa.append(i + 1)
                    data = [word.replace(self._dados[i][8], "ERRADO") if word == self._dados[i][8] else word for word in self.dados[i]]
                    self.detalhes.append(data)
                    self._correto = False

        if (not self.correto and len(self._printa) > 0):
            self.printa_an1()

        self.detalhes.clear()
        self._printa.clear()

        for i in range(0, len(self._dados)):
            # VERIFICO SE O VALOR É DIFERENTE DE NULO, CASO SEJA, VERIFICO SE ELE É DIFERENTE DE 0 OU 1;
            if (self._dados[i][10] != ""):
                if (self._dados[i][10] != "0" or self._dados[i][10] != "1"):
                    if((i+1) not in self._printa):
                        self._printa.append(i + 1)
                    if(self.dados[i] not in self.detalhes):
                        data = [word.replace(self._dados[i][10], "ERRADO") if word == self._dados[i][10] else word for word in
                                self.dados[i]]
                        self.detalhes.append(data)
                    self._correto = False

            # VERIFICO SE O VALOR É DIFERENTE DE NULO, CASO SEJA, VERIFICO SE ELE É DIFERENTE DE 0 OU 1;
            if (self._dados[i][12] != ""):
                if (self._dados[i][12] != "0" or self._dados[i][12] != "1"):
                    if ((i + 1) not in self._printa):
                        self._printa.append(i + 1)
                    if (self.dados[i] not in self.detalhes):
                        data = [word.replace(self._dados[i][12], "ERRADO") if word == self._dados[i][12] else word for word in
                                self.dados[i]]
                        self.detalhes.append(data)
                    self._correto = False

        if (not self.correto and len(self._printa) > 0):
            self.printa_ed2()

        self.detalhes.clear()
        self._printa.clear()

        self.detalhes.clear()
        self._printa.clear()
        return self._correto

    '''
    FUNÇÃO RESPONSÁVEL POR VERIFICAR SE EXISTE DUPLICATAS EM FZT NO ARQUIVO ESTACAO
    '''
    #FUNÇÃO EXCLUSIVA DE ESTACAO;
    def duplicados(self):
        self._printa.clear()
        self.detalhes.clear()
        #CRIO O FOR E PEGO OS VALORES DE FZT EM VARIAVEIS SEPARADAS;
        for i in range(0, len(self._dados)):
            t = self._dados[i][2]  # PEGUEI O VALOR DO TALHÃO;
            z = self._dados[i][1]  # PEGUEI O VALOR DA ZONA;
            f = self._dados[i][0]  # PEGUEI O VALOR DA FAZENDA;
            #CRIO UM IF, ATÉ O ULTIMO VALOR DO ARRAY, SEM PASSAR DELE COM i+1
            if ((i + 1) < len(self._dados)):
                #ACESSO CADA VALOR DA MATRIZ AQUI;
                for n in range(0, len(self._dados)):
                    #VALOR DE n NÃO PODE SER IGUAL AO VALOR DE i;
                    if (n != i):
                        # COMPARO SE O VALOR DO TALHÃO QUE ESTA EM T, É IGUAL A OUTRO TALHÃO DA LISTA
                        if (self._dados[n][2] == t):
                            # SE O TALHÃO É IGUAL, COMPARO SE A ZONA TAMBÉM É IGUAL;
                            if (self._dados[n][1] == z):
                                # SE O TALHÃO, ZONA FOREM IGUAIS, COMPARO SE A FAZENDA É IGUAL
                                if (self._dados[n][0] == f):
                                    self._printa.append(i)
                                    data = [word.replace(self._dados[n][0], "ERRADO") if word == self._dados[n][0] else word for word
                                            in
                                            self.dados[n]]
                                    data = [word.replace(self._dados[n][1], "ERRADO") if word == self._dados[n][1] else word for word
                                            in
                                            self.dados[n]]
                                    data = [word.replace(self._dados[n][2], "ERRADO") if word == self._dados[n][2] else word for word
                                            in
                                            self.dados[n]]
                                    self.detalhes.append(data)
                                    self._correto = False

        # FAÇO A VERIFICAÇÃO SE ELE É FALSO E SE TEM ALGO NESSE VETOR
        if (not self._correto and len(self._printa) > 0):
            self.printa_duplicados()

        self._printa.clear()
        self.detalhes.clear()
        return self._correto

    '''
    FUNÇÃO RESPONSÁVEL POR VERIFICAR SE EXISTE TEMPO CONFIGURADO EM ALGUM CAMPO PARA TPL
    '''
    # FUNÇÃO EXCLUSIVA DE OPERAÇÕES PARADAS
    def verifica_tempo_parada(self):
        self._printa.clear()
        for i in range(0, len(self._dados)):
            # IF RESPONSÁVEL EM VERIFICAR SE EXISTE TEMPO INSERIDO NO CAMPO DE OPERACOES_PARADAS;
            if (self._dados[i][2] != "N"):
                self._printa.append(self._dados[i][0])
                self._printa2.append(self._dados[i][2])

        # FAÇO A VERIFICAÇÃO SE ELE É FALSO E SE TEM ALGO NESSE VETOR
        if (len(self._printa) > 0 and len(self._printa2) > 0):
            self.printa_tempo()

        self._printa.clear()
        return self._correto

    '''
    FUNÇÃO RESPONSÁVEL POR VERIFICAR SE OS CAMPOS RESERVADOS EM OPERACOES_PRODUTIVAS ESTAO FORA DO PADRÃO
    '''
    # FUNCÕES EXCLUSIVAS DE OPERACOES_PRODUTIVAS
    def verifica_reservados(self):
        self._printa.clear()
        self.detalhes.clear()
        for i in range(0, len(self._dados)):
            # IF RESPONSÁVEL EM VERIFICAR SE O CAMPO RESERVADO ESTÁ FORA DO PADRÃO;
            for n in range(2, 5):
                if (self._dados[i][n] != "N"):
                    if(i+1 not in self._printa):
                        self._printa.append(i+1)
                        data = [word.replace(self._dados[i][n], "ERRADO") if word == self._dados[i][n] else word for word in
                                self.dados[i]]
                        self.detalhes.append(data)
                    self._correto = False

            # IF RESPONSÁVEL EM VERIFICAR SE O CAMPO RESERVADO ESTÁ FORA DO PADRÃO;
            if (self._dados[i][7] != "N"):
                if (i + 1 not in self._printa):
                    self._printa.append(i + 1)
                    data = [word.replace(self._dados[i][7], "ERRADO") if word == self._dados[i][7] else word for word in
                            self.dados[i]]
                    self.detalhes.append(data)
                self._correto = False

        # FAÇO A VERIFICAÇÃO SE ELE É FALSO E SE TEM ALGO NESSE VETOR
        if (not self._correto and len(self._printa) > 0):
            self.printa_reservados()

        self._printa.clear()
        self.detalhes.clear()
        return self._correto

    '''
    FUNÇÃO RESPONSÁVEL POR VERIFICAR SE A VELOCIDADE MINIMA É MAIOR QUE A VELOCIDADE MAXIMA
    '''
    # FUNCÕES EXCLUSIVAS DE OPERACOES_PRODUTIVAS
    # FUNÇÃO RESPONSÁVEL POR VERIFICAR SE A VELOCIDADE MINIMA É MAIOR QUE A VELOCIDADE MAXIMA;
    def verifica_valores(self):
        self._printa.clear()
        self.detalhes.clear()
        for i in range(0, len(self._dados)):
            #VERIFICO SE O CAMPO É DIFERENTE DE Y;
            if (self._dados[i][8] != "Y" and self.dados[i][9] != "Y"):
                min = int(self._dados[i][8])
                max = int(self._dados[i][9])
                #AQUI EU VERIFICO SE OS VALORES SÃO MAIORES OU NÃO;
                if (min > max):
                    self._printa.append(i+1)
                    data = [word.replace(self._dados[i][8], "ERRADO") if word == self._dados[i][8] else word for word in
                            self.dados[i]]
                    data = [word.replace(self._dados[i][9], "ERRADO") if word == self._dados[i][9] else word for word in
                            self.dados[i]]

                    self.detalhes.append(data)
                    self._correto = False

        # FAÇO A VERIFICAÇÃO SE ELE É FALSO E SE TEM ALGO NESSE VETOR
        if(not self._correto and len(self._printa) > 0):
            self.printa_velocidade_max_min()

        self._printa.clear()
        self.detalhes.clear()
        return self._correto

    '''
    FUNÇÃO RESPONSÁVEL POR VERIFICAR VINCULOS ENTRE ARQUIVOS
    '''
    def verifica_vinculos(self, verifica_vinculo, n, nome_comparacao):
        self._printa.clear()
        #COM O ARRAY ERRADOS, EU INSIRO TODAS AS INFORMAÇÕES QUE DESEJO COMPARAR;
        for i in range(0, len(verifica_vinculo)):
            self.vinculos.append(verifica_vinculo[i][0])

        #AQUI EU COMPARO OS VINCULOS DESEJADOS;
        for i in range(0, len(self._dados)):
            #SE UM DADO EM self._dados NÃO EXISTE EM errados, JÁ ASSUME FALSO, E MOSTRA ONDE ESTÁ ERRADO;
            if (self._dados[i][n] not in self.vinculos):
                #print("  > {} NÃO EXISTE EM {}\n".format(self.dados[i][n], nome_comparacao))
                self._printa.append(self._dados[i][n])
                self._correto = False

        if(not self._correto and len(self._printa) > 0):
            self.printa_verifica_vinculo(nome_comparacao)
        self._printa.clear()
        return self._correto

    def verifica_caractere(self, n):
        self._printa.clear()
        self.detalhes.clear()
        for i in range(0, len(self.dados)):
            if(len(self.dados[i][n]) > self._caractere):
                self._printa.append(i+1)
                data = [word.replace(self._dados[i][n], "ERRADO") if word == self._dados[i][n] else word for word in
                        self.dados[i]]
                self.detalhes.append(data)
                self._correto = False

        if (not self._correto and len(self._printa) > 0):
            self.printa_caractere()
        self._printa.clear()
        self.detalhes.clear()
        return self._correto

    def verifica_cd_especial(self):
        self._printa.clear()
        self.detalhes.clear()
        cd_produtivo = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "20", "21", "22", "23",
                        "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44",
                        "45", "46", "47", "48", "49", "50", "51", "52", "53", "55", "56","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                        "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V","W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                        "l", "m", "n", "o", "p", "q", "r","s", "t", "u", "w", "x")

        for i in range(0, len(self.dados)):
            if (self.dados[i][5] not in cd_produtivo):
                self._printa.append(i+1)
                data = [word.replace(self._dados[i][5], "ERRADO") if word == self._dados[i][5] else word for word in
                        self.dados[i]]
                self.detalhes.append(data)
                self._correto = False

        if (not self._correto and len(self._printa) > 0):
            self.printa_cd_produtivo()
        self._printa.clear()
        self.detalhes.clear()
        return self._correto

    def verifica_cd_especial_parada(self):
        self._printa.clear()
        self.detalhes.clear()
        cd_improdutivo = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "M",
                        "O", "P", "Q", "R", "S", "T", "J", "K", "U", "V", "W", "X", "a", "b", "c", "d", "e", "f", "g", "h", "L", "N")

        for i in range(0, len(self.dados)):
            if (self.dados[i][3] not in cd_improdutivo):
                self._printa.append(i+1)
                data = [word.replace(self._dados[i][3], "ERRADO") if word == self._dados[i][3] else word for word in
                        self.dados[i]]
                self.detalhes.append(data)
                self._correto = False

        if (not self._correto and len(self._printa) > 0):
            self.printa_cd_produtivo()
        self._printa.clear()
        self.detalhes.clear()
        return self._correto

    def verifica_duplicados(self):
        self._printa.clear()
        self.detalhes.clear()
        for i in range(0, len(self.dados)):
            for j in range(0, len(self.dados)):
                if(self.dados[i][0] == self.dados[j][0] and i != j):
                    if(self.dados[i][0] not in self.printa):
                        self.printa.append(self.dados[i][0])
                        data = [word.replace(self._dados[i][0], "ERRADO") if word == self._dados[i][0] else word for word in
                                self.dados[i]]
                        self.detalhes.append(data)
                    self._correto = False


        if (not self._correto and len(self._printa) > 0):
            self.printa_codigos_duplicados()
        self._printa.clear()
        self.detalhes.clear()
        return self._correto

    def verifica_vinculos_cp(self, verifica_vinculo, nome_comparacao):
        self._printa.clear()
        self.vinculos.clear()
        #COM O ARRAY ERRADOS, EU INSIRO TODAS AS INFORMAÇÕES QUE DESEJO COMPARAR;
        for i in verifica_vinculo:
            self.vinculos.append(i)

        #AQUI EU COMPARO OS VINCULOS DESEJADOS;
        for i in range(0, len(self._dados)):
            #SE UM DADO EM self._dados NÃO EXISTE EM errados, JÁ ASSUME FALSO, E MOSTRA ONDE ESTÁ ERRADO;
            if (str(self._dados[i][0] + ".png") not in self.vinculos):
                #print("  > {} NÃO EXISTE EM {}\n".format(self.dados[i][n], nome_comparacao))
                self._printa.append(self._dados[i][0])
                self._correto = False

        if(not self._correto and len(self._printa) > 0):
            self.printa_verifica_vinculo(nome_comparacao)
        self._printa.clear()
        return self._correto



if(__name__ == "__main__"):
    pass