from fastapi import FastAPI
from pydantic import BaseModel
from json import loads, dump


app = FastAPI()

@app.get('/')
async def root():
    return {'message' : 'Tudo ok'}

    
class Calc(BaseModel):
    var1: int
    var2: int
    operacao: str


@app.post('/calculadora')
async def novarota(calc: Calc):
    dicionario = calc.dict() # transforma os dados recebidos pelo post em dicionario python
    opera = dicionario['operacao'].lower().strip() # faz o tratamento da string relacionada a operação
    if opera == 'adicao':
        return dicionario['var1'] + dicionario['var2']
    if opera == 'subtracao':
        return dicionario['var1'] - dicionario['var2']
    if opera == 'divisao':
        return dicionario['var1'] / dicionario['var2']
    if opera == 'multiplicacao':
        return dicionario['var1'] * dicionario['var2']