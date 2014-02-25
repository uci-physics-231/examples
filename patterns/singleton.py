# A sample implementation of the Singleton design pattern in python
# Test with:
"""
import singleton as GPU
GPU.getInstance()
GPU.getInstance()
"""

instance = None

def getInstance():
	global instance
	if not instance:
		# Initialize and allocate GPU here...
		print 'Initializing...'
		instance = 'The GPU'
	return instance
