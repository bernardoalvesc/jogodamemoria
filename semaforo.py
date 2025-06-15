# semaforo.py

import threading

semaforo_p1 = threading.Semaphore(1)
semaforo_p2 = threading.Semaphore(0)
