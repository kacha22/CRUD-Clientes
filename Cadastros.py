import time


def Cadastrar_Cliente(arqv_clientes):

    nome = str(input('Digite o NOME do cliente: '))
    sobrenome = str(input('Digite o SOBRENOME do cliente: '))
    idade = int(input('Digite a IDADE do cliente: '))
    arqv_clientes = open(arqv_clientes, 'at')
    arqv_clientes.write(f'{nome};{sobrenome};{idade}\n')
    arqv_clientes.close()


def Cadastrar_moto(arqv_motos):
    marca = str(input('Digite a Marca da moto: '))
    modelo = str(input('Digite o Modelo: '))
    ano = int(input('Digite o ANO: '))
    arqv_motos = open(arqv_motos, 'at')
    arqv_motos.write(f'{marca};{modelo};{ano}\n')
    arqv_motos.close()

def AlterarDados_cliente(path):
    print('\033[1;94mSelecione qual cliente deseja alterar o cadastro.\n'
          'Escolha o numero ao lado do cliente, para alterar seu cadastro\n'
          'Ex: 1 para Diego.\033[m')
    linha = int(input('\033[;1mDigite o numero do cliente: \033[m'))
    nome = str(input('\033[;1mDigite o Nome: \033[m'))
    sobrenome = str(input('\033[;1mDigite o Sobrenome: \033[m'))
    idade = int(input('\033[;1mDigite a idade: \033[m'))
    with open(path, 'r') as f:
        texto = f.readlines()
    for linhas in texto:
        linhas.split(';')
    with open(path, 'w') as f:
        for i in texto:
            if texto.index(i) == linha:
                f.write(f'{nome};{sobrenome};{idade}\n')
            else:
                f.write(i)



def AlterarDados_moto(path):
    print("{:^80}".format('\033[1;94mSelecione qual Moto deseja alterar o cadastro.\n'
          'Escolha o numero ao lado da Moto, para alterar seu cadastro\n'
          'Ex: 1 para Honda.\033[m'))
    linha = int(input('\033[;1mDigite o numero da Moto: \033[m'))
    nome = str(input('\033[;1mDigite a Marca: \033[m'))
    sobrenome = str(input('\033[;1mDigite o Modelo: \033[m'))
    idade = int(input('\033[;1mDigite o Ano: \033[m'))
    with open(path, 'r') as f:
        texto = f.readlines()
    for linhas in texto:
        linhas.split(';')
    with open(path, 'w') as f:
        for i in texto:
            if texto.index(i) == linha:
                f.write(f'{nome};{sobrenome};{idade}\n')
            else:
                f.write(i)

def Apagar_cliente(path):
    print('Selecione o cliente que deseja excluir.')
    print('Ex: 1 - Carlos')
    apagar = int(input('Selecione o cliente: '))
    with open(path, 'r') as f:
        texto = f.readlines()
    with open(path, 'w') as f:
        for i in texto:
            if texto.index(i) == apagar:
                f.write(f'')
            else:
                f.write(i)

def Apagar_moto(path):
    print('Selecione a Moto que deseja excluir.')
    print('Ex: 1 - Honda')
    apagar = int(input('Selecione a moto: '))
    with open(path, 'r') as f:
        texto = f.readlines()
    with open(path, 'w') as f:
        for i in texto:
            if texto.index(i) == apagar:
                f.write(f'')
            else:
                f.write(i)


def Arquivo_existe(nome1, nome2, nome3, nome4):
    try:
        arq1 = open(nome1, 'rt')
        arq2 = open(nome2, 'rt')
        arq3 = open(nome3, 'rt')
        arq4 = open(nome4, 'rt')
        arq1.close()
        arq2.close()
        arq3.close()
        arq4.close()
        print("*{:^80}*".format("\033[1;31mVocê já tem os arquivos necessários!\033[m"))
        Pula_linha()
    except FileNotFoundError:
        return False
    else:
        return True


