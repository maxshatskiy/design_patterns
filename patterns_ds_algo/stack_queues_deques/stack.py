class Empty(Exception):
    def __init__(self, message):
        super().__init__(self.message)

class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage.
    Example of adapter design pattern."""

    def __init__(self):
        """Create an empty stack."""
        self._data = [] # nonpublic list instance

    def __len__(self):
        """Return the number of elements in the stack"""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data)==0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._data.append(e)

    def top(self):
        """Return but not remove the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        """Remove and return the element from the top of the stack (LIFO)
        Raise Empty exception if the stack is empty.
        """
    if self.is_empty():
        raise Empty('Stack is empty')
    return self._data.pop()

def reverse_file(filename):
    """Overwrite given file with its contents line-by-line reversed. Stacks is used."""
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip('\n')) # re-inreset newlines when wrinting
    original.close()

    output = open(filename,'w')
    while not S.is_empty():
        output.write(S.pop()+'\n')
    output.close()

