import ctypes

class DynamicArray:

    def __init__(self):
        self._n = 0 # count actual elements
        self._capacity = 1 # default capacity
        self._A = self._make_array(self._capacity) #low-level array

    def __len__(self):
        return self._n

    def __getitem__(self, item):
        if not 0<=k<self._n:
            raise IndexError('invalid index')

    def append(self,obj):
        """Add object to end of the array"""
        if self._n == self._capacity: # array is full
            self._resize(2*self._capacity)
        self._A[self._n] = obj
        self._n +=1

    def _resize(self, c): #non public utility method
        """Resize internal array to capacity C"""
        B = self._make_array(c)
        for k in range(self._n):
            B[k]=self._A[k]
        self._A = B
        self._capacity=c

    def _make_array(self,c): # non public utility method
        """Return new array with capacity c."""
        return (c*ctypes.py_object)()