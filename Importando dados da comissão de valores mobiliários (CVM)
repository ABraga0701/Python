#Importando dados_cvm

#Importando bibliotecas

import pandas as pd
import requests
import zipfile

pd.options.display.float_format = '{:.4f}'.format

#Definindo range de data

ano = "2023"
mes = "10"
url =f'https://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/inf_diario_fi_{ano}{mes}.zip'

#Fazendo o download dos arquivos em csv

download = requests.get(url)

with open (f"inf_diario_fi_{ano}{mes}.zip","wb") as arquivo_cvm:
    arquivo_cvm.write(download.content)

arquivo_zip = zipfile.ZipFile(f"inf_diario_fi_{ano}{mes}.zip")

#Abrindo o arquivo

dados_fundo = pd.read_csv(arquivo_zip.open(arquivo_zip.namelist()[0]), sep = ";", encoding = 'ISO-8859-1')

dados_fundo

#Abrindo os dados cadastrais

dados_cadastro = pd.read_csv('https://dados.cvm.gov.br/dados/FI/CAD/DADOS/cad_fi.csv', sep=";", encoding='ISO-8859-1')

dados_cadastro = dados_cadastro[['CNPJ_FUNDO', 'DENOM_SOCIAL']]

dados_cadastro = dados_cadastro.drop_duplicates()

dados_cadastro

#Ordenar valores por data

data_inicio_mes = (dados_fundo['DT_COMPTC'].sort_values(ascending= True).unique())[0]
data_fim_mes = (dados_fundo['DT_COMPTC'].sort_values(ascending= True).unique())[-1]

dados_fundo_filtrado = dados_fundo[(dados_fundo['DT_COMPTC'].isin([data_inicio_mes, data_fim_mes]))]

dados_fundo_filtrado

#Combinar dataframes com base final

base_final = pd.merge(dados_fundo_filtrado, dados_cadastro, how= "left", left_on=["CNPJ FUNDO"], right_on=["CNPJ_FUNDO"])

base_final = base_final[['CNPJ_FUNDO', 'DENOM_SOCIAL', 'DT_COMPTC', 'VL_QUOTA', 'VL_PATRIM_LIQ', 'NR_COTST']]

base_final

