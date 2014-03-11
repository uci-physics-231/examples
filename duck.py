"""
Duck typing example in python
"""

import math

def getMass(p):
	"""
	This function requires that p implement getEnergy and getMomentum
	methods, but does not care about their formal types
	"""
	print 'Calling getMass for type',type(p)
	return math.sqrt(p.getEnergy()**2 - p.getMomentum()**2)

class Electron(object):
	def __init__(self,p):
		self.p = p
		self.m = 0.511
		self.E = math.sqrt(p**2+self.m**2)
	def getEnergy(self):
		return self.E
	def getMomentum(self):
		return self.p

class SpaceShuttle(object):
	def __init__(self,fuel):
		self.fuel = fuel
		self.p = 10.
		self.m = 10000.
		self.E = math.sqrt(self.p**2+self.m**2)
	def getEnergy(self):
		return self.E
	def getMomentum(self):
		return self.p
	def getFuel(self):
		return self.fuel

electron = Electron(1)
print getMass(electron)

shuttle = SpaceShuttle(500)
print getMass(shuttle)
