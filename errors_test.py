#!/usr/bin/env python

"""
Tests the ValueWithError class using the standard python unittest module.
See http://docs.python.org/2/library/unittest.html for details.
"""

import errors
import unittest

class ValueWithErrorsTests(unittest.TestCase):

	def setUp(self):
		pass

	def test_ctor_two_args(self):
		"ctor requires exactly two args"
		self.assertRaises(TypeError,errors.ValueWithError)
		self.assertRaises(TypeError,errors.ValueWithError,1)
		self.assertRaises(TypeError,errors.ValueWithError,1,2,3)

	def test_ctor_neg_error(self):
		"error value must be positive"
		self.assertRaises(ValueError,errors.ValueWithError,1,0)
		self.assertRaises(ValueError,errors.ValueWithError,1,-1)

	def test_str_rounding_range1(self):
		"rounding test cases with sig = 100 - 354"
		self.assertEqual(str(errors.ValueWithError(1,1)),"1.0 +/- 1.0")
		self.assertEqual(str(errors.ValueWithError(1,0.1)),"1.00 +/- 0.10")
		self.assertEqual(str(errors.ValueWithError(1,0.01)),"1.000 +/- 0.010")
		self.assertEqual(str(errors.ValueWithError(1,3.54)),"1.0 +/- 3.5")
		self.assertEqual(str(errors.ValueWithError(1,0.354)),"1.00 +/- 0.35")
		self.assertEqual(str(errors.ValueWithError(1,0.0354)),"1.000 +/- 0.035")
		self.assertEqual(str(errors.ValueWithError(1,3.54999)),"1.0 +/- 3.5")
		self.assertEqual(str(errors.ValueWithError(1,0.354999)),"1.00 +/- 0.35")
		self.assertEqual(str(errors.ValueWithError(1,0.0354999)),"1.000 +/- 0.035")

	def test_str_rounding_range2(self):
		"rounding test cases with sig = 355 - 949"
		pass

	def str_value_sign(self):
		self.assertEqual(str(errors.ValueWithError(-1,1)),"-1.00 +/- 1.00")

if __name__ == '__main__':
	unittest.main()
