stack = []

def push():
    while True:
        try:
            item = int(input("Enter an item: "))
            stack.append(item)
            break
        except ValueError:
            print("Only integers are accepted")

def pop():
    stack.pop(-1)

def peek():
    print(stack[-1])

def size():
    print(len(stack))

def isEmpty():
    if len(stack) == 0:
        return True
    else:
        return False

def isFull():
    if len(stack) == 6:
        return True
    else:
        return False

again = True

menu = ("1. push \n"
           "2. pop \n" 
           "3. peek \n" 
           "4. size \n" 
           "5. exit")
while again:
    print (menu)
    print(stack)

    while True:
        try:
            option = int(input("Enter your choice: "))
            if 1 <= option <= 5:
                break
            else:
                print("Invalid option please enter a number between 1 and 5")

        except ValueError:
            print("Only integers are accepted")

    if option == 1:
        if isFull():
            print ("Stack is full")
        else:
            push()

    elif option == 2:
        if isEmpty():
            print("Stack is empty")

        else:
            pop()

    elif option == 3:
        if isEmpty():
            print("Stack is empty")
        else:
            peek()

    elif option == 4:
        size()

    elif option == 5:
        again = False



