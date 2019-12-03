class HashNode:
    """
    DO NOT EDIT
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"HashNode({self.key}, {self.value})"


class HashTable:
    """
    Hash table class, utilizes double hashing for conflicts
    """

    def __init__(self, capacity=4):
        """
        DO NOT EDIT
        Initializes hash table
        :param tableSize: size of the hash table
        """
        self.capacity = capacity
        self.size = 0
        self.table = [None]*capacity

    def __eq__(self, other):
        """
        DO NOT EDIT
        Equality operator
        :param other: other hash table we are comparing with this one
        :return: bool if equal or not
        """
        if self.capacity != other.capacity or self.size != other.size:
            return False
        for i in range(self.capacity):
            if self.table[i] != other.table[i]:
                return False
        return True

    def __repr__(self):
        pass

    def hash_function(self, x):
        """
        ---DO NOT EDIT---

        Converts a string x into a bin number for our hash table
        :param x: key to be hashed
        :return: bin number to insert hash item at in our table, -1 if x is an empty string
        """
        if not x:
            return -1
        hashed_value = 0

        for char in x:
            hashed_value = 181 * hashed_value + ord(char)

        return hashed_value % self.capacity

    def insert(self, key, value):
        """
        Insert the Hashnode into the HashTable
        :param key: The key of the HashNode
        :param value: The value of the HashNode
        :return: Return nothing
        """
        index = self.quadratic_probe(key)
        n_node = HashNode(key, value)

        if key != '' and value != '':
            if index is not None:
                if self.table[index] is None:
                    self.table[index] = n_node
                    self.size += 1
                else:
                    self.table[index].value = value
            if self.size / self.capacity > 0.75:
                self.grow()

    def quadratic_probe(self, key):
        """
        The function running the quadratic procedure
        :param key: The key of Hashnode needed to be search
        :return: the right index of the key
        """
        increment = 0
        bucket = self.hash_function(key)
        if not key:
            return -1
        elif self.find(key):
            while True:
                bucket = (bucket + increment * increment) % self.capacity
                if self.table[bucket] is not None and self.table[bucket].key == key:
                    return bucket
                else:
                    increment += 1
        else:
            while True:
                bucket = (bucket + increment * increment) % self.capacity
                if self.table[bucket] is None:
                    return bucket
                else:
                    increment += 1

    def find(self, key):
        """
        Using the key to search in the Hash Table
        :param key: The key needed to be found in the Hash Table
        :return: The HashNode of the key
        """
        for i in self.table:
            if i is None:
                continue
            elif i.key == key:
                return i
        return False

    def lookup(self, key):
        """
        Take the key to search in the Hash table and return the value of the key
        :param key: the key needed to be searched
        :return: The value of HashNode
        """
        if self.find(key):
            bucket = self.quadratic_probe(key)
            return self.table[bucket].value
        else:
            return False

    def delete(self, key):
        """
        Delete the HashNode in the Hashtable and assigned it to None
        :param key: The key of the HashNode needed to be deleted
        :return: Return nothing
        """
        if self.find(key):
            bucket = self.quadratic_probe(key)
            self.table[bucket] = None
            self.size -= 1

    def grow(self):
        """
        Change the capacity to twice as the original one and call rehash
        :return: Return nothing
        """
        self.capacity *= 2
        self.rehash()

    def rehash(self):
        """
        Rehashes all items inside of the table
        :return: return nothing
        """
        o_table = self.table
        self.table = [None] * self.capacity
        self.size = 0
        for node in o_table:
            if node is None:
                continue
            self.insert(node.key, node.value)


def string_difference(string1, string2):
    """
    Compare the differences between two strings
    :param string1: The first string
    :param string2: The second string
    :return: Return the set that contains the differences between two string
    """
    hash_set1 = set()
    hash_table = HashTable()
    hash_table1 = HashTable()
    if string1 == string2:
        return hash_set1
    for i in string1:
        if hash_table.find(i):
            bucket = hash_table.quadratic_probe(i)
            hash_table.table[bucket].value += 1
        else:
            hash_table.insert(i, 1)

    for i in string2:
        if hash_table1.find(i):
            bucket = hash_table1.quadratic_probe(i)
            hash_table1.table[bucket].value += 1
        else:
            hash_table1.insert(i, 1)

    for i in hash_table.table:
        if i is None:
            continue
        if not hash_table1.find(i.key):
            hash_set1.add(i.key*i.value)
            continue
        if i.key == hash_table1.find(i.key).key:
            i.value -= hash_table1.find(i.key).value
            if i.value == 0:
                continue
            hash_set1.add(i.value * i.key)

    for i in hash_table1.table:
        if i is None:
            continue
        if not hash_table.find(i.key):
            hash_set1.add(i.key*i.value)
            continue

    return hash_set1