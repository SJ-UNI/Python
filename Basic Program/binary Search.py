class BinarySearch:
    def __init__(self, data):
        self.data = data

    def search_recursive(self, element, low, high):
        if low <= high:
            mid = (low + high) // 2
            if self.data[mid] == element:
                return mid  # Element found at this index
            elif self.data[mid] < element:
                return self.search_recursive(element, mid + 1, high)
            else:
                return self.search_recursive(element, low, mid - 1)
        else:
            return -1  # Element not found

    def search(self, element):
        return self.search_recursive(element, 0, len(self.data) - 1)

# Create an object of the BinarySearch class
data_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
element_to_find = int(input("Enter an element to search: "))
searcher = BinarySearch(data_list)

# Perform the binary search and print the result
result = searcher.search(element_to_find)

if result != -1:
    print(f"Element {element_to_find} found at index {result}.")
else:
    print(f"Element {element_to_find} not found in the list.")
