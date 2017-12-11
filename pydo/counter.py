import Pyro4

@Pyro4.expose
class Counter:

	def __init__(self):
		self.x = 10

	def hello():
		print "world"