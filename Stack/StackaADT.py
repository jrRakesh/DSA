class Stack:
    def __init__(self):
        self.items = []

    # Push element onto stack
    def push(self, item):
        self.items.append(item)

    # Pop element from stack
    def pop(self):
        if self.is_empty():
            return "Stack Underflow"
        return self.items.pop()

    # Return top element
    def peek(self):
        if self.is_empty():
            return "Stack is Empty"
        return self.items[-1]

    # Check if stack is empty
    def is_empty(self):
        return len(self.items) == 0

    # Return size of stack
    def size(self):
        return len(self.items)

    # Display stack
    def display(self):
        print("Stack:", self.items)


# Driver Code
s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()

print("Top element:", s.peek())
print("Popped:", s.pop())

s.display()

print("Size:", s.size())
print("Is Empty?", s.is_empty())