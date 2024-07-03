import os
import pandas as pd
import pytest
from main import clean_dataframe, set_datatype, input_median, location_per_riskscore, address_bigger_sales


def test_clean_dataframe():
    df = pd.DataFrame({'col1': [1, 2, 2, 3, 4], 'col2': ['B', 'A', 'A', 'none', 'none'], 'location_region': ['0', 'Africa', 'Africa', 'Asia', 'Asia']})
    df = clean_dataframe(df)
    assert df.shape == (3, 3)  # Verifica se os dados duplicados e inconsistências foram removidos
    assert df['col2'].isna().sum() == 2  # Verifica se 'none' foi substituído por NaN

def test_set_datatype():
    df = pd.DataFrame({'col1': [1.5, 2.5, 3.5], 'col2': ['a', 'b', 'c']})
    set_datatype(df, ['col1'], 'float')
    set_datatype(df, ['col2'], 'string')
    assert df['col1'].dtype == 'float'  # Verifica se o tipo de dado foi alterado para float
    assert df['col2'].dtype == 'string'  # Verifica se o tipo de dado foi alterado para string

def test_input_median():
    df = pd.DataFrame({'col1': [1, 2, None, 4], 'col2': [None, 2, 3, 4]})
    input_median(df, columns=['col1', 'col2'])
    assert df['col1'].isna().sum() == 0  # Verifica se os valores nulos foram preenchidos com a média
    assert df['col2'].isna().sum() == 0  # Verifica se os valores nulos foram preenchidos com a média

def test_location_per_riskscore():
    df = pd.DataFrame({'location_region': ['A', 'B', 'C'], 'risk_score': [0.5, 0.8, 0.6]})
    location_per_riskscore(df)
    assert os.path.exists('tabela_resultado_1.csv')  # Verifica se o arquivo 'tabela_resultado_1.csv' foi criado

def test_address_bigger_sales():
    df = pd.DataFrame({'transaction_type': ['sale', 'purchase', 'sale'],
                       'timestamp': [1563258442, 1562586542, 1573655896],
                       'receiving_address': [0xd37c6b8b5c6d362ee4ba439ddca3056f658cdd3e, 0xd37c6b8b5c6d362ee4ba598ddca3056f880cdd3e, 0xd62c6b8b5c6d362ee4ba439ddca3056f880cdd3e],
                       'amount': [10.8, 4.8, 65.1]})
    address_bigger_sales(df)
    assert os.path.exists('tabela_resultado_2.csv')  # Verifica se o arquivo 'tabela_resultado_2.csv' foi criado