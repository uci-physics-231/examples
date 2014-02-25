class AbsInterpolator(object):
	def interpolate(x):
		raise NotImplementedError('interpolate method has not been implemented')

class LinearInterpolator(AbsInterpolator):
	def __init__(self,xvec,yvec):
		pass
	def interpolate(self,x):
		pass

class SplineInterpolator(AbsInterpolator):
	def __init__(self,xvec,yvec):
		pass
	def interpolate(self,x):
		pass
