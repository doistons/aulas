import math

class Vector:
	P=[]
	D=0

	def __init__(self,p):
		self.D=len(p)
		self.P=p
		
	def __add__(self,other):
		pp=[]
		for i in range(len(self.P)):
			pp.append(self.P[i]+other.P[i])
		return Vector(pp)
		
	def __iadd__(self,other):
		for i in range(len(self.P)):
			self.P[i]+=other.P[i]
		return self
		
	def __sub__(self,other):
		pp=[]
		for i in range(len(self.P)):
			pp.append(self.P[i]-other.P[i])
		return Vector(pp)
		
	def __isub__(self,other):
		for i in range(len(self.P)):
			self.P[i]-=other.P[i]
		return self
		
	def __mul__(self,a):
		pp=[]
		for i in range(len(self.P)):
			pp.append(self.P[i]*a)
		return Vector(pp)
		
	def __div__(self,a):
		if (a==0.0):
			print "Vetor: divisao por 0"
			exit()
	
		a=1.0/a
		return self*a
		
	def __getitem__(self,i):
		return self.P[i]
		
	def __setitem__ (self,i,value):
		self.P[i]=value
	
	def SC(self,other):
		dot=0.0
		for i in range(len(self.P)):
			dot+=self.P[i]*other.P[i]
		return dot
		
	def Length(self):
		len=self.SC(self)
		return math.sqrt(len)
	
	def Projecao(self,other):
		fator=self.SC(other)/other.SC(other)
		return other*fator

	def __str__(self):
		text="["
		for i in range(len(self.P)):
			text+=str(self.P[i])
			if (i+1)<len(self.P):
				text+=","
		text+="]"
		
		return text
