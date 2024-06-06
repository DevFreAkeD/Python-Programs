class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty")
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty")
            return None

    def size(self):
        return len(self.items)

# Create a queue object
queue = Queue()

# Main loop for queue operations
while True:
    print("\nSelect operation:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Show elements")
    print("4. Empty the queue")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        item = input("\nEnter element to enqueue: ")
        queue.enqueue(item)
        print("Element enqueued:", item)
    elif choice == '2':
        dequeued_item = queue.dequeue()
        if dequeued_item is not None:
            print("Dequeued element from the queue:", dequeued_item)
    elif choice == '3':
        print("\nElements in the queue:", queue.items)
    elif choice == '4':
        queue.items = []
        print("\nQueue emptied")
    elif choice == '5':
        print("\nExiting program")
        break
    else:
        print("\nInvalid choice. Please enter a number from 1 to 5.")
