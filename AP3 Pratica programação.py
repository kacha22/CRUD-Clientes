import time

from Cadastros import *

arquivo_clientes = 'Cadastro_clientes.txt'
arquivo_motos = 'Cadastro_motos.txt'
arquivo_vendas = 'ArquivoDe_vendas.txt'
arquivoTemporario = 'ArquivoTemporario.txt'

Pula_linha()
print("*{:^80}*".format("\033[1;94mAguarde um segundo enquanto iniciamos nosso sistema!\033[m"))
Pula_linha()
time.sleep(2)
Pula_linha()
if not Arquivo_existe(arquivo_motos, arquivo_clientes, arquivo_motos, arquivoTemporario):
    Arquivo_nao_existe(arquivo_clientes, arquivo_motos, arquivo_vendas,arquivoTemporario)

time.sleep(2)
Pula_linha()
print("*{:^80}*".format("\033[1;94mBem-Vindo(a) a conssecionária Mais Motos!\033[m"))
Pula_linha()
print()
time.sleep(1)
while True:
    Pula_linha()
    print("*{:^80}*".format("\033[1;32mO que você deseja fazer?\033[m"))
    print('-' * 74)
    print("{:^80}".format('\033[;1m1 - Cadastrar um cliente.\n'
          '2 - Cadastrar uma moto.\n'
          '3 - Alterar dados cadastrais do Cliente.\n'
          '4 - Alterar dados cadastrais da Moto.\n'
          '5 - Excluir um cliente.\n'
          '6 - Excluir uma moto.\n'
          '7 - Consultar Cadastros de motos.\n'
          '8 - Consultar Cadastros de Clientes.\n'
          '9 - Fazer uma venda\n'
          '10 - Consultar Vendas\n'
          '11 - Consultar Venda especifica\033[m'))
    try:
        Pula_linha()
        opcao = int(input('\033[1;94mEscolha uma das opções acima: \033[m'))
        Pula_linha()
    except:
        Pula_linha()
        print('Digite apenas numeros!')
        opcao = int(input('\033[1;94mEscolha uma das opções acima: \033[m'))
        Pula_linha()



    if opcao == 1:
        try:
            Cadastrar_Cliente(arquivo_clientes)
            print('\033[1;94mCadastrando cliente, porfavor aguarde...\33[m')
        except:
            print('\033[1;31mPORFAVOR DIGITE SOMENTE OS DADOS SOLICITADOS!!\033[m')
            Cadastrar_Cliente(arquivo_clientes)
            print('\033[1;94mCadastrando cliente, porfavor aguarde...\33[m')
        time.sleep(3)



    elif opcao == 2:
        try:
            Cadastrar_moto(arquivo_motos)
            print('\033[1;94mCadastrando moto porfavor aguarde....\033[m')
        except:
            print('\033[1;31mPORFAVOR DIGITE SOMENTE OS DADOS SOLICITADOS!!\033[m')
            Cadastrar_moto(arquivo_motos)
            print('\033[1;94mCadastrando moto porfavor aguarde....\033[m')
        time.sleep(3)



    elif opcao == 3:
        Ler_arquivo(arquivo_clientes)
        try:
            AlterarDados_cliente(arquivo_clientes)
            print('\033[1;94mAlterando dados cadastrais  do cliente, aguarde....\033[m')
        except:
            print('\033[1;31mPORFAVOR DIGITE SOMENTE OS DADOS SOLICITADOS!!\033[m')
            AlterarDados_cliente(arquivo_clientes)
            Ler_arquivo(arquivo_clientes)
        time.sleep(3)


    elif opcao == 4:
        Ler_arquivo(arquivo_motos)
        try:
            AlterarDados_moto(arquivo_motos)
            print('\033[1;94mAlterando dados cadastrais aguarde....\033[m')
        except:
            print('\033[1;31mPORFAVOR DIGITE SOMENTE OS DADOS SOLICITADOS!!\033[m')
            AlterarDados_moto(arquivo_motos)
            print('\033[1;94mAlterando dados cadastrais aguarde....\033[m')
        time.sleep(3)

    elif opcao == 5:
        Ler_arquivo(arquivo_clientes)
        try:
            Apagar_cliente(arquivo_clientes)
            print('\033[1;94mApagando registro do cliente, por favor aguarde....\033[m')
        except:
            print('\033[1;31mPORFAVOR DIGITE SOMENTE OS DADOS SOLICITADOS!!\033[m')
            Ler_arquivo(arquivo_clientes)
            Apagar_cliente(arquivo_clientes)
        time.sleep(3)


    elif opcao == 6:
        Ler_arquivo(arquivo_motos)
        try:
            Apagar_moto(arquivo_motos)
            print('\033[1;94mApagando registro da moto, por favor aguarde....\033[m')
        except:
            print('\033[1;31mPORFAVOR DIGITE SOMENTE OS DADOS SOLICITADOS!!\033[m')
            Ler_arquivo(arquivo_motos)
            Apagar_moto(arquivo_motos)
        time.sleep(3)

    elif opcao == 7:
        print("*{:^80}*".format("\033[1;94mLista de motos cadastradas.\033[m"))
        LerArquivoMoto(arquivo_motos)
        time.sleep(3)


    elif opcao == 8:
        print("*{:^80}*".format("\033[1;94mLista de de Clientes cadastrados.\033[m"))
        Ler_arquivo(arquivo_clientes)
        time.sleep(3)


    elif opcao == 9:
        FazerUmaVenda(arquivo_clientes, arquivo_motos, arquivo_vendas)


    elif opcao == 10:
        ConsultarTodasasVendas(arquivo_vendas)
        print()
        time.sleep(4)

    elif opcao == 11:
        try:
            ConsultarumaVendaEspecifica(arquivoTemporario, arquivo_vendas)
            time.sleep(3)
        except:
            print('\033[1;31mDigite somente os numeros correspondentes ao Cliente!\033[m')
            ConsultarumaVendaEspecifica(arquivoTemporario, arquivo_vendas)

