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
      
  def insert(self, val):
    self.list.append(val)

    idx = self.list.index(val)

    self.sip_index(idx)
  
  def sip_index(self, idx):

    while idx > 0:
      parent_index = (idx - 1) // 2
      if self.list[parent_index] > self.list[idx]:
        self.list[parent_index], self.list[idx] =  self.list[idx], self.list[parent_index]
        idx = parent_index
      else:
        break
    

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