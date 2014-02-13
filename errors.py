class ValueWithError(object):
	"""
	Represents a numeric value with a corresponding Gaussian error.
	"""
	def __init__(self,value,error):
		"""
		Creates a new ValueWithError using the specified value and error.
		Raises a ValueError if error is negative.
		"""
		if error < 0:
			raise ValueError("error cannot be negative")
		self.value = value
		self.error = error
