import Pyro4
import random
from threading import Thread
import pickle
import socket
import pydo

class SharedObject(object):
    def __init__(self):
        print self.__class__
        Pyro4.expose(self.__class__)
        self.name = pydo.register(self)
        print self.name

    def get_name(self):
        return self.name

    def get_server(self):
        with open("pydo.object", "r") as f:
            return pickle.load(f)

    def __getattribute__(self, name):
        """ Intercept calls to any of the methods in the child object """
        attr = object.__getattribute__(self, name)
        if hasattr(attr, '__call__'):
            def newfunc(*args, **kwargs):
                # Allow async calls to methods (promises)
                if 'async' in kwargs: del kwargs['async']
                obj = Pyro4.Proxy(self.name)
                print "---Proxy {}".format(obj)
                return obj.perform()
                # result = func(*args, **kwargs)
                # return result
            return newfunc
        else:
            return attr

class Counter(SharedObject):

    def __init__(self):
        super(Counter, self).__init__()
        self.count = 10

    def perform(self):
        return "Hey yo!"


if __name__ == "__main__":
    c1 = Counter()
    print c1
    print c1.perform()
    c2 = Counter()
    c3 = Counter()