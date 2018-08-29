# MoreFourCal.py
from FourCal import FourCal

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = MoreFourCal(4, 2)
print(a.sum())
print(a.mul())
print(a.sub())
print(a.div())
print(a.pow())
b = MoreFourCal(4, 0)
print(b.div())