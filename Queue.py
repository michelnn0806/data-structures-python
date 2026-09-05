#A queue is a first in first out data structure

Queue = []

#When an item is enqueued it goes the back of the queue
def enqueue():

    while True:
        try:
            number = int(input("Enter a number: "))
            Queue.append(number)
            break

        except ValueError:
            print("Please enter a number")


#When an item is dequeued the item at the front of the queue is removed
def dequeue():
    Queue.pop(0)

def peek():
    print(Queue[0])

def size():
    print(len(Queue))

def QueueEmpty():
    if len(Queue) == 0:
        return True
    else:
        return False

menu = ("1. Enqueue \n"
           "2. dequeue \n" 
           "3. peek \n" 
           "4. size \n" 
           "5. exit")

again = True

while again:
    print(menu)
    print(Queue)

    while True:
        try:
            option = int(input("Enter your choice: "))
            if 1 <= option <= 5:
                break
            else:
                print("Only numbers between 1 and 5 should be entered")

        except ValueError:
            print("Please enter a number")

    if option == 1:
        enqueue()

    elif option == 2:
        if QueueEmpty():
            print("Queue is empty")
        else:
            dequeue()

    elif option == 3:
        if QueueEmpty():
            print("Queue is empty")
        else:
            peek()

    elif option == 4:
        size()

    elif option == 5:
        again = False
