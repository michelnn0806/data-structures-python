#A queue is a first in first out data structure
Queue = []

#When an item is enqueued it goes the back of the queue
def enqueue(item):
    Queue.append(item)

#When an item is dequeued the item at the front of the queue is removed
def dequeue():
    Queue.pop(0)

def peek():
    print(Queue[0])

def size():
    print(len(Queue))

def IsEmpty():
    if len(Queue) == 0:
        print("Queue is empty")

menu = ("1. Enqueue \n"
           "2. dequeue \n" 
           "3. peek \n" 
           "4. size \n" 
           "5. exit")