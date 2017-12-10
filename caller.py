import Pyro4


x = "PYRO:obj_3ca09e74aa1542d6ac6f0ce090fcdd9d@localhost:49996"

obj = Pyro4.Proxy(x)
print obj
print obj.perform()