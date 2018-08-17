# FourCal.py

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    # def setdata(self, first, second):
    #     self.first = first
    #     self.second = second

    def sum(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result

'''
a = FourCal(4, 2)
# a.setdata(4, 2)
print(a.sum())
print(a.sub())
print(a.mul())
print(a.div())

b = FourCal(3, 7)
# b.setdata(3, 7)
print(b.sum())
print(b.sub())
print(b.mul())
print(b.div())
'''
