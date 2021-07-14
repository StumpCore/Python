import threading
import time
import os

path = "text.txt"
text = ""

def readFile():
    user = os.getlogin()
    global path, text
    while True:
        time_ = time.asctime()
        content = str(time_) + ": " + str(user)
        with open(path, "w") as f:
            f.write(content)

        with open(path, "r") as f:
            text = f.read()

        time.sleep(2)

def printloop():
    for x in range(10):
        print(text)
        time.sleep(1)


t1 = threading.Thread(target=readFile,daemon=True) #not important thread
t2 = threading.Thread(target=printloop)

t1.start()
t2.start()