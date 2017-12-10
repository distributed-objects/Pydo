import Pyro4
import random
import pydo

class SharedObject(object):

    def __init__(self):
        self.name = self.__class__.__name__ + "%s" %random.randint(1, 100)
        self.name = pydo.register(self, Pyro4.Daemon())
        print self.name

    def get_name(self):
        return self.name

    def __getattribute__(self, name):
        """ Intercept calls to any of the methods in the child object """
        attr = object.__getattribute__(self, name)
        if hasattr(attr, '__call__'):
            def newfunc(*args, **kwargs):
                # Allow async calls to methods (promises)
                if 'async' in kwargs: del kwargs['async']
                obj = Pyro4.Proxy(self.name)
                print obj
                return obj.perform()
                # result = func(*args, **kwargs)
                # return result
            return newfunc
        else:
            return attr

@Pyro4.expose
class Counter(SharedObject):

    def __init__(self):
        super(Counter, self).__init__()
        self.count = 10

    def perform(self):
        return "Hey yo!"

c1 = Counter()
print "Perform"
print c1.perform()
print dir(c1)
print c1.count