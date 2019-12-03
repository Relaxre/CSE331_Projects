########################################
# PROJECT: Binary Min Heap and Sort
# Author: Jiachen Lin
########################################

class BinaryMinHeap:
    # DO NOT MODIFY THIS CLASS #
    def __init__(self):
        """
        Creates an empty hash table with a fixed capacity
        """
        self.table = []


    def __eq__(self, other):
        """
        Equality comparison for heaps
        :param other: Heap being compared to
        :return: True if equal, False if not equal
        """
        if len(self.table) != len(other.table):
            return False
        for i in range(len(self.table)):
            if self.table[i] != other.table[i]:
                return False

        return True

    ###### COMPLETE THE FUNCTIONS BELOW ######

    def __str__(self):
        pass

    def get_size(self):
        """
        The function to return the numbers of nodes currently in the Heap
        :return: The actual numbers of nodes in the heap
        """
        return len(self.table)

    def parent(self, position):
        """
        Finds the parent's index of node position
        :param position: The index of node
        :return: The index of node's parent's index
        """
        return (position-1) // 2

    def left_child(self, position):
        """
        Find the left child of the node at index position
        :param position: The index of node
        :return: Index of left child
        """
        return 2 * position + 1

    def right_child(self, position):
        """
        Find the right child of the node at index position
        :param position: The index of node
        :return: Index of right child
        """
        return 2 * position + 2

    def has_left(self, position):
        """
        Determine the node has left child or not
        :param position: The index of node
        :return: True/ False
        """
        return self.left_child(position) < len(self.table)

    def has_right(self, position):
        """
        Determine the node has right child or not
        :param position: The index of node
        :return: True/ False
        """
        return self.right_child(position)< len(self.table)

    def find(self, value):
        """
        Find the index of given node
        :param value: Given node
        :return: The index of given node
        """
        for i in range(self.get_size()):
            if self.table[i] == value:
                return i
        return None

    def heap_push(self, value):
        """
        Add a node with the given value
        :param value:  The given node
        :return: return nothing
        """
        if self.find(value) == 0 or self.find(value):
            return
        else:
            self.table.append(value)
            self.percolate_up(self.table.index(value))

    def heap_pop(self, value):
        """
        Pop the given node
        :param value:  The given node
        :return: return nothing
        """
        index = self.find(value)
        if index is not None:
            self.swap(0, index)
            self.pop_min()
            self.percolate_down(index)

    def pop_min(self):
        """
        Pop the minimal node in the heap
        :return: return the item popped
        """
        if self.get_size() > 0:
            self.swap(0, len(self.table) - 1)
            item = self.table.pop()
            self.percolate_down(0)
            return item

    def swap(self, p1, p2):
        """
        Swap the value and the index of two given nodes
        :param p1: given nodes 1
        :param p2: given nodes 2
        :return: Return Nothing
        """
        self.table[p1], self.table[p2] = self.table[p2], self.table[p1]

    def percolate_up(self, position):
        """
        Move the node at index position up the tree until found the appropriate one
        :param position: The index of node
        :return: Return nothing
        """
        parent = self.parent(position)
        if position > 0 and self.table[position] < self.table[parent]:
            self.swap(position, parent)
            self.percolate_up(parent)  # recur at position of parent

    def percolate_down(self, position):
        """
        Move the node at index position down the tree until found the appropriate one
        :param position: The index of node
        :return: Return nothing
        """
        if self.has_left(position):
            left = self.left_child(position)
            small_child = left  # although right may be smaller
            if self.has_right(position):
                right = self.right_child(position)
                if self.table[right] < self.table[left]:
                    small_child = right
            if self.table[small_child] < self.table[position]:
                self.swap(position, small_child)
                self.percolate_down(small_child)  # recur at position of small child


def heap_sort(unsorted):
    """
    Perform the heap sort
    :param unsorted: The unsorted list
    :return: The heap sorted list
    """
    re_list = []
    heap_arr = BinaryMinHeap()
    for i in unsorted:
        heap_arr.heap_push(i)

    for i in range(heap_arr.get_size()):
        re_list.append(heap_arr.pop_min())

    return re_list


# def main():
#     heap = BinaryMinHeap()
#     heap.heap_push(1)
#     heap.heap_push(2)
#     heap.heap_push(3)
#     heap.heap_push(4)
#     heap.heap_push(5)
#     heap.heap_push(6)
#     heap.heap_push(7)
#
#     heap.heap_pop(4)
#     heap.heap_pop(6)
#     heap.heap_pop(2)
#     heap.heap_pop(7)
#
# if __name__ == '__main__':
#     main()
