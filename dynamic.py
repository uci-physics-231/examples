class Particle(object):
	def __init__(self,mass):
		self.mass = mass

electron = Particle(0.511)
proton = Particle(938.0)

print 'electron mass is',electron.mass
print 'proton mass is',proton.mass

# add an attribute to one object without affecting other instances of the same class
electron.spin = 0.5

print 'electron spin is',electron.spin
# this next line will fail
print 'proton spin is',proton.spin
