import math

class Vector:
	P=[]

	def __init__(self,p):
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
		other=1.0*other
		pp=[]
		for i in range(len(self.P)):
			pp.append(self.P[i]/a)
		return Vector(pp)
		
	def SC(self,other):
		dot=0.0
		for i in range(len(self.P)):
			dot+=self.P[i]*other.P[i]
		return dot
		
	def Length(self):
		len=self.SC(self)
		return math.sqrt(len)
	
	def Project(self,other):
		fator=self.SC(other)/other.SC(other)
		return other*fator

	def Write(self):
		text="["
		for i in range(len(self.P)):
			text+=str(self.P[i])
			if (i+1)<len(self.P):
				text+=","
				
			print text
			
	def Complement(self):
		


print ('Projecao')			
v=Vector([1,2,3])
w=Vector([-1,1,3])
pro=w.Project(v)
pro.Write()


