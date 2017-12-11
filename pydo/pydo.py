import Pyro4
from Pyro4 import Daemon, Proxy
from threading import Thread
import thread
import pickle
import socket

Pyro4.config.REQUIRE_EXPOSE = False

def register(obj):
    ''' Register an object with daemon '''
    daemon = Pyro4.Daemon(host="localhost")
    uri = daemon.register(obj) # Scheduler
    serve_daemon(daemon)
    return uri

def serve_daemon(daemon):
    ''' Serve the daemon in a separate thread '''
    t = Thread(target=lambda: daemon.requestLoop())
    t.setDaemon(True)
    t.start()

def proxy(uri):
    ''' Return a proxy object for the given uri '''
    return Pyro4.Proxy(uri)


class SharedObject(object):
    ''' Shared object that is distribtued across nodes '''

    def __init__(self):
        ''' Register the child object to the daeomn and
            replace object with the proxy object '''
        self.name = register(self)
        print proxy(self.name)

    def __getattribute__(self, name):
        """ Intercept calls to any of the methods in the child object """
        attr = object.__getattribute__(self, name)
        if hasattr(attr, '__call__'):
            def newfunc(*args, **kwargs):
                # Allow async calls to methods (promises)
                if 'async' in kwargs: del kwargs['async']
                # result = func(*args, **kwargs)
                # return result
            return newfunc
        else:
            return attr