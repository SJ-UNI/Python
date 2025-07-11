class TowerOfHanoi:
    def _init_(self, n):
        self.n = n
        self.towers = [[i for i in range(n, 0, -1)], [], []]

    def move(self, source, destination):
        if not self.towers[source]:
            return
        if not self.towers[destination] or self.towers[destination][-1] > self.towers[source][-1]:
            self.towers[destination].append(self.towers[source].pop())
            print(f"Moved {self.towers[destination][-1]} from Tower {source + 1} to Tower {destination + 1}")
    
    def solve(self, n=None, source=0, destination=2, auxiliary=1):
        if n is None:
            n = self.n
        if n == 0:
            return
        self.solve(n - 1, source, auxiliary, destination)
        self.move(source, destination)
        self.solve(n - 1, auxiliary, destination, source)

n = int(input("Enter the number of disks: "))
t = TowerOfHanoi(n)
t.solve()
