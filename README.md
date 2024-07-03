# Desafio Técnico - Localiza

Olá! Eu sou a Débora, e este é a minha pipeline de dados para o desafio técnico da Localiza.

## Informações

Utilizei as bibliotecas `pandas` e `numpy`. A pipeline não faz uma análise tão profunda do dataset, mas tem o necessário para a preparação dos dados para gerar as duas tabelas solicitadas.

### Limpeza dos dados

`clean_dataframe()` -> Remove dados duplicados e substitui dados inconsistente por NaN

`set_datatype()` -> Define o tipo de dado correto em cada coluna

`input_median()` -> Substitui valores nulos pela média

### Gerando tabelas

- `location_per_riskscore()` -> Gera uma tabela com a média de `risk_score` por `location_region`

- `address_bigger_sales()` -> Gera uma tabela com 3 `receiving_address` cujas vendas (`transaction_type`==`sale`) tiveram maior `amount` recentemente (> `timestamp`)


## Instruções para execução

A aplicação está em um container, então com Docker instalado e rodando em sua máquina, você deve executar o código:

```
docker build -t localizalab .
```

#### E pronto, agora você já pode rodar a pipeline no container criado :)
#

- Para realizar os testes unitários nas funções, basta executar o código dentro da pasta `testes`:

```
pytest test_main.py
```
