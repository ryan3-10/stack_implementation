class Stack:
    def __init__(self):
        self.__data = []
        self.__size = 0
    
    def push(self, item):
        self.__data.insert(0, item)
        self.__size += 1
    
    def pop(self):
        if self.__size == 0:
            raise IndexError("This stack is empty")
        
        popped_item = self.__data[0]
        self.__data.remove(popped_item)
        self.__size -= 1

        return popped_item
    
    def top(self):
        if self.__size == 0:
            raise IndexError("This stack is empty")
        
        return self.__data[0]
    
    def size(self):
        return self.__size
    
    def clear(self):
        self.__data.clear()
        self.__size = 0
    
    def __str__(self):
        return str(self.__data)
    


