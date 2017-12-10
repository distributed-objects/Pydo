import Pyro4

Pyro4.config.REQUIRE_EXPOSE = False

def register(obj, daemon):
	uri = daemon.register(obj) # Scheduler
	with Pyro4.locateNS() as ns:
		ns.register("Namespace", uri)
		print "Registered to namespace"
	return uri