import os
import time

def funcao(valor_temp):
	for i in range(valor_temp):
		z=i*i # Não deve ser criado nenhum if dentro desse loop

valor = 1_000_000_000	#Escolher o valor de forma que demore 60s para ser executado
start = time.time()
funcao(valor)
print(f"Duracao= {time.time()-start:.2f}")
