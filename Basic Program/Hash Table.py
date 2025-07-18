class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i, (existing_key, _) in enumerate(self.table[index]):
                if existing_key == key:
                    
                    self.table[index][i] = (key, value)
                    break
            else:
               
                self.table[index].append((key, value))

    def search(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for existing_key, value in self.table[index]:
                if existing_key == key:
                    return value
        return None

    def delete(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for i, (existing_key, _) in enumerate(self.table[index]):
                if existing_key == key:
                    del self.table[index][i]
                    break


hash_table = HashTable(size=10)
hash_table.insert("key1", "value1")
hash_table.insert("key2", "value2")

print(hash_table.search("key1"))  

hash_table.delete("key1")
print(hash_table.search("key1"))  
