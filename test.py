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
		self.assertEqual(1,AND.do(1,1))
		self.assertEqual(0,AND.do(0,1))
		self.assertEqual(0,AND.do(1,0))
		self.assertEqual(0,AND.do(0,0))
	def test_nand(self):
		NAND = fortest.Perceptron(w1=-0.5,w2=-0.5,b=0.7)
		self.assertEqual(1,NAND.do(0,1))
		self.assertEqual(1,NAND.do(1,0))
		self.assertEqual(1,NAND.do(0,0))
		self.assertEqual(0,NAND.do(1,1))
if __name__ == '__main__':
	unittest.main()
