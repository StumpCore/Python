import threading
import time

x = 8192

lock = threading.Lock()

def double():
    global x, lock #keyword for variable in the script, not function
    lock.acquire() #wait until lock is free, while not wait
    while x < 16384:
        x *= 2
        print(x)
        time.sleep(1)

    print("Reached the maximum!")
    lock.release()

def half():
    global x, lock
    lock.acquire()
    while x > 1:
        x /= 2
        print(x)
        time.sleep(1)

    print("Reched the minimum!")
    lock.release()

t1 = threading.Thread(target=half)
t2 = threading.Thread(target=double)

t1.start()
t2.start()


