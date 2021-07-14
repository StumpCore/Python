import queue
#queues are important for structure ways to get into and out of data

q = queue.Queue()

numbers = [10,20,30,40,50,60,70]

for number in numbers:
    q.put(number)

print(q.get())
print(q.get())

