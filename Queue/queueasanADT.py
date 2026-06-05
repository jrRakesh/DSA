class QueueADT:
	def __init__(self):
		self.items = []

	def is_empty(self):
		return len(self.items) == 0

	def enqueue(self, item):
		self.items.append(item)

	def dequeue(self):
		if self.is_empty():
			return "Queue is empty"
		return self.items.pop(0)

	def front(self):
		if self.is_empty():
			return "Queue is empty"
		return self.items[0]

	def display(self):
		return self.items


if __name__ == "__main__":
	queue = QueueADT()
	queue.enqueue(10)
	queue.enqueue(20)
	queue.enqueue(30)

	print("Queue:", queue.display())
	print("Front element:", queue.front())
	print("Deleted element:", queue.dequeue())
	print("Queue after deletion:", queue.display())
