from pydo import SharedObject

class Counter(SharedObject):

    def __init__(self):
        super(Counter, self).__init__()
        self.count = 10

    def print_count(self):
        return self.count

c = Counter()
print c.count
c1 = Counter()
print c1.count