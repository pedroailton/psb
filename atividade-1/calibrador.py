import time

def funcao(valor_temp):
    for i in range(valor_temp):
        z = i * i

print("Iniciando calibração rápida. Aguarde alguns segundos...")

amostra_base = 50_000_000

start = time.time()
funcao(amostra_base)
tempo_gasto = time.time() - start

valor_ideal = int((amostra_base * 60) / tempo_gasto)

print("-" * 40)
print(f"Resultados da Calibração:")
print(f"A amostra de {amostra_base:,} iterações levou {tempo_gasto:.2f} segundos.")
print(f"\n=> COPIE ESTE VALOR PARA O SEU CÓDIGO FINAL: {valor_ideal}")
print("-" * 40)
