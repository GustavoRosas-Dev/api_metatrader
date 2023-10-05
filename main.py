"""
    Passo 1:
        pip install "fastapi[all]"

    Passo 2:
        uvicorn main:app --reload

    Observação:
    - O nome do seu arquivo deve ser 'main.py' e o nome da sua pasta deve ser diferente de 'app'.

    Referência oficial: https://fastapi.tiangolo.com/tutorial/
    Outras referências: https://www.hashtagtreinamentos.com/criar-api-com-fastapi-em-python

"""

from fastapi import FastAPI, Query
from metatrader import inicializar_metatrader, obter_ultimo_fechamento

app = FastAPI()


# GET - Retorna informações da API
@app.get("/")
async def root():
    autor = "Gustavo Rosas"  # Você pode alterar o ativo conforme necessário
    api_nome = "MetaTrader 5"
    versao = "1.0"

    value = {"API": api_nome, "Versão": versao, "Criado por": autor}
    return value


# GET - Retorna o último valor de fechamento de 1 ativo apenas
@app.get("/eur-usd")
async def root():
    ativo = "EURUSD"  # Você pode alterar o ativo conforme necessário
    ultimo_fechamento = obter_ultimo_fechamento(ativo)

    if ultimo_fechamento:
        value = {f"{ativo}": ultimo_fechamento}
        return value
    else:
        return {"Erro": "Não foi possível obter o último fechamento."}


# GET - Retorna o último valor de fechamento de qualquer ativo, ex: /ultimo_fechamento/?ativo=AUDCHF
@app.get("/ultimo_fechamento/")
async def obter_fechamento(ativo: str = Query(default="EURUSD")):
    # Inicialize o MetaTrader 5 aqui ou em outro local apropriado
    inicializar_metatrader()

    ultimo_fechamento = obter_ultimo_fechamento(ativo)

    if ultimo_fechamento:
        value = {f"{ativo}": ultimo_fechamento}
        return value
    else:
        return {"Erro": f"Não foi possível obter o último fechamento para o ativo {ativo}."}



