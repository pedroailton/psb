import os
import time
import threading

# Esse valor é declarado inicialmente como teto de execução do arquivo em 100% da CPU
valor = 1_000_000_000	#Escolher o valor de forma que demore 60s para ser executado

executando = True

def funcao(valor_temp):
	for i in range(valor_temp):
		z=i*i

def monitorPrioridade(tempo_inicio):
	global executando
	while executando:
		tempo_decorrido = time.time() - tempo_inicio

		## Lógica de variação do nice
		"""
		Dúvidas:
		Quanto o nice é capaz de influenciar no uso da CPU (qual a matemática por trás dele)?
		Quais os comandos para alterar o nice
		Qual o nice padrão de um processo do Linux
		Quais valores eu coloco como marco para aumentar ou diminuir o nice? Posso usar regras de 3 baseadas no meus valores base...
		"""

		time.sleep(1)

if __name__ == "__main__":
	start = time.time()

	thread_monitor = threading.Thread(target=monitor_de_prioridade, args=(start,))

	funcao(valor)

	executando = False
	thread_monitor.join()

	print(f"Duracao= {time.time()-start:.2f}")