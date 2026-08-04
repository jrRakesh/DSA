class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # 1. Check if list is empty
    def is_empty(self):
        return self.head is None

    # 2. Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 3. Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # 4. Insert at specific position
    def insert_at_position(self, data, position):
        if position < 0:
            print("Invalid position")
            return

        if position == 0:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        temp = self.head

        for _ in range(position - 1):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next

        if temp is None:
            print("Position out of range")
            return

        new_node.next = temp.next
        temp.next = new_node

    # 5. Delete from beginning
    def delete_from_beginning(self):
        if self.is_empty():
            print("List is empty")
            return

        self.head = self.head.next

    # 6. Delete from end
    def delete_from_end(self):
        if self.is_empty():
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next.next:
            temp = temp.next

        temp.next = None

    # 7. Delete by value
    def delete_by_value(self, value):
        if self.is_empty():
            print("List is empty")
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        prev = None
        curr = self.head

        while curr and curr.data != value:
            prev = curr
            curr = curr.next

        if curr is None:
            print("Value not found")
            return

        prev.next = curr.next

    # 8. Search
    def search(self, value):
        temp = self.head
        position = 0

        while temp:
            if temp.data == value:
                return position

            temp = temp.next
            position += 1

        return -1

    # 9. Count nodes
    def count_nodes(self):
        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        return count

    # 10. Display list
    def display(self):
        if self.is_empty():
            print("List is empty")
            return

        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # 11. Reverse list
    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev

    # 12. Clear list
    def clear(self):
        self.head = None


# Driver Program
sll = SinglyLinkedList()

sll.insert_at_end(10)
sll.insert_at_end(20)
sll.insert_at_end(30)

print("Initial List:")
sll.display()

sll.insert_at_beginning(5)
print("\nAfter inserting 5 at beginning:")
sll.display()

sll.insert_at_position(15, 2)
print("\nAfter inserting 15 at position 2:")
sll.display()

print("\nPosition of 20:", sll.search(20))

sll.delete_from_beginning()
print("\nAfter deleting from beginning:")
sll.display()

sll.delete_from_end()
print("\nAfter deleting from end:")
sll.display()

sll.delete_by_value(15)
print("\nAfter deleting 15:")
sll.display()

print("\nNumber of nodes:", sll.count_nodes())

sll.reverse()
print("\nAfter reversing:")
sll.display()