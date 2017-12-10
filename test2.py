import Pyro4
from accessor import Counter
from counter import Counter

c = Counter()
daemon = Pyro4.Proxy("PYRO:obj_4f9617d564a4482a97ced8ee97da3103@localhost:4040")
print daemon.register(c)