import unittest
import Perceptron as fortest
class TestPerceptron(unittest.TestCase):
	def test_init(self):
		perceptron = fortest.Perceptron(0.5,0.5,-0.7)
		self.assertEqual(perceptron.w1,0.5)
		self.assertEqual(perceptron.w2,0.5)
		self.assertEqual(perceptron.b,-0.7)
	def test_and(self):
		AND = fortest.Perceptron(0.5,0.5,-0.7)
		self.assertEquals(1,AND.do(1,1))
if __name__ == '__main__':
	unittest.main()
