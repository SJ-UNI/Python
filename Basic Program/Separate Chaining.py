class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTableSeparateChaining:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current.next is not None:
                current = current.next
            current.next = Node(key, value)

    def search(self, key):
        index = self._hash(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        index = self._hash(key)
        current = self.table[index]
        if current is not None and current.key == key:
            self.table[index] = current.next
            return
        prev = None
        while current is not None and current.key != key:
            prev = current
            current = current.next
        if current is not None:
            prev.next = current.next

hash_table = HashTableSeparateChaining(size=10)
hash_table.insert("key1", "value1")
hash_table.insert("key2", "value2")
hash_table.insert("key3", "value3")
print("Search key2:", hash_table.search("key2"))  
hash_table.delete("key2")
print("Search key2 after deletion:", hash_table.search("key2"))
print("Search key3:", hash_table.search("key3")) 
