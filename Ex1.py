import math
import operator
import numpy as np

class Vector:
	P=[]
	
	def __init__(self,p):
		self.P=p
		
		
	def Sum(self,other):
		pp=[]
		for i in range(len(self.P)):
			pp.append(self.P[i]+other.P[i])
		return Vector(pp)
        
	def Mult(self,a):
		pp=[]
		for i in range(len(self.P)):
			pp.append(self.P[i]*a)
		return Vector(pp)
		
	def DotProduct(self,other):
		dot=0.0
		for i in range(len(self.P)):
			dot+=self.P[i]*other.P[i]
		return dot
			
	def Length(self):
		len=self.DotProduct(self)
		return math.sqrt(len)
		
	def Project(self,other):
		fator=self.DotProduct(other)/other.DotProduct(other)
		return other*fator

	def Angle(self, other):
		return math.acos(self.DotProduct(other) / (self.Length() * other.Length()))
		
	def Norm_1(self):
		n = np.array(self)
		np.linalg.norm(n)

	def Write(self):
		for i in range(len(self.P)):
			print "%f" % self.P[i]
		return 0
		



v=Vector([1,2,3])
w=Vector([4,5,6])

pro=w.Sum(v)
print ('Soma')
pro.Write()
print ('Multiplicacao')
c=2
x=v.Mult(c)
x.Write()
print ('Angulo')
print "%f" % v.Angle(w)
print ('Norma')

