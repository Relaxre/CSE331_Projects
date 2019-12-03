class Node:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'parent', 'left', 'right'

    def __init__(self, value, parent=None, left=None, right=None):
        """
        Initialization of a node
        :param value: value stored at the node
        :param parent: the parent node
        :param left: the left child node
        :param right: the right child node
        """
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def __eq__(self, other):
        """
        Determine if the two nodes are equal
        :param other: the node being compared to
        :return: true if the nodes are equal, false otherwise
        """
        if type(self) is not type(other):
            return False
        return self.value == other.value

    def __str__(self):
        """String representation of a node by its value"""
        return str(self.value)

    def __repr__(self):
        """String representation of a node by its value"""
        return str(self.value)


class BinarySearchTree:

    def __init__(self):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Initializes an empty Binary Search Tree
        """
        self.root = None
        self.size = 0

    def __eq__(self, other):
        """
        Describe equality comparison for BSTs ('==')
        :param other: BST being compared to
        :return: True if equal, False if not equal
        """
        if self.size != other.size:
            return False
        if self.root != other.root:
            return False
        if self.root is None or other.root is None:
            return True  # Both must be None

        if self.root.left is not None and other.root.left is not None:
            r1 = self._compare(self.root.left, other.root.left)
        else:
            r1 = (self.root.left == other.root.left)
        if self.root.right is not None and other.root.right is not None:
            r2 = self._compare(self.root.right, other.root.right)
        else:
            r2 = (self.root.right == other.root.right)

        result = r1 and r2
        return result

    def _compare(self, t1, t2):
        """
        Recursively compares two trees, used in __eq__.
        :param t1: root node of first tree
        :param t2: root node of second tree
        :return: True if equal, False if nott
        """
        if t1 is None or t2 is None:
            return t1 == t2
        if t1 != t2:
            return False
        result = self._compare(t1.left, t2.left) and self._compare(t1.right, t2.right)
        return result

    ### Implement/Modify the functions below ###

    def insert(self, value):
        """
        Insert the node at the appropriate position in the tree
        :param value: The value ready to be inserted
        :return: retrun nothing
        """
        n_node = Node(value)

        if self.root is None:

             self.root = n_node
             self.size += 1

        else:
            cur = self.root
            while cur is not None:
                if n_node.value == cur.value:
                    return
                elif n_node.value < cur.value:
                    if cur.left is None:
                        cur.left = n_node
                        n_node.parent = cur
                        cur = None
                        self.size += 1
                    else:
                        cur = cur.left
                else:
                    if cur.right is None:
                        cur.right = n_node
                        n_node.parent = cur
                        cur = None
                        self.size += 1
                    else:
                        cur = cur.right
            n_node.left = None
            n_node.right = None

    def remove(self, value):
        """
        Remove the given value in the tree
        :param value: The value ready to be removed and update the value and the relationship between nodes
        :return: return nothing
        """
        n_node = Node(value)
        cur = self.root
        while cur is not None:  # Search for node
            if value == cur.value:  # Node found
                if (cur.left is None) & (cur.right is None):  # Remove leaf
                    if not n_node.parent:  # Node is root
                        self.root = None
                        self.size -= 1

                    elif n_node.parent.left == cur:
                        n_node.parent.left = None
                        self.size -= 1

                    else:
                        n_node.parent.right = None
                        self.size -= 1

                elif (cur.right is None) & (cur.left is not None):   # Remove node with only left child
                    if not n_node.parent:  # Node is root
                        self.root = cur.left
                        self.size -= 1

                    elif n_node.parent.left == cur:
                        n_node.parent.left = cur.left
                        self.size -= 1

                    else:
                        n_node.parent.right = cur.left
                        self.size -= 1

                elif (cur.left is None) & (cur.right is not None):   # Remove node with only right child
                    if not n_node.parent:  # Node is root
                        self.root = cur.right
                        self.size -= 1

                    elif n_node.parent.left == cur:
                        n_node.parent.left = cur.right
                        self.size -= 1

                    else:
                        n_node.parent.right = cur.right
                        self.size -= 1

                else:                 # Remove node with two children
                    if not n_node.parent:  # if it is root
                        copy_node = self.min(cur.right)
                        self.remove(copy_node.value)
                        copy_node.parent = None
                        cur.value = copy_node.value
                        copy_node.left = cur.left
                        copy_node.right = cur.right
                        cur.left.parent = copy_node
                        if cur.right is not None:
                            cur.right.parent = copy_node

                    else:  # if it is not
                        copy_node = self.min(cur.right)
                        self.remove(copy_node.value)
                        copy_node.parent = cur.parent
                        cur.value = copy_node.value
                        copy_node.left = cur.left
                        copy_node.right = cur.right
                        cur.left.parent = copy_node
                        if cur.right is not None:
                            cur.right.parent = copy_node
                return

            elif cur.value < n_node.value:
                n_node.parent = cur
                cur = cur.right
            else:
                n_node.parent = cur
                cur = cur.left
        return

    def search(self, value, node):
        """
        Search the given value from given node
        :param value: The value needs to be search
        :param node: The position where the search begin
        :return: Return nothing
        """
        if node is None:
            return

        if value == node.value:
            return node

        elif value < node.value:
            if node.left is None:
                return node
            return self.search(value, node.left)

        elif value > node.value:
            if node.right is None:
                return node
            return self.search(value, node.right)

    def inorder(self, node):
        """
        Arrange the the nodes in binary tree in inorder order
        :param node: The given node took as root node
        :return: Return nothing
        """
        if node is None:
            return
        yield from self.inorder(node.left)
        yield node.value
        yield from self.inorder(node.right)

    def preorder(self, node):
        """
        Arrange the the nodes in binary tree in preorder order
        :param node: The given node took as root node
        :return: Return nothing
        """
        if node is None:
            return
        yield node.value
        yield from self.preorder(node.left)
        yield from self.preorder(node.right)


    def postorder(self, node):
        """
        Arrange the the nodes in binary tree in postorder order
        :param node: The given node took as root node
        :return: Return nothing
        """
        if node is None:
            return
        yield from self.postorder(node.left)
        yield from self.postorder(node.right)
        yield node.value

    def depth(self, value):
        """
        Get the value of depth of the binary tree
        :param value: The value of depth that needs to be measured
        :return: The height of the tree rooted at the given node
        """
        cur = self.root
        if cur is None:
            dep = -1
            return dep
        dep = 0
        while cur is not None:
            if value == cur.value:
                return dep
            elif value < cur.value:
                if cur.left is None:
                    dep = -1
                    return dep
                cur = cur.left
                dep += 1
            elif value > cur.value:
                if cur.right is None:
                    dep = -1
                    return dep
                cur = cur.right
                dep += 1

    def height(self, node):
        """
        Get the height of the tree rooted at the given node
        :param node: The root node
        :return: The height of the tree rooted at the given node
        """
        if node is None:
            return -1
        left_h = self.height(node.left)
        right_h = self.height(node.right)

        if left_h > right_h:
            return 1 + left_h
        else:
            return 1 + right_h

    def min(self, node):
        """
        The minimal node in the tree rooted at hte given node
        :param node: The root node
        :return: The minimal node in the tree rooted at hte given node
        """
        if self.size == 0:
            return
        if node.left is None:
            return node
        return self.min(node.left)

    def max(self, node):
        """
        The maximum node in the tree rooted at hte given node
        :param node: The root node
        :return: The maximum node in the tree rooted at hte given node
        """
        if self.size == 0:
            return
        if node.right is None:
            return node
        return self.max(node.right)

    def get_size(self):
        """
        Get the size of node in the tree
        :return: size of the nodes in the tree
        """
        return self.size

    def is_perfect(self, node):
        """
        Boolean to check whether the tree is perfect or not
        :param node: The root node
        :return: True and False
        """
        if node is None:
            return True

        if node.left is None and node.right is None:
            return True

        if node.left is not None and node.right is not None:
            return self.is_perfect(node.left) and self.is_perfect(node.right)
        return False

    def is_degenerate(self):
        """
        Boolean to check whether the tree is degenerate or not
        :return: True and False
        """
        if self.root is None:
            return False
        if self.size == self.height(self.root) + 1:
            return True
        return False