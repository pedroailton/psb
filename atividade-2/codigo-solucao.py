# Solução

import time
import threading

cupons_disponiveis = 20

usuarios_sem_cupom = 0 # Quantidade de usuários que não conseguiram cupom por indisponibilidade

trava = threading.Lock()

def aplicarCupomSeguro():
  global cupons_disponiveis
  global usuarios_sem_cupom
  
  trava.acquire()
  temp = cupons_disponiveis
  time.sleep(0.1)
  if temp > 0:
    temp -= 1
  else: 
    print(f"O número de cupons esgotou")
    usuarios_sem_cupom += 1
  cupons_disponiveis = temp
  trava.release()

threads = []
for t in range(30):
  thread = threading.Thread(name = "thread" + str(t),target = aplicarCupomSeguro)
  threads.append(thread)
  thread.start()

for t in threads:
  t.join()

print(f"usuários que não conseguiram o cupom: {usuarios_sem_cupom}")
print(f"cupons disponíveis: {cupons_disponiveis}")