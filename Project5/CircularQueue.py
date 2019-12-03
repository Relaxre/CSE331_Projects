class CircularQueue():
    # DO NOT MODIFY THESE METHODS
    def __init__(self, capacity=4):
        """
        Initialize the queue with an initial capacity
        :param capacity: the initial capacity of the queue
        """
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity
        self.head = 0
        self.tail = 0


    def __eq__(self, other):
        """
        Defines equality for two queues
        :return: true if two queues are equal, false otherwise
        """
        if self.capacity != other.capacity:
            return False
        for i in range(self.capacity):
            if self.data[i] != other.data[i]:
                return False
        return self.head == other.head and self.tail == other.tail and self.size == other.size

    # -----------MODIFY BELOW--------------

    def __str__(self):
        pass

    def is_empty(self):
        """
        To check whether the queue is empty or not
        :return: True if it is empty, false otherwise
        O(1) time complexity, O(1) space complexity
        """
        return self.size == 0

    def __len__(self):
        """
        The amount of items in queue
        :return: the size of the queue
        O(1) time complexity, O(1) space complexity
        """
        return self.size

    def first_value(self):
        """
        The front of the queue
        :return: THe front value of the queue
        O(1) time complexity, O(1) space complexity
        """
        return self.data[self.head]

    def enqueue(self, val):
        """
        Add a number to the back of the queue
        :param val: the number to be queued
        :return: return None
        O(1) time complexity, O(1) space complexity
        """
        if self.size == 0:
            right_index = (self.head + self.size) % len(self.data)
            self.data[right_index] = val
            self.size += 1
            self.tail += 1
        else:
            right_index = (self.head + self.size) % len(self.data)
            self.data[right_index] = val
            self.tail += 1
            self.tail = self.tail % self.capacity
            self.size += 1
            if self.size == self.capacity:
                self.grow()

    def dequeue(self):
        """
        Remove an item from the start of the a queue if not empty
        :return: the value got popped
        O(1) time complexity, O(1) space complexity
        """
        if not self.is_empty():
            ori_ele = self.data[self.head]
            self.data[self.head] = None
            self.head += 1
            self.head = self.head % self.capacity
            self.size -= 1
            if self.size <= self.capacity * 1 // 4:
                self.shrink()
            return ori_ele

    def grow(self):
        """
        Double the capacity once the size of the queue equals to the capacity of the queue
        :return: return none
        O(n) time complexity, O(n) space complexity
        """
        self.capacity *= 2
        old_queue = self.data
        self.data = [None] * self.capacity
        old_ele = self.head
        for i in range(self.size):
            self.data[i] = old_queue[old_ele]
            old_ele = (1 + old_ele) % len(old_queue)
            self.tail += 1
        self.tail = self.size
        self.head = 0

    def shrink(self):
        """
        Halves the capacity of the queue if the size equal or less than
        1/4 * capacity of queue. Also the capacity of queue should not less than 4
        :return: return none
        O(n) time complexity, O(n) space complexity
        """
        if self.capacity > 4:
            self.capacity = self.capacity * 1//2
            old_queue = self.data
            self.data = [None] * self.capacity
            old_ele = self.head
            for i in range(self.size):
                self.data[i] = old_queue[old_ele]
                old_ele += 1
            self.tail = self.size
            self.head = 0

