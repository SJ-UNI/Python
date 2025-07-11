class HashTableLinearProbing:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        while self.keys[index] is not None:
            index = (index + 1) % self.size
        self.keys[index] = key
        self.values[index] = value

    def search(self, key):
        index = self._hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size
        return None

    def delete(self, key):
        index = self._hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.keys[index] = None
                self.values[index] = None
                return
            index = (index + 1) % self.size

hash_table = HashTableLinearProbing(size=10)
hash_table.insert("key1", "value1")
hash_table.insert("key2", "value2")
hash_table.insert("key3", "value3")

print("Search key2:", hash_table.search("key2"))  

hash_table.delete("key2")
print("Search key2 after deletion:", hash_table.search("key2"))  

