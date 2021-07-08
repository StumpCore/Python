import threading
#useful when needing several tasks ( like in games, walking and shooting)

def function1():
    for x in range(10000):
        print("One")

def function2():
    for x in range(10000):
        print("Two")

t1 =threading.Thread(target = function1)
t2 =threading.Thread(target = function2)

t1.start()
t2.start()

