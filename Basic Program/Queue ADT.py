class MyList:
    def _init_(self):
        self.data = []

    def add(self, value):
        self.data.append(value)

    def remove(self, value):
        if value in self.data:
            self.data.remove(value)
        else:
            print(f"{value} not found in the list.")

    def display(self):
        print(self.data)

    def size(self):
        return len(self.data)


my_list = MyList()


my_list.add(1)
my_list.add(2)
my_list.add(3)

my_list.display()  

my_list.remove(2)
my_list.display()  

print("Size of the list:", my_list.size())  
