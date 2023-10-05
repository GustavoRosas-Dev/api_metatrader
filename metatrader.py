# Referência: https://www.youtube.com/watch?v=KlyObTKogeY

from datetime import datetime
import MetaTrader5 as mt5
import pandas as pd


def inicializar_metatrader():
    if not mt5.initialize():
        print('A inicialização falhou. Código do erro:', mt5.last_error())
        quit()
    else:
        pass
        # print('Versão do pacote do Metatrader5:', mt5.__version__) # Ative apenas para ver se esta conectado


# Inicializa o MetaTrader 5 fora da função
inicializar_metatrader()


def obter_ultimo_fechamento(ativo):
    rates = mt5.copy_rates_from_pos(ativo, mt5.TIMEFRAME_M5, 0, 1)
    df = pd.DataFrame(rates)
    if not df.empty:
        df['time'] = pd.to_datetime(df['time'], unit='s')
        df = df.drop(df.columns[[0, 1, 2, 3, 5, 6, 7]], axis=1)
        ultimo_fechamento = df.iloc[0]['close']
        # print(df[-1:]) # Ative apenas para conferir o valor do ultimo fechamento
        return ultimo_fechamento
    else:
        return None


obter_ultimo_fechamento("EURUSD")
