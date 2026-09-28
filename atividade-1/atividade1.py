import os
import time
import threading

def funcao(valor_temp):
    for i in range(valor_temp):
        z = i * i

# Coloque aqui o valor exato que você calibrou (ex: 2_481_000_000)
VALOR_CALIBRADO = 2_250_000_000 
executando = True 
nice_atual = 0  

def monitor_de_prioridade(start_real, start_cpu):
    global executando, nice_atual
    
    while executando:
        agora_real = time.time()
        agora_cpu = time.process_time()
        
        decorrido_real = agora_real - start_real
        decorrido_cpu = agora_cpu - start_cpu
        
        # Se a CPU estiver 5% atrasada em relação ao tempo real, estamos perdendo espaço.
        if decorrido_cpu < (decorrido_real * 0.95):
            if nice_atual > -20:
                # Desce 2 degraus de prioridade a cada 100ms. Atinge -20 em exato 1 segundo!
                nice_atual = max(-20, nice_atual - 2) 
                try:
                    os.setpriority(os.PRIO_PROCESS, os.getpid(), nice_atual)
                    print(f"[{decorrido_real:.1f}s] Concorrência! Acelerando processo (nice = {nice_atual})")
                except Exception as e:
                    pass
        
        # O sleep de 0.1s garante reação imediata contra qualquer oscilação do escalonador
        time.sleep(0.1)

if __name__ == "__main__":
    start_real = time.time()
    start_cpu = time.process_time()
    
    thread_monitor = threading.Thread(target=monitor_de_prioridade, args=(start_real, start_cpu))
    thread_monitor.start()
    
    funcao(VALOR_CALIBRADO)
    
    executando = False
    thread_monitor.join()
    
    print(f"Duracao= {time.time()-start_real:.2f}")
