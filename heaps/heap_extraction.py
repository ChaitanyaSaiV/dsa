""" heap deletion
Implement the extract_min method for the existing class. 

The method should return and remove the smallest value in the heap, maintaining min heap order and height balance.

Start by watching the approach video. You'll also want to follow along with the walkthrough video. 

You won't know how to implement this if it is your first time dealing with heaps. """


class MinHeap:
  def __init__(self):
    self.list = []
    
  def is_empty(self):
    return len(self.list) == 0

  def size(self):
    return len(self.list)
  
  def swap(self, index_1, index_2):
    self.list[index_1], self.list[index_2] = self.list[index_2], self.list[index_1]
  
  def sift_up(self, index):
    current_index = index
    while current_index > 0:
      parent_index = (current_index - 1) // 2
      if self.list[current_index] < self.list[parent_index]:
        self.swap(current_index, parent_index)
        current_index = parent_index
      else:
        break

  def sift_down(self, index):
    current_index = index
    size = self.size()
    print(current_index)
    while current_index < size:
      left_index = 2 * current_index + 1
      right_index = 2 * current_index + 2
      if left_index > size - 1:
        left_val = float("inf")
      else:
        left_val = self.list[left_index]

      if right_index > size - 1:
        right_val = float("inf")
      else:
        right_val = self.list[right_index]
      
      if left_val < right_val:
        swap_val = left_val
        swap_index = left_index
      else:
        swap_val = right_val
        swap_index = right_index

      if self.list[current_index] > swap_val:
        self.swap(swap_index, current_index)
        current_index = swap_index
      else:
        break
    return
        
    
  def insert(self, val):
    self.list.append(val)
    self.sift_up(self.size() - 1)
      
  def extract_min(self):
    value = self.list[0]
    self.list[0] = self.list.pop()
    self.sift_down(0)
    return value


heap = MinHeap()
heap.insert(12)
heap.insert(13)
heap.insert(11)
heap.insert(4)
heap.insert(20)
heap.insert(9)
heap.insert(22)
heap.insert(14)
heap.extract_min() # -> 4
heap.extract_min() # -> 9
heap.extract_min() # -> 11

