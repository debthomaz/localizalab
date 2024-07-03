import pandas as pd
import numpy as np

# Transformando o arquivo .csv em um dataframe
df = pd.read_csv('df_fraud_credit.csv')

# Percentual de conformidade -antes da limpeza dos dados
registers = df[['location_region', 'amount', 'risk_score']].count()
print(f'\nRegistros:\n{registers}')

errors_amount = df['amount'].loc[(df['amount'] == 'none')].count()
print(f'\nDados inconsistentes:\namount: {errors_amount}')
errors_rscore = df['risk_score'].loc[(df['risk_score'] == 'none')].count()
print(f'risk_score: {errors_rscore}')
errors_locregion = df['location_region'].loc[(df['location_region'] == '0')].count()
print(F'location_region: {errors_locregion}')

compliance_amount = errors_amount / df['amount'].count()
print(f'\nPercentual de conformidade:\namount: {"{:.5f}".format(compliance_amount)}')
compliance_rscore = errors_rscore / df['risk_score'].count()
print(f'risk_score: {"{:.5f}".format(compliance_rscore)}')
compliance_locregion = errors_locregion / df['location_region'].count()
print(f'location_region: {"{:.5f}".format(compliance_rscore)}\n')


# Funções de limpeza do dataframe
def clean_dataframe(dataframe):
    # Removendo dados inconsistentes na coluna location_region
    error_locregion = dataframe.loc[(dataframe['location_region'] == '0')]
    result = dataframe.drop(error_locregion.index)
    # Removendo dados duplicados
    result = result.drop_duplicates()
    # Substituindo dados nulos para NaN
    result = result.replace('none', np.nan)
    return result

def set_datatype(dataframe, columns, type):
    # Alterando para o tipo de dado correto em cada coluna
    for column in columns:
        dataframe[column] = dataframe[column].astype(type)

def input_median(dataframe, columns):
    print(f'\nA quantidade de valores nulos é:\n{dataframe.isna().sum()}') 
    # Substituindo valores nulos pela média
    for column in columns:
        dataframe[column].fillna(dataframe[column].mean(), inplace=True)
    print(f'\nApós preencher os valores nulos com a média:\n{dataframe.isna().sum()}')

# Separando colunas por tipos
str_cols = ['location_region']
num_cols = ['amount', 'risk_score']
categorical_cols = ['transaction_type', 'purchase_pattern', 'age_group', 'anomaly']

# Limpando dataframe
df = clean_dataframe(df)
set_datatype(df, str_cols, 'string')
set_datatype(df, num_cols, 'float')
set_datatype(df, categorical_cols, 'category')
df.info()
input_median(df, num_cols)

# Percentual de conformidade -depois da limpeza dos dados
errors_amount = df['amount'].loc[(df['amount'] == 'none')].count()
print(f'\nDados inconsistentes:\namount: {errors_amount}')
errors_rscore = df['risk_score'].loc[(df['risk_score'] == 'none')].count()
print(f'risk_score: {errors_rscore}')
errors_locregion = df['location_region'].loc[(df['location_region'] == '0')].count()
print(F'location_region: {errors_locregion}')

compliance_amount = errors_amount / df['amount'].count()
print(f'\nPercentual de conformidade:\namount: {compliance_amount}')
compliance_rscore = errors_rscore / df['risk_score'].count()
print(f'risk_score: {compliance_rscore}')
compliance_locregion = errors_locregion / df['location_region'].count()
print(f'location_region: {compliance_rscore}\n')


# Funções para gerar as tabelas resultado 1 e 2
def location_per_riskscore(dataframe):
    # Listando as location_region de acordo com a média do risk_score
    result = dataframe.groupby('location_region')['risk_score'].mean().to_frame()
    # Ordenando o dataframe em ordem decrescente
    result = result.sort_values(by='location_region', ascending=False)
    # Salvando a tabela em um arquivo .csv
    result.to_csv('tabela_resultado_1.csv')

def address_bigger_sales(dataframe):
    # Filtrando por transaction_type = sale
    result = dataframe.loc[(df['transaction_type'] == 'sale')]
    # Ordenando por timestamp em ordem crescente
    result = result.sort_values(by='timestamp')
    # Pegando as 100 primeiras linhas
    result = result.head(100)
    # Ordenando esses valores por amount na ordem decrescente
    result = result.sort_values(by='amount', ascending=False)
    # Pegando as 3 primeiras linhas, que correspondem aos 3 maiores amounts
    result = result.head(3)
    # Deixando apenas as colunas timestamp, receiving_address e amount
    result = result[['timestamp', 'receiving_address', 'amount']]
    # Salvando a tabela em uma rquivo .csv
    result.to_csv('tabela_resultado_2.csv')

# Gerando as tabelas resultado
location_per_riskscore(df)
address_bigger_sales(df)
