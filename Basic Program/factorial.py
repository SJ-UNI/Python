class Fact:
    def factorial(self,n,num):
        if (n==1 or n==0):
            return 1
        else:
            return (n * factorial(n - 1))
        print("Factorial : ",factorial(num))    
FAT = Fact()
num = int(input("enter the number:")) 
FAT.factorial(num)
