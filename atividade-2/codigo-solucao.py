# Solução

import time
import threading

cupons_disponiveis = 20

trava = threading.Lock()

def aplicarCupomSeguro():
  global cupons_disponiveis
  trava.acquire()
  temp = cupons_disponiveis
  time.sleep(0.1)
  if temp > 0:
    temp -= 1
  else: 
    print(f"O número de cupons esgotou")
  cupons_disponiveis = temp
  trava.release()

threads = []
for t in range(30):
  thread = threading.Thread(name = "thread" + str(t),target = aplicarCupomSeguro)
  threads.append(thread)
  thread.start()

for t in threads:
  t.join()

print(f"cupons disponíveis: {cupons_disponiveis}")