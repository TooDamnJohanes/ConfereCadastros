from classe_abre_arquivo import Arquivos

class Printa(Arquivos):

    def printa_sem_arq(self):
        if (not self._marcador):
            self.printa_cabecalho()
        self._texto = "ARQUIVO {} NÃO ESTÁ NA PASTA CADASTRO!".format(self.nome_arquivo)

        relatorio = open("DIAGNÓSTICO.TXT", "a", encoding="utf8")

        relatorio.write("\n")
        relatorio.write("{}\n".format(self._texto))
        relatorio.write("\n")
        relatorio.close()

    def acha_dif(self):
        self.dif = 0
        size = 50
        self.dif = size - len(self._arquivo_nome.upper())
        return self.dif

    def printa_cabecalho(self):
        self.acha_dif()
        estrelas = ""
        self._marcador = True
        relatorio = open("DIAGNÓSTICO.TXT", "a", encoding="utf8")
        relatorio.write("\n")
        relatorio.write("\n")
        for i in range(0, (self.dif)+1):
            estrelas += "*"

        relatorio.write('{} {} {} \n'.format(estrelas, self._arquivo_nome.upper(), estrelas))
        relatorio.write("\n")

    def printa_cabecalho_2(self):
        self.acha_dif()
        estrelas = ""
        self.marcador_2 = True

        relatorio = open("DETALHES.TXT", "a", encoding="utf8")
        relatorio.write("\n")
        relatorio.write("\n")
        for i in range(0, (self.dif) + 1):
            estrelas += "*"

        relatorio.write('{} {} {} \n'.format(estrelas, self._arquivo_nome.upper(), estrelas))
        relatorio.write("\n")

    def printa_c_fase(self):
        self.check_print = True
        if (not self._marcador):
            self.printa_cabecalho()
        relatorio = open("DIAGNÓSTICO.TXT", "a", encoding="utf8")
        relatorio.write("\n")
        relatorio.write('{} \n'.format(self._texto))

    def printa_linha(self):
        self._contador = 0
        relatorio = open("DIAGNÓSTICO.TXT", "a", encoding="utf8")
        relatorio.write("\n")
        if (not self._marcador):
            self.printa_cabecalho()
        if(not self.marcador_2):
            self.printa_cabecalho_2()

        relatorio.write("\n")
        relatorio.write("\t> ERRO EM {}! {} \n\tCONFIRA AS LINHAS:\n".format(self._arquivo_nome, self._texto))
        for i in range(0, len(self._printa)):
            # VERIFICO SE JÁ FORAM MOSTRADOS 5 ELEMENTOS NO ARQUIVO, SE SIM, EU QUEBRO A LINHA
            # E ZERO O CONTADOR
            if (self._contador > 3):
                relatorio.write("\n")
                self._contador = 0

            relatorio.write("\t{}\t".format(self._printa[i]))
            self._contador += 1
        relatorio.write("\n")
        relatorio.close()

        relatorio = open("DETALHES.TXT", "a", encoding="utf8")
        relatorio.write("\n")
        relatorio.write("\n")
        relatorio.write("\t> DETALHES DE {}!\n \t> {}\n\n".format(self._arquivo_nome, self._texto))
        for i in range(0, len(self.detalhes)):
            # VERIFICO SE JÁ FORAM MOSTRADOS 5 ELEMENTOS NO ARQUIVO, SE SIM, EU QUEBRO A LINHA
            # E ZERO O CONTADOR
            relatorio.write("\t{}".format(self.detalhes[i]))
            relatorio.write("\n\n")
        relatorio.write("\n")
        relatorio.close()



    def printa_cd_duplicados(self):
        self._contador = 0
        relatorio = open("DIAGNÓSTICO.TXT", "a", encoding="utf8")
        relatorio.write("\n")
        if (not self._marcador):
            self.printa_cabecalho()
        if (not self.marcador_2):
            self.printa_cabecalho()

        relatorio.write("\n")
        relatorio.write("\t> ERRO EM {}! {} \n\tCONFIRA OS CÓDIGOS:\n".format(self._arquivo_nome, self._texto))
        for i in range(0, len(self._printa)):
            # VERIFICO SE JÁ FORAM MOSTRADOS 5 ELEMENTOS NO ARQUIVO, SE SIM, EU QUEBRO A LINHA
            # E ZERO O CONTADOR
            if (self._contador > 3):
                relatorio.write("\n")
                self._contador = 0

            relatorio.write("\t{}\t".format(self._printa[i]))
            self._contador += 1
        relatorio.write("\n")
        relatorio.close()

        relatorio = open("DETALHES.TXT", "a", encoding="utf8")
        relatorio.write("\n")
        relatorio.write("\t> DETALHES DE {}!\n \t> {}\n\n".format(self._arquivo_nome, self._texto))
        for i in range(0, len(self.detalhes)):
            # VERIFICO SE JÁ FORAM MOSTRADOS 5 ELEMENTOS NO ARQUIVO, SE SIM, EU QUEBRO A LINHA
            # E ZERO O CONTADOR
            relatorio.write("\t{}".format(self.detalhes[i]))
            relatorio.write("\n\n")
        relatorio.write("\n")
        relatorio.close()

    def printa_tempos(self):
        self._contador = 0
        relatorio = open("DIAGNÓSTICO.TXT", "a", encoding="utf8")
        relatorio.write("\n")
        if (not self._marcador):
            self.printa_cabecalho()

        relatorio.write("\n")
        relatorio.write("\t> PARADAS COM TEMPO CONFIGURADO\n")
        for i in range(0, len(self._printa)):
            relatorio.write("\tPARADA: {}\t TEMPO: {} MINUTOS\n".format(self._printa[i], self._printa2[i]))

        relatorio.write("\n")
        relatorio.close()


    def printa_verifica_vinculo(self, nome_comparacao):
        relatorio = open("DIAGNÓSTICO.TXT", "a", encoding="utf8")
        if(not self._marcador):
            self.printa_cabecalho()

        for i in range(0, len(self._printa)):
            relatorio.write("\n")
            relatorio.write("\t> {} NÃO EXISTE EM {}\n".format(self._printa[i], nome_comparacao))

        relatorio.write("\n")
        relatorio.close()

    def printa_velocidade_max_min(self):
        self._texto = "VEL MIN > VEL MAX!"
        self.printa_linha()

    def printa_reservados(self):
        self._texto = "CAMPOS RESERVADOS FORA DO PADRÃO!"
        self.printa_linha()

    def printa_tempo(self):
        self.printa_tempos()

    def printa_duplicados(self):
        self._texto = "EXISTEM FZT DUPLICADOS!"
        self.printa_linha()

    def printa_ed3(self):
        self._texto = "VALOR TIPO DE ED3 NÃO PODE SER DIFERENTE DE 0 E 1!"
        self.printa_linha()

    def printa_an1(self):
        self._texto = "VALOR TIPO DE AN1 NÃO PODE SER DIFERENTE DE 0 E 1!"
        self.printa_linha()

    def printa_ed2(self):
        self._texto = "VALOR TIPO DE ED2 NÃO PODE SER DIFERENTE DE 0 E 1!"
        self.printa_linha()

    def printa_valor(self):
        self._texto = "EXISTEM VALORES MAX MENORES QUE VALORES MIN!"
        self.printa_linha()

    def printa_tag(self):
        # SE TAG_CADASTRADOS É NULO, ENTÃO EU DIGO QUE ELE NÃO FEZ VINCULO ALGUM;
        if (not self._printa):
            if (not self._marcador):
                self.printa_cabecalho()
            relatorio = open("DIAGNÓSTICO.TXT", "a", encoding="utf8")
            relatorio.write("\n")
            relatorio.write("\t> VOCÊ NÃO FEZ VINCULOS DE TAG EM SEU ARQUIVO!\n")
            relatorio.write("\n")
            relatorio.close()

        # MOSTRO QUAL IMPLEMENTO ESTÁ VINCULADO COM QUAL TAG, COM OU SEM OPERAÇÃO VINCULADA;
        # NESTED FOR, PARA TER ACESSO A CADA ITEM DA MATRIZ;
        if (not self._marcador):
            self.printa_cabecalho()
        for i in range(len(self._dados)):
            for j in range(len(self._printa)):
                # ENCONTRO O TAG CADASTRADO, E VERIFICO SE ELE TEM VINCULO COM A OPERAÇÃO;
                if (self._printa[j] == self._dados[i][4]):
                    # SE ELE TEM VINCULO COM OPERAÇÃO, MOSTRO QUAL FOI O VINCULO CRIADO, COM TAG-IMPLEMENTO-OPERAÇÃO;
                    if (self._dados[i][5] != ""):
                        relatorio = open("DIAGNÓSTICO.TXT", "a", encoding="utf8")
                        relatorio.write("\n")
                        relatorio.write("\t> VOCÊ VINCULOU O TAG {} COM O IMPLEMENTO {}\n".format(self._dados[i][4],
                                                                                                  self._dados[i][0]))
                        relatorio.write("\t> ESSE VINCULO FOI FEITO NA OPERACAO {}\n".format(self._dados[i][5]))
                        relatorio.close()
                    # NÃO TENDO VINCULO COM OPERAÇÃO, APENAS MOSTRO O VINCULO DELE DE TAG-OPERAÇÃO;
                    else:
                        relatorio = open("DIAGNÓSTICO.TXT", "a")
                        relatorio.write("\n")
                        relatorio.write("\t> VOCÊ VINCULOU O TAG {} COM O IMPLEMENTO {}\n".format(self._dados[i][4],
                                                                                                  self._dados[i][0]))
                        relatorio.close()

    def printa_tipo(self):
        self._texto = "EXISTEM TIPO DE OPERADORES FORA DO PADRÃO!"
        self.printa_linha()

    def printa_matricula(self):
        self._texto = "OS CÓDIGOS DE OPERADOR ESTAO DIFERENTES!"
        self.printa_linha()

    def printa_nao_nulo(self):
        self._texto = "ARQUIVO PRECISA ESTAR EM BRANCO!"
        self.printa_c_fase()

    def printa_virgula(self):
        self._texto = "EXISTEM VALORES COM VIRGULA!"
        self.printa_linha()

    def printa_entrada_nula(self):
        self._texto = "EXISTEM VALORES NULOS!"
        self.printa_linha()

    def printa_campos(self):
        self._texto = "O ARQUIVO NÃO ESTÁ COM OS CAMPOS VÁLIDOS!"
        self.printa_linha()

    def printa_caractere(self):
        self._texto = "ARQUIVO POSSUI EXCEDENTE DE CARACTERES! LIMITE DE 32!"
        self.printa_linha()

    def printa_cd_produtivo(self):
        self._texto = "CÓDIGO ESPECIAL INVALIDO!"
        self.printa_linha()

    def printa_codigos_duplicados(self):
        self._texto = "CÓDIGOS DUPLICADOS!"
        self.printa_cd_duplicados()

    def printa_pastas(self):
        self.printa_pastas_faltando()

    def printa_pastas_faltando(self):
        relatorio = open("DIAGNÓSTICO.TXT", "a", encoding="utf8")

        for i in range(0, len(self._printa)):
            relatorio.write("\n")
            relatorio.write("PASTA {} NÃO EXISTE NO DIRETORIO\n".format(self._printa[i]))

        relatorio.write("\n")
        relatorio.close()

if(__name__ == "__main__"):
    pass
