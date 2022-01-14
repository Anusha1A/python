class example():
    def __init__(self):
        self.str1 = ""
    def getstring(self):
        self.str1 = input("enter a string")
    def printstring(self):
        print(self.str1.upper())
str1 = example()
str1.getstring()
str1.printstring()