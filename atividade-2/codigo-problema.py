"""
35. Simulação de Checkout Inline com Cupom
Problema Real: Múltiplos usuários aplicado cupons limitados
Descrição: Threads disputam um número limitado de cupons adicionais
Objetivo: Garantir que cada cupom seja usado apenas uma vez
"""

# Erro forçado

import time
import threading

cupons_disponiveis = 20

def aplicarCupom():
  global cupons_disponiveis
  temp = cupons_disponiveis
  time.sleep(0.1)
  temp -= 1
  cupons_disponiveis = temp

threads = []
for t in range(30):
  thread = threading.Thread(name = "thread" + str(t),target = aplicarCupom)
  threads.append(thread)
  thread.start()

for t in threads:
  t.join()

print(f"cupons disponíveis: {cupons_disponiveis}")