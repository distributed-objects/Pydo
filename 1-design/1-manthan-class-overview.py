# Pydo side

# central server
class Lookup(object):
    pass

    # Mapping -> objectname -> pyro_uri

# Tanenbaum paper
# Migration/ Retrieving results
class SharedObject(object):

    # Data structure
    def _init_(self):
        pass

    def _setattr_(self):
        if self.local:
            pass
        else: # The object is remote
            pass


# User-side
class Counter(SharedObject):