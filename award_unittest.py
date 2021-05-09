import unittest
from award_classifier import *

# create our testing class (OOP)
class TestOrders(unittest.TestCase):
	
	# define our tests
	def test_distinction(self):
		# We 'assert' that the value returned by the function matches
		# the text output provided.
		# If it does, the test is passed, otherwise it is failed.
		self.assertEqual(award_classifier(65, 75, 0.5), 'Distinction')

	def test_fail(self):
		self.assertEqual(award_classifier(45, 54, 0.5), 'Fail')

	def test_merit(self):
		self.assertEqual(award_classifier(65, 55, 0.67), 'Merit')

# if the file is ran execute all the above code
if __name__ == '__main__':
	# If ran in Notebooks we need to replace first argument and prevent
	# automatic close down.
	# If ran from standard Python "unittest.main()" instead
	unittest.main(argv=['first-arg-is-ignored'], exit=False)		