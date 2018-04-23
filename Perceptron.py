import numpy as np
class Perceptron:
	def __init__(self,w1,w2,b):
		self.w1 = w1
		self.w2 = w2
		self.b = b
	def do(self,x1,x2):
		x = np.array([x1,x2])
		w = np.array([self.w1,self.w2])
		b = self.b
		tmp = np.sum(w*x) + b
		if tmp <= 0:
			return 0
		else:
			return 1

