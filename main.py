from pocco import *
import pandas as pd
import pyodbc
from os import system


# CADASTRAR!
def cadastro_usuario():
    novo_usario = Usuario()
    nome = str(input('Nome que deseja cadastrar: '))
    sobrenome = str(input('Sobrenome: '))
    bairro = str(input('Bairro: '))
    email = str(input('E-mail para cadastro: '))
    dia = int(input('[SEGUIR ESTE FORMADO - DD]Dia do nascimento: '))
    mes = int(input('[SEGUIR ESTE FORMADO - MM]Mes do nascimento: '))
    ano = int(input('[SEGUIR ESTE FORMADO  - YYYY]Ano do nascimento: '))
    dtnas = f'{ano}-{mes}-{dia}'
    novo_usario.set_u(nome, sobrenome, bairro, email, dtnas)
    print('Usuario cadastrado!')
    menu()


def cadastrar_cartao():
    novocartao = Cartao()
    idc = int(input('Informe o seu ID do seu cartão: '))
    idp = int(input('Informe o seu ID do seu usuário: '))
    credito = float(input('Informe o valor que deseja: '))
    tipoc = str(input("""
        [1] COMUM
        [2] ESTUDANTE
        [3] VALE-TRANSPORTE   
        [3] IDOSO
        Escolhe o tipo do seu cartão: """))

    if tipoc == 1:
        tipoc = 'COMUM'

    elif tipoc == 2:
        tipoc = 'ESTUDANTE'

    elif tipoc == 3:
        tipoc = 'VALE-TRANSPORTE'

    elif tipoc == 4:
        tipoc = 'IDOSO'

    else:
        print('Selecione uma opção válida')
        cadastrar_cartao()

    dia = int(input('[SEGUIR ESTE FORMADO - DD]Dia da emissão: '))
    mes = int(input('[SEGUIR ESTE FORMADO - MM]Mes da emissão: '))
    ano = int(input('[SEGUIR ESTE FORMADO  - YYYY]Ano da emissão: '))
    dtemissao = f'{ano}-{mes}-{dia}'
    novocartao.setc(idc, idp, credito, tipoc, dtemissao)
    print('Cartão cadastrado')
    menu()


def cadastrar_onibus():
    novoonibus = Onibus()
    num_placa = int(input('Informe o número da placa do veículo: '))
    num_linha = int(input('Informe o número da linha do veículo: '))
    modelo_onibus = str(input('Informe o modelo do veículo: '))
    dia = int(input('[SEGUIR ESTE FORMADO - DD]Dia da fabricação: '))
    mes = int(input('[SEGUIR ESTE FORMADO - MM]Mes da fabricação: '))
    ano = int(input('[SEGUIR ESTE FORMADO  - YYYY]Ano da fabricação: '))
    ano_fabricado = f'{ano}-{mes}-{dia}'
    idm = int(input('Informe o ID do motorista: '))
    novoonibus.seto(num_placa, num_linha, modelo_onibus, ano_fabricado, idm)
    print('Onibus cadastrado')
    menu()


def cadastrar_motorista():
    novomotorista = Motorista()
    idm = int(input('Informe o ID do motorista: '))
    cnh = int(input('Informe o número da CNH: '))
    nome = str(input('Informe o seu nome: '))
    sobrenome = str(input('Informe o seu sobrenome: '))
    dia = int(input('[SEGUIR ESTE FORMADO - DD]Dia do nascimento: '))
    mes = int(input('[SEGUIR ESTE FORMADO - MM]Mes do nascimento: '))
    ano = int(input('[SEGUIR ESTE FORMADO  - YYYY]Ano do nascimento: '))
    dtnas = f'{ano}-{mes}-{dia}'
    novomotorista.set_m(idm, cnh, nome, sobrenome, dtnas)
    print('Motorista cadastrado')
    menu()


# VER CADASTRADOS
def usuarios_cadastrados():
    view_user = pd.read_sql("SELECT * FROM [schema].[table];", conn)
    dt = pd.DataFrame(view_user)
    df = dt.to_string(index=False)
    print(df)
    menu()


def cartoes_cadastrados():
    view_cartoes = pd.read_sql("SELECT * FROM [schema].[table];", conn)
    dt = pd.DataFrame(view_cartoes)
    df = dt.to_string(index=False)
    print(df)
    menu()


def onibus_cadastrados():
    view_onibus = pd.read_sql("SELECT * FROM [schema].[table];", conn)
    dt = pd.DataFrame(view_onibus)
    df = dt.to_string(index=False)
    print(df)
    menu()


def motoristas_cadastrados():
    view_motoristas = pd.read_sql("SELECT * FROM [schema].[table];", conn)
    dt = pd.DataFrame(view_motoristas)
    df = dt.to_string(index=False)
    print(df)
    menu()


def menu():
    print("""
    [1] Cadastrar
    [2] Cadastros
    [3] Fechar aplicativo """)

    try:
        opcao = int(input('Escolha a opcao desejada: '))

        if opcao == 1:
            print(""" QUAL OPÇÃO PARA EFETUAR O CADASTRO
            [1] Cadastrar usuário
            [2] Cadastrar cartao
            [3] Cadastrar onibus
            [4] Cadastrar motorista
            [5] Menu   """)
            cadastrar = int(input('Escolha a opção: '))
            if cadastrar == 1:
                cadastro_usuario()
            elif cadastrar == 2:
                cadastrar_cartao()
            elif cadastrar == 3:
                cadastrar_onibus()
            elif cadastrar == 4:
                cadastrar_motorista()
            else:
                print('Opção não disponivel')
                menu()

        elif opcao == 2:
            views = int(input("""
            [1] Usuários cadastrados
            [2] Cartões cadastrados
            [3] Onibus cadastrados
            [4] Motoristas cadastrados
            [5] Menu
            Escolha a opçao desejada: """))
            if views == 1:
                usuarios_cadastrados()
            elif views == 2:
                cartoes_cadastrados()
            elif views == 3:
                onibus_cadastrados()
            elif views == 4:
                motoristas_cadastrados()
            else:
                print('Opção não disponivel')
                menu()

        elif opcao == 3:
            print('Volte sempre!')
            exit()

        else:
            print('Opção não disponivel')
            menu()

    except ValueError:
        print('\033[91m        Tente novamente\033[0m')
        menu()


menu()