def Arquivo_nao_existe(nome1, nome2, nome3, nome4):
    try:
        print("*{:^80}*".format("\033[1;31mCriando os arquivos necessários para o banco de dados!\033[m"))
        Pula_linha()
        time.sleep(3)
        arq1 = open(nome1, 'wt+')
        arq2 = open(nome2, 'wt+')
        arq3 = open(nome3, 'wt+')
        arq4 = open(nome4, 'wt+')
        arq1.close()
        arq2.close()
        arq3.close()
        arq4.close()
    except:
        print('Houve um ERRO ao criar o arquivo!')
    else:
        time.sleep(2)
        Pula_linha()
        print("*{:^80}*".format(f"\033[1;34mArquivo {nome1} criado com sucesso!\033[m"))
        Pula_linha()
        time.sleep(3)
        Pula_linha()
        print("*{:^80}*".format(f"\033[1;34mArquivo {nome2} criado com sucesso!\033[m"))
        Pula_linha()
        time.sleep(3)
        Pula_linha()
        print("*{:^80}*".format(f"\033[1;34mArquivo {nome3} criado com sucesso!\033[m"))
        Pula_linha()
        time.sleep(3)
        print("*{:^80}*".format(f"\033[1;34mArquivo {nome4} criado com sucesso!\033[m"))

def FazerUmaVenda(arqvCliente, arqvMoto,arqvVenda):
    Ler_arquivo(arqvCliente)
    Pula_linha()
    print("*{:^80}*".format("\033[1;94mEx: Para escolher o cliente Rodrigo aperte a tecla 1\n"
                            "Para escolher a moto que o cliente vai comprar aperte a tecla 2\033[m"))
    Pula_linha()
    selecaoCliente = int(input('Digite o numero do Cliente que vai comprar a Moto: '))
    Ler_arquivo(arqvMoto)
    selecaoMoto = int(input('Digite o numero da moto que o Cliente vai comprar: '))
    with open(arqvCliente, 'r') as ler:
        lendo = ler.readlines()
        for linha in lendo:
            indexDaLinha = linha.split(';')
            if lendo.index(linha) == selecaoCliente:
                escrever = open(arqvVenda, 'a+')
                escrever.write(f'{indexDaLinha[0]};{indexDaLinha[1]};')
    with open(arqvMoto, 'r') as ler1:
        lendo1 = ler1.readlines()
        for linha1 in lendo1:
            indexDaLinha1 = linha1.split(';')
            if lendo1.index(linha1) == selecaoMoto:
                escrever1 = open(arqvVenda, 'a+')
                escrever1.write(f'{indexDaLinha1[0]};{indexDaLinha1[1]};{indexDaLinha1[2]}')


def ConsultarTodasasVendas(arquivoVendas):
        with open(arquivoVendas, 'rt') as ler1:
            lendo = ler1.readlines()
        index = 0
        for linha in lendo:
            index += 1
            vendas = linha.split(';')
            Pula_linha()
            print(f'{index} - {vendas[0]}')
            Pula_linha()
            print(f'\033[1;94m{vendas[0]} comprou a seguinte moto.\n'
                  f'Marca da moto: {vendas[2]}\n'
                  f'Modelo da moto: {vendas[3]}\n'
                  f'Ano de fabricação: {vendas[4]}\033[m')

def ConsultarumaVendaEspecifica(arquivoTemp, arquivoVendas):
    with open(arquivoVendas, 'rt') as ler1:
        lendo = ler1.readlines()
    index = 0
    Pula_linha()
    print(f'Selecione o cliente que você deseja consultar a venda\n'
          f'Ex. Para o cliente Mariana digite o numero ao seu lado esquedo.')
    for linha in lendo:
        vendas = linha.split(';')
        print()
        print(f'{index} - {vendas[0]}')
        index += 1
        print()
    selecionaCliente = int(input('Digite o numero do cliente: '))
    with open(arquivoVendas, 'r') as arq:
        variavel = arq.readlines()
        cliente = variavel[selecionaCliente]
    with open(arquivoTemp, 'w') as temp:
        temp.write(cliente)
    with open(arquivoTemp, 'r') as arq:
        texto = arq.readlines()
        for i in texto:
            dados = i.split(';')
            print()
            print(f'\033[1;34m{dados[0]} comprou a seguinte moto:\n'
                  f'Marca: {dados[2]}\n'
                  f'Modelo: {dados[3]}\n'
                  f'Ano de fabricação: {dados[4]}\033[m')


def Ler_arquivo(nome):
    index = 0
    try:
        arq = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        for linha in arq:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            Pula_linha()
            print(f'{index} - Nome: {dado[0]}       Sobrenome: {dado[1]}      Idade: {dado[2]}')
            index += 1
            Pula_linha()
    finally:
        arq.close()

def LerArquivoMoto(nome):
    index = 0
    try:
        arq = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        for linha in arq:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            Pula_linha()
            print(f'{index} - Marca: {dado[0]}      Modelo: {dado[1]}       Ano de fabricação: {dado[2]}')
            index += 1
            Pula_linha()
    finally:
        arq.close()

def Pula_linha():
    print(f'-+' * 37)
