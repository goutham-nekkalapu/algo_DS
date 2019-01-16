
# max heap 
class max_heap(object):
    def __init__(self):
        self.heap = [-1]
        self.index = 0 

    # used for populating the values in heap while testing the heap 
    def temp_insert(self, value):
        self.heap.append(value)
        self.index += 1

    def print_heap(self):
        return self.heap
 
    # returns the max element of the heap 
    def max_value(self):
        if self.index == 0:
           return (False,)
        else:
           return (True,self.heap[1])

    # inserts an elment into a heap 
    # complexity : O(logn) (base-2)
    def insert(self, value):
        # creating an entry in list for index val of 'pos'
        self.heap.append(value)
        self.index += 1 
        pos = self.index 
        
	# bubbling the new_value up the heap depending on its value 
        while pos > 1 and  value > self.heap[pos//2]:
            self.heap[pos] = self.heap[pos//2]
            pos = pos//2
        self.heap[pos] = value

    # returns the location of next child to be used for maintain maxheap property 
    def maxChild(self,i):
        if i * 2 + 1 > self.index:
           return i * 2
        else:
           if self.heap[i*2] > self.heap[i*2+1]:
              return i * 2
           else:
              return i * 2 + 1 

    # deletes the max element, returns True upon success, False if heap is empty 
    # complexity : O(logn) (base-2)
    def delete_max(self):
        # checking if heap is empty 
        if self.index == 0: #empty heap 
           return False
        elif self.index == 1: #only one element left in heap
           value = self.heap.pop() 
           self.index -= 1
           return True

        #deleting the last element  from heap  
        value = self.heap.pop() 
        self.index -= 1
        self.heap[1] = value  #inserting the last element as root
        pos = 1
       
        # bubbling the new value down 
        while pos*2 <= self.index:
           mc = self.maxChild(pos)   
           if self.heap[pos] < self.heap[mc]:
              tmp = self.heap[pos]
              self.heap[pos] = self.heap[mc]
              self.heap[mc] = tmp 
           pos = mc 
        return True 
          

if __name__ == "__main__":
   h1 = max_heap() 

   '''
   h1.temp_insert(6)
   h1.temp_insert(7)
   h1.temp_insert(12)
   h1.temp_insert(10)
   h1.temp_insert(15)
   h1.temp_insert(17)
   '''
   h1.insert(10)
   h1.insert(5)
   h1.insert(21)
   h1.insert(2)
   
   print(h1.print_heap())

   print("------\n") 
   print(h1.max_value())
   h1.delete_max()
   print(h1.print_heap())
   
   print("------\n") 
   print(h1.max_value())
   h1.delete_max()
   print(h1.print_heap())

   print("------\n") 
   print(h1.max_value())
   h1.delete_max()
   print(h1.print_heap())

   print("------\n") 
   print(h1.max_value())
   h1.delete_max()
   print(h1.print_heap())

   '''
   h1.delete_min()
   print(h1.min_value())
   print(h1.min_value()[1])
   '''
 
