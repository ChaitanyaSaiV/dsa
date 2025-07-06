
""" kth-largest
Write a function, kth_largest, that takes in a list of numbers and a value, k. The function should return the k-th largest element of the list. """


def kth_largest(numbers, k):
  heap = heapify()
  for number in numbers:
    heap.insert(number)

  print(heap.list)


class heapify:
  def __init__(self):
    self.list = []

  def is_empty(self):
    return len(self.list) == 0
  
  def size(self):
    return len(self.list)
  
  def insert(self, val):
    self.list.append(val)
    self.sift_up(len(self.list) - 1)

  def swap(self,val1, val2):
    self.list[val1], self.list[val2] = self.list[val2] , self.list[val1]
  
  def sift_up(self, idx):

    while idx > 0:
      root_idx = (idx - 1) // 2
      if self.list[root_idx] > self.list[idx]:
        self.swap(root_idx, idx)
        idx = root_idx
      else:
        break
  def sift_down(self, idx):
    

  def extract(self):
    root = self.list[0]
    self.list[0] = self.list.pop()
    self.sift_down(0)
    return root

  



    




kth_largest([9,2,6,6,1,5,8,7], 3) # -> 7