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
    
  def insert(self, val):
    self.list.append(val)
    self.sift_up(self.size() - 1)
      
  def sift_down(self, index):
    current_index = index
    while current_index < self.size() - 1:
      left_child_index = current_index * 2 + 1
      right_child_index = current_index * 2 + 2
      
      left_child_val = float("inf") if left_child_index >= self.size() else self.list[left_child_index]
      right_child_val = float("inf") if right_child_index >= self.size() else self.list[right_child_index]
      
      smaller_child_val = left_child_val if left_child_val < right_child_val else right_child_val
      smaller_child_index = left_child_index if left_child_val < right_child_val else right_child_index
      
      if self.list[current_index] > smaller_child_val:
        self.swap(current_index, smaller_child_index)
        current_index = smaller_child_index
      else:
        break
      
  def extract_min(self):
    if self.is_empty():
      return None
    
    if self.size() == 1:
      return self.list.pop()
    
    min_val = self.list[0]
    self.list[0] = self.list.pop()
    self.sift_down(0)
    return min_val








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

