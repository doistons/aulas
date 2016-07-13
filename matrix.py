import math

from Vector import Vector

class Matrix:
	M=[]
	R=0
	S=0
	
	def __init__ (self,A):
		self.R=len(A)
		self.S=len(A[0])
		
		self.M=A
		
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
		
	def __getitem__(self,i):
		return self.M[i]
		
	def __setitem__(self,i,value):
		self.M[i]=value

	def CheckDimensions (self,other):
		if (self.R!=other.R or self.S!=other.S):
			print "Add: Invalid measure of rows or columns"
			exit()
	
	def NormInf(self):
		norm=0.0
		for i in range(self.R):
			for j in range(self.S):
				if (abs(self.M[i][j])>norm):
					norm=abs(self.M[i][j])
		
		return norm
			
	def __add__ (self,other):
		self.CheckDimensions(other)
		
		AA=[]
		for i in range(self.R):
			AA.append([])
			for j in range(self.S):
				AA[i].append(self.A[i][j])
		return Matrix(AA)
		
	def __sub__(self, other):
		self.CheckDimensions(other)
		
		AA=[]
		for i in range(self.R):
			AA.append([])
			for j in range(self.S):
				AA[i].append(self.M[i][j]-other.M[i][j])
		print Matrix(AA)
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
						cij+=self.M[i][k]*other.M[k][j]
					AA[i].append(cij)
		elif (othername==name2):
			if (self.S!=other.D):
				print "Mult Vector: Invalid Dimensions"
				exit()
				
			P=[]
			for i in range (self.R):
				cij=0
				for j in range(other.D):
					cij+=self.M[i][j]*other.P[j]
				P.append(cij)
				
			return Vector(P)
			
		else:
			a=other
			for i in range(self.R):
				AA.append([])
				for j in range(self.S):
					AA[i].append(a*self.A[i][j])
					
		return Matrix(AA)
	
	def SwapRows(self,i1,i2):
		if (i1!=i2):
			tmp=self.M[i1]
			self.M[i1]=self.M[i2]
			self.M[i2]=tmp
	
	
	#Matriz B	
	def GaussForward(self,B):
		for i in range(0,self,R):
			ipiv=i
			max=0.0
			for j in range(i,self.S):
				if (abs(self.M[i][j]>max)):
					max=self.M[i][j]
					ipiv=j
			self.SwapRows(i,ipiv)
			B.SwapRows(i,ipiv)
			
			fact=1.0*self.M[i][i]
			
			if (fact==0.0):
				print "Matrz Singular em %d, %d: %f" %(i,i,self.M[i][i])
				exit()
			
			fact=1.0/fact
		
			#Divide pivote row
			self.M[i][i]=1.0
			for j in range(0,B.S):
				B[i][j]*=fact
			for j in range(i+1,self.S):
				self.M[i][j]*=fact
				
			for j in range(i+1,self.R):
				fact=self.M[j][i]
				self.M[j][i]=0.0
				
				for k in range(0,B.S):
					B[j][k]-=fact*B[i][k]
					
				for k in range(i+1,self.S):
					self.M[j][k]-=fact*self.M[i][k]
			
	def GaussBackward(self,B):
		for i in range(self.R-1,0,-1):
			for j in range(i-1,-1,-1):
				fact=self.M[j][i]
				
				for k in range(0,B.S):
					B[j][k]-=fact*B[i][k]
				
				for k in range(i,-1,-1):
					self.M[j][k]-=fact*self.M[i][k]
					
	def Gauss(self,B):
		self.GaussForward(B)
		self.GaussBackward(B)
		return B
	
	def Vandermonte(a):
		A=[]
		for i in range (0,a,D):
			A.append([])
			
			aa=1.0
			for j in range(0,a.D):
				A[i].append(aa)
				aa*=a[i]
		return Matrix(A)
		
	a=Vector([2,3,4,5])
	A=Vandermonte(a)
	
	A=Matrix([[0,1,2,3],[2,3,4,5],[3,4,5,6],[4,5,6,7]])
	AA=A
	
	B=Vandermonte(a)
	BB=B
	
	X=A.Gauss(B)
	R=AA*X-BB

print AA
print BB
print R
print "R_a=%e, R_r=%e" %(R.NormInf(),R.NormInf()/AA.NormInf())
