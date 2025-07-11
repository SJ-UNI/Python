class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)

    def _insert(self, root, key, value):
        if root is None:
            return TreeNode(key, value)
        if key < root.key:
            root.left = self._insert(root.left, key, value)
        elif key > root.key:
            root.right = self._insert(root.right, key, value)
        else:
            root.value = value
        return root

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.key == key:
            return root.value if root else None
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)

bst = BinarySearchTree()
bst.insert(5, "Data")
bst.insert(3, "Structures")
bst.insert(7, "Argument")

print("Search 5:", bst.search(5))
print("Search 3:", bst.search(3))
print("Search 7:", bst.search(7))  
print("Search 4:", bst.search(4))  
