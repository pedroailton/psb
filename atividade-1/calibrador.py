import time

def funcao(valor_temp):
    for i in range(valor_temp):
        z = i * i

print("Iniciando calibração rápida. Aguarde alguns segundos...")

# 1. Definimos uma amostra base (um número alto o suficiente para ser mensurável, mas rápido)
amostra_base = 50_000_000

start = time.time()
funcao(amostra_base)
tempo_gasto = time.time() - start

# 2. Regra de três simples para descobrir a proporção para 60 segundos
# Se 'amostra_base' leva 'tempo_gasto'
# Então 'valor_ideal' leva '60'
valor_ideal = int((amostra_base * 60) / tempo_gasto)

print("-" * 40)
print(f"Resultados da Calibração:")
print(f"A amostra de {amostra_base:,} iterações levou {tempo_gasto:.2f} segundos.")
print(f"\n=> COPIE ESTE VALOR PARA O SEU CÓDIGO FINAL: {valor_ideal}")
print("-" * 40)
