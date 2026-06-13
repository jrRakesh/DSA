from collections import deque


class QueueADT:
	def __init__(self):
		self.items = deque()

	def is_empty(self):
		return len(self.items) == 0

	def size(self):
		return len(self.items)

	def enqueue(self, item):
		self.items.append(item)

	def dequeue(self):
		if self.is_empty():
			return "Queue is empty"
		return self.items.popleft()

	def front(self):
		if self.is_empty():
			return "Queue is empty"
		return self.items[0]

	def display(self):
		return list(self.items)

	def clear(self):
		self.items.clear()

	def __str__(self):
		return str(list(self.items))


if __name__ == "__main__":
	queue = QueueADT()
	for value in [10, 20, 30]:
		queue.enqueue(value)

	print("Queue:", queue)
	print("Size:", queue.size())
	print("Front element:", queue.front())
	print("Deleted element:", queue.dequeue())
	print("Queue after deletion:", queue)
