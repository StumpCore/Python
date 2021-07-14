import threading

event = threading.Event() #Object that has the function to be triggered

def myfunction():
    print("Waiting for event to trigger...\n")
    event.wait()
    print("Performing action XYZ now...")

t1 = threading.Thread(target=myfunction)
t1.start()

x = input("Do you want to trigger the event (y/n)")
if x == "y":
    event.set()
else:
    print("Close Event.")