class Stack(object):

    def __init__(self):
        self.items = []

    def push(self, item=''):
        """
        Adds an item to the stack.
        
        :param item: Item to be added to the stack.
        :return: None
        """
        self.items.append(item)

    def pop(self):
        """
        Removes the last item from the stack.
        
        :return: None
        """
        if not self.isempty():
            self.items.pop()

    def peek(self):
        """
        Returns the last item from the stack without removing it.
        
        :return: The last item or None if the stack is empty.
        """
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """
        Returns the number of items in the stack.
        
        :return: The size of the stack.
        """
        return len(self.items)

    def isempty(self):
        """
        Checks if the stack is empty.
        
        :return: True if the stack is empty, False otherwise.
        """
        return not bool(self.items)


if __name__ == "__main__":
    stack = Stack()

