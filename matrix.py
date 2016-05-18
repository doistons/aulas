import math

class Matrix:
	A=[]
	R=0
	S=0
	
	def __init__ (self,A):
		self.R=len(A)
		self.S=len(A[0])
		
		self.A=A
		
	def __str__(self):
		
		text="["
		for i in range (self.R):
			text=text + "\n ["
			for j in range (self.S):
				text+=str(self.A[i][j])
				if (j+1<self.S):
					text+=","
			if (i+1<self.R):
				text+="] \n"
			else:
				text+="] \n"
		
		return text	

	def CheckDimensions (self,other):
		if (self.R!=other.R or self.S!=other.S):
			print "Add: Invalid measure of rows or columns"
			exit()
			
	def __add__ (self,other):
		self.CheckDimensions(other)
		
		AA=[]
		for i in range(self.R):
			AA.append([])
			for j in range(self.S):
				AA[i].append(self.A[i][j])
		return Matrix(AA)
		
	def __mul__ (self,other):
		
		name1="Matrix"
		name2="Vector"
		othername=other.__class__.__name__
		
		AA=[]
		if (othername==name1):
			if (self.S!=other.R):
				print "Mult Matrix: Invalid Dimensions"
				exit()
				
			for i in range(self.R):
				AA.append([])
				for j in range (other.S):
					cij=0
					for k in range (self.S):
						cij+=self.A[i][k]*other.A[k][j]
					AA[i].append(cij)
		
		elif (othername==name2):
			if (self.S!=other.D):
				print "Mult Vector: Invalid Dimensions"
				exit()
				
			P=[]
			for i in range (self.R):
				cij=0
				for j in range(other.D):
					cij+=self.A[i][j]*other.P[j]
				P.append(cij)
				
			return Vector (P)
			
		else:
			a=other
			for i in range(self.R):
				AA.append([])
				for j in range(self.S):
					AA[i].append(a*self.A[i][j])
					
		return Matrix(AA)
		
A=Matrix([
[2.0,3.0,1.0],
[9.0,6.0,3.0],
[5.0,2.0,4.0],
])

B=Matrix([
[1.0,2.0,3.0],
[3.0,2.0,1.0],
[2,0,1.0,3.0],
])

print A*B
		
