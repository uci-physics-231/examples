# A sample implementation of the Factory Method design pattern in python
# Test using:
"""
import factory as particle
e = particle.create("electron")
e.mass
p = particle.create("proton")
p.mass
"""

class Particle(object):
	def __init__(self,mass):
		self.mass = mass

def create(name):
	# define the subclasses of Particle that we can create as nested
	# classes so that they cannot be created directly.
	class Electron(Particle):
		def __init__(self):
			Particle.__init__(self,0.511)
	class Proton(Particle):
		def __init__(self):
			Particle.__init__(self,938.)
	# create the requested class by name
	if name == "electron":
		return Electron()
	if name == "proton":
		return Proton()
	raise RuntimeError("Unknown particle name: %s",name)
	# We could have used eval above, but this has security issues
	#if name in ("Electron","Proton"):
	#	return eval(name+"()")
