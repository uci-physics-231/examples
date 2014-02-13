import math

class ValueWithError(object):
	"""
	Represents a numeric value with a corresponding Gaussian error.
	"""
	def __init__(self,value,error):
		"""
		Creates a new ValueWithError using the specified value and error.
		Raises a ValueError if error is less than or equal to zero.
		"""
		if error <= 0:
			raise ValueError("error must be positive")
		self.value = value
		self.error = error
	def __repr__(self):
		"""
		Returns our definitive and unambiguious string representation
		"""
		return "%f +/- %f" % (self.value,self.error)
	def __str__(self):
		"""
		Returns our string representation using the PDG rounding rules described
		in Section 5.3 of http://pdg.lbl.gov/2011/reviews/rpp2011-rev-rpp-intro.pdf
		"""
		# we assume that error > 0 in the following
		assert self.error > 0, "Error isn't positive !?"
		# find the power of ten corresponding to the most significant digit of the error
		msd = int(math.floor(math.log10(self.error)))
		# convert the three most significant digits of the error to an integer 100-999
		sig = math.floor(self.error/10**(msd-2))
		print msd,sig
		assert sig >= 100 and sig <= 999, "Range error for 3 most sig digits !?"
		# select the number of significant digits to use for rounding
		if sig < 355:
			nround = 2
		elif sig < 950:
			nround = 1
		else:
			nround = 2
			msd += 1
		# round the error
		roundedError = math.floor(self.error/10**(msd-nround))
		# round the value
		roundedValue = math.floor(abs(self.value)/10**(msd-nround))
		if self.value < 0:
			roundedValue = -roundedValue
		return "%d +/- %d" % (roundedValue,roundedError)
