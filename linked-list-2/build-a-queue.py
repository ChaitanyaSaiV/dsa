""" build a queue
Implement the enqueue and dequeue methods for the existing class. 

The enqueue method should add a given value into the queue. 

The dequeue should return and remove an item from the queue following first-in, first-out order.

Your implementation should use a linked-list and not any built in containers. """

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

class Queue:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0
    
  def enqueue(self, val):
    dummy = Node(val)
    if self.head == None:
      self.head = dummy
      self.tail = dummy
    else:
      self.tail.next = dummy
      self.tail = self.tail.next

    self.size += 1

  def dequeue(self):
    dummy = self.head
    self.head = self.head.next
    self.size -= 1
    return dummy.val



queue = Queue()
queue.enqueue("a")
queue.size # -> 1
queue.dequeue() # -> a
queue.enqueue("b")
queue.enqueue("c")
queue.size # -> 2
queue.dequeue() # -> b
queue.dequeue() # -> c
queue.size # -> 0