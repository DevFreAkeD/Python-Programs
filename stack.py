class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty")
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty")
            return None

    def size(self):
        return len(self.items)

# Create a stack object
stack = Stack()

# Main loop for stack operations
while True:
    print("\nSelect operation:")
    print("1. Push")
    print("2. Pop")
    print("3. Show elements")
    print("4. Empty the stack")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        item = input("\nEnter element to push: ")
        stack.push(item)
        print("Element pushed onto the stack:", item)
    elif choice == '2':
        popped_item = stack.pop()
        if popped_item is not None:
            print("Popped element from the stack:", popped_item)
    elif choice == '3':
        print("\nElements in the stack:", stack.items)
    elif choice == '4':
        stack.items = []
        print("\nStack emptied")
    elif choice == '5':
        print("\nExiting program")
        break
    else:
        print("\nInvalid choice. Please enter a number from 1 to 5.")
