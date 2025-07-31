""" heap insertion
Implement the insert method for the existing class. The method should properly add a given value into the heap, maintaining min heap order and height balance.

Start by watching the approach video. You'll also want to follow along with the walkthrough video. 

You won't know how to implement this if it is your first time dealing with heaps. """


class MinHeap:
  def __init__(self):
    self.list = []
    
  def is_empty(self):
    return len(self.list) == 0

  def size(self):
    return len(self.list)

  def swap(self, index, parent):
    self.list[parent], self.list[index] = self.list[index], self.list[parent]
    return

  def sip_down(self, index):
    while index > 0:
      parent = (index - 1) // 2
      if self.list[parent] > self.list[index]:
        self.swap(index, parent)
        index = parent
      else:
        break

    return
        
      
  def insert(self, val):
    self.list.append(val)
    index = self.size() - 1

    self.sip_down(index)
    return
    

heap = MinHeap()
heap.insert(12)
heap.insert(13)
heap.insert(11)
heap.insert(4)
heap.insert(20)
heap.insert(9)
heap.insert(22)
heap.insert(14)

#
#               4
#            /    \
#          11      9
#         / \    /  \
#       13  20  12  22
#      /
#    14
#
# [ 4, 11, 9, 13, 20, 12, 22, 14 ]