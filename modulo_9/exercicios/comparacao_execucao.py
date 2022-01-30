import scrape_assincrono_concorrente, scrape_sincrono, scrape_assincrono_paralelo
from time import time


inicio_sincrono = time()
scrape_sincrono.execucao()
fim_sincrono = time()
print(f'o tempo de execução do scrape sincrono foi {abs(int(fim_sincrono - inicio_sincrono))} segundos')

inicio_concorrente = time()
scrape_assincrono_concorrente.execucao()
fim_concorrente = time()
print(f'o tempo de execução do scrape assincrono concorrente foi {abs(int(fim_concorrente - inicio_concorrente))} segundos')

inicio_paralelo = time()
scrape_assincrono_paralelo.execucao()
fim_paralelo = time()
print(f'o tempo de execução do scrape assincrono paralelo foi {abs(int(fim_paralelo - inicio_paralelo))} segundos')