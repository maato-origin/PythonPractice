
#オブジェクト同士の演算
print('オブジェクト同士の演算')

print('\n比較演算')
class Sample:
    def __init__(self, val, text):
        self.val = val
        self.text = text

    def __lt__(self, other):
        return self.val < other.val

    def __le__(self, other):
        return self.val <= other.val

    def __eq__(self, other):
        return self.val == other.val

    def __ne__(self, other):
        return self.val != other.val

    def __gt__(self, other):
        return self.val > other.val

    def __ge__(self, other):
        return self.val >= other.val

obj1 = Sample(100, 'aaa')
obj2 = Sample(200, 'bbb')

print(obj1 < obj2)
print(obj1 <= obj2)
print(obj1 == obj2)
print(obj1 != obj2)
print(obj1 > obj2)
print(obj1 >= obj2)

print('\n数値演算')
class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """座標の足し算に使用"""
        x = self.x + other.x
        y = self.y + other.y

        return Coordinate(x, y)

    def __sub__(self, other):
        """座標の引き算に使用"""
        x = self.x - other.x
        y = self.y - other.y

        return Coordinate(x, y)

    def __str__(self):
        return "coordinate:({0},{1})".format(self.x, self.y)

c1 = Coordinate(1000, 2000)
c2 = Coordinate(300, 400)
print(c1 + c2)
print(c1 - c2)