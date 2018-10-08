
import time, threading
balance = 0
def change_her(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(10000):
        change_her(n)
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)



t = (1, ) # tuple
print(t)
