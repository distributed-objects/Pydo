import Pyro4
from Pyro4 import Daemon
from threading import Thread
import thread
import pickle
import socket

Pyro4.config.SERVERTYPE = "multiplex"
Pyro4.expose(Daemon)
daemon = Pyro4.Daemon(host="localhost", port=4040)
uri = daemon.register(daemon)
print uri
with Pyro4.locateNS() as ns:
	ns.register("Namespace", uri)
	print "Registered to namespace"
daemon.requestLoop()

def register(obj):
	daemon = Pyro4.Daemon(host="localhost", port=4040)
	uri = daemon.register(obj) # Scheduler
	with Pyro4.locateNS() as ns:
		ns.register("Namespace", uri)
		print "Registered to namespace"
	serve_daemon(daemon)
	return uri

def serve_daemon(daemon):
	print "Serving daemon"
	t = Thread(target=lambda: daemon.requestLoop())
	t.start()