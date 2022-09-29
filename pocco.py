import pyodbc
import pandas as pd
from os import system

server = ''
driver = ''
database = ''
username = ''
Authentication=''
port = ''
conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';AUTHENTICATION='+Authentication+';PORT='+port+';DATABASE='+database+';UID='+username)#+';PWD='+password)

cursor = conn.cursor()

class Usuario:
    def __init__(self, nome = str, sobrenome=str, email=str, bairro=str, nascimento='nascimento'):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.bairro = bairro
        self.nascimento = nascimento
    
    def get_u (self):
        return self.nome, self.sobrenome, self.email, self.bairro, self.nascimento
    
    def set_u (self, newnome, newsobrenome, newemail, newbairro, newnascimento):

        self.nome = newnome
        self.sobrenome = newsobrenome
        self.email = newemail
        self.bairro = newbairro
        self.nascimento = newnascimento
        novo_usario = f"INSERT INTO [schema].[table] VALUES ('{self.nome}','{self.sobrenome}','{self.email}','{self.bairro}','{self.nascimento}') "
        cursor.execute(novo_usario)
        cursor.commit()

class Cartao():
    def __init__(self,idc =int, idp=int, credito=float, tipoc=str, dtemissao='nascimento'):
        self.idc = idc
        self.idp = idp
        self.credito = credito
        self.tipoc = ['COMUM', 'ESTUDANTE', 'VALE-TRANSPORTE', 'IDOSO']
        self.dtemissao = dtemissao
    
    def getc(self):
        return  self.idc, self.idp, self.credito, self.tipoc, self.dtemissao

    def setc(self, newidc, newidp, newcredito, newtipoc, newdtemissao):
       
        self.idc = newidc
        self.idp = newidp
        self.credito = newcredito
        self.tipoc = newtipoc
        self.dtemissao = newdtemissao
        novocartao = f"INSERT INTO [schema].[table] VALUES ('{self.idc}' , '{self.idp}', '{self.credito}', '{self.tipoc}', '{self.dtemissao}')"
        cursor.execute(novocartao)
        cursor.commit()

class Onibus():
    def __init__(self, num_placa = int, num_linha=int, modelo_onibus = str, ano_fabricado = 'anofabrica', idm = int):
        self.num_placa = num_placa
        self.num_linha = num_linha
        self.modelo_onibus = modelo_onibus
        self.ano_fabricado = ano_fabricado
        self.idm = idm
    
    def geto(self):
        return self, self.num_placa, self.num_linha, self.modelo_onibus, self.ano_fabricado, self.idm
    
    def seto(self, newnum_placa, newnum_linha, newmodelo_onibus, newano_fabricado, newidm):
        self.num_placa = newnum_placa
        self.num_linha = newnum_linha
        self.modelo_onibus = newmodelo_onibus
        self.ano_fabricado = newano_fabricado
        self.idm = newidm
        novoonibus = f"INSERT INTO [schema].[table] VALUES ('{self.num_placa}' , '{self.num_linha}',\
             '{self.modelo_onibus}', '{self.ano_fabricado}', '{self.idm}')"
        cursor.execute(novoonibus)
        cursor.commit()

class Motorista():
    def __init__(self, idm = int, cnh= int, nome = str, sobrenome= str, dtnas= 'nascimento'):
        self.idm = idm
        self.cnh= cnh
        self.nome= nome
        self.sobrenome= sobrenome
        self.dtnas= dtnas
    
    def get_m(self):
        return self, self.cnh, self.dtnas, self.idm, self.nome, self.sobrenome
    
    def set_m(self, newcnh, newdtnas, newidm, newnome, newsobrenome):
        
        self.idm = newidm
        self.cnh= newcnh
        self.nome= newnome
        self.sobrenome= newsobrenome
        self.dtnas= newdtnas
        novomotorista = f"INSERT INTO [schema].[table] VALUES ('{self.idm}' , '{self.cnh}', '{self.nome}', '{self.sobrenome}', '{self.dtnas}')"
        cursor.execute(novomotorista)
        cursor.commit()

