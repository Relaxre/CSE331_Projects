"""
# Project 4
# Name: JiaChen Lin
# PID: A54510773
"""

class Stack:
    """
    Stack class
    """
    def __init__(self, capacity=2):
        """
        DO NOT MODIFY
        Creates an empty Stack with a fixed capacity
        :param capacity: Initial size of the stack. Default size 2.
        """
        self.capacity = capacity
        self.data = [None] * self.capacity
        self.size = 0

    def __str__(self):
        """
        DO NOT MODIFY
        Prints the values in the stack from bottom to top. Then, prints capacity.
        :return: string
        """
        if self.size == 0:
            return "Empty Stack"

        output = []
        for i in range(self.size):
            output.append(str(self.data[i]))
        return "{} Capacity: {}".format(output, str(self.capacity))

    def __eq__(self, stack2):
        """
        DO NOT MODIFY
        Checks if two stacks are equivalent to each other. Checks equivalency of data and capacity
        :return: True if equal, False if not
        """
        if self.capacity != stack2.capacity:
            return False

        count = 0
        for item in self.data:
            if item != stack2.data[count]:
                return False
            count += 1

        return True

    def stack_size(self):
        """
        The size of the stack
        :return: The updated size of the stack
        """
        return self.size

    def is_empty(self):
        """
        Check whether the stack is empty or not
        :return: Return true if th stack is empty, return false otherwise
        """
        if self.size == 0:
            return True
        return False

    def top(self):
        """
        Return the top item in the stack but not remove the item
        :return: return None if the stack is empty. return the top element
        if there is one in the stack
        """
        if self.is_empty():
            return None
        return self.data[self.size-1]

    def push(self, val):
        """
        Push the val into the stack, updated the size of stack and grow by the increase of size
        :param val: The value that need to be pushed into
        :return: return nothing
        """
        if self.size == self.capacity:
            self.grow()
        self.data[self.size] = val
        self.size += 1

    def pop(self):
        """
        pop the top element in the stack, updated the size of stack and shrink by the decrease of size
        :return: return the value that has been popped
        """
        if self.size == 0:
            return None
        re_val = self.data[self.size-1]
        self.data[self.size - 1] = None
        self.size -= 1
        if self.size <= (self.capacity // 2):
            self.shrink()
        return re_val

    def grow(self):
        """
        Grow the capacity of the stack when the capacity and size are same
        :return: return nothing
        """
        self.capacity = self.capacity * 2
        for i in range(self.size, self.capacity):
            self.data.append(None)

    def shrink(self):
        """
        Shrink the capacity of the stack when the capacity is twice as the size
        :return: return nothing
        """
        if self.capacity > 2:
            self.capacity = self.capacity//2
            for i in range(0, self.size):
                self.data.pop()


def reverse(stack):
    """
    Reverse the order of elements in the stack
    :param stack: The stack needed to be reversed
    :return: return the reversed stack
    """
    n_stack = Stack(stack.capacity)
    while stack.size != 0:
        val = stack.pop()
        n_stack.push(val)
    return n_stack


def replace(stack, old, new):
    """
    Replace all existence of old value with the new value
    :param stack: The stack that needs to be replaced
    :param old: The value waited to be relpaced
    :param new: The value needs to be replaced to
    :return: return the after replaced stack
    """
    n_stack = Stack(stack.capacity)
    while stack.size != 0:
        val = stack.pop()
        if val == old:
            val = new
            n_stack.push(val)
        else:
            n_stack.push(val)
    return reverse(n_stack)