#!/usr/bin/env python

import errors
import unittest

class ValueWithErrorsTests(unittest.TestCase):

	def setUp(self):
		pass

	def ctor_two_args(self):
		"ctor requires exactly two args"
		self.assertRaises(TypeError,errors.ValueWithError)
		self.assertRaises(TypeError,errors.ValueWithError,1)
		self.assertRaises(TypeError,errors.ValueWithError,1,2,3)

	def ctor_neg_error(self):
		"error value must be positive"
		self.assertRaises(ValueError,errors.ValueWithError,1,0)
		self.assertRaises(ValueError,errors.ValueWithError,1,-1)

if __name__ == '__main__':
	unittest.main()
