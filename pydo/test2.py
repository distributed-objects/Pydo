import Pyro4
# from accessor import Counter
from counter import Counter

daemon = Pyro4.Proxy("PYRO:obj_e7986bf6109c442cad4925086760b334@localhost:4040")
print dir(daemon)
# print daemon.locationStr