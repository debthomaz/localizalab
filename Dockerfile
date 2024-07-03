FROM python:3.8.8
LABEL org.opencontainers.image.source https://github.com/debthomaz/localizalab
LABEL org.opencontainers.image.licenses MIT

WORKDIR /localizalab

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main.py df_fraud_credit.csv tabela_resultado_1.csv tabela_resultado_2.csv README.md /localizalab/

CMD ["python", "main.py"]