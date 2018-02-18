# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data=[-1]
    self._data +=[int(s) for s in input().split()]
    assert n == len(self._data)-1

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def GenerateSwaps(self):
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    size=len(self._data)
    for i in range((len(self._data)-1)//2,0,-1):

      self.siftDown(i)

  def siftDown(self,i):
    root=i
    
    left=2*i
    right=2*i+1
    if left<=len(self._data)-1 and self._data[left]<self._data[root]:
      root=left
    if right<=len(self._data)-1 and self._data[right]<self._data[root]:
      root=right
    if i != root:
      self._swaps.append((i-1,root-1))
      
      self._data[i], self._data[root]=self._data[root],self._data[i]
      
      self.siftDown(root)  
  


  



        


  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()


if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
    

