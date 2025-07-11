class LinearSearch:
    def __init__(self, data):
        self.data = data

    def search_recursive(self, element, index=0):
        if index >= len(self.data):
            return -1  # Element not found
        if self.data[index] == element:
            return index  # Element found at this index
        return self.search_recursive(element, index + 1)

    def search(self, element):
        return self.search_recursive(element)

# Create an object of the LinearSearch class
data_list = [10, 20, 30, 40, 50]
element_to_find = int(input("Enter an element to search: "))
searcher = LinearSearch(data_list)

# Perform the linear search and print the result
result = searcher.search(element_to_find)

if result != -1:
    print(f"Element {element_to_find} found at index {result}.")
else:
    print(f"Element {element_to_find} not found in the list.")
