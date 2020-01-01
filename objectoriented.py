# x = "abc"
# print(type(x))
# print(dir(x))
# y = x.capitalize()
# print(y)

class testboi:
    x = 0
    name = ""
    def __init__(self, y):
        self.name = y
        print("You constucted testboi called:", self.name)

    def add(self):
        self.x = self.x + 1
        print(self.x)

class inheritboi(testboi):
    y = 0
    def add2(self):
        self.y = self.y + 1
        print(self.y)

tb = testboi("Miku")
tb2 = testboi("Miku2")
ib = inheritboi("inheritboi1")
tb.add()
tb.add()
tb.add()
ib.add()
ib.add2()
print(tb.x + tb.x)
print(tb.name)
print(tb2.name)