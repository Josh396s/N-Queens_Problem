#------------------------------------------------------------------------------ 
#  Queens.py
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# import statements
#------------------------------------------------------------------------------
import sys

#------------------------------------------------------------------------------
# definitions of optional helper functions
#------------------------------------------------------------------------------
def printMessage(x, y):
	print(x + "-Queens has " + y + " solutions")
	sys.exit()

def initList(n):
	a = int(n)+1
	B = list()
	R = a * [0]
	for x in range(0,a):
		B.append(R[:])
	return B

def errorCode():
	print('Usage: python3 Queens.py [-v] number', file=sys.stderr)
	print('Option: -v verbose output, print all solutions', file=sys.stderr)
	exit()

#------------------------------------------------------------------------------
# definitions of required functions
#------------------------------------------------------------------------------
def placeQueen(B, i, j):
	B[i][j] = 1
	B[i][0] = j
	k = i
	l = j
	n = len(B)-1

	#Downwards
	for q in range(i, n):
		B[k+1][l] -= 1 
		k += 1

	k = i
	l = j
	#Right Diagonal
	for q in range(i, n):
		if k<n and l<n:
			B[k+1][l+1] -= 1
			k += 1
			l += 1

	k = i
	l = j
	#Left Diagonal
	for q in range(i, n):
		if 1<l:
			B[k+1][l-1] -= 1
			k += 1
			l -= 1

def removeQueen(B, i, j):
	B[i][j] = 0
	B[i][0] = 0
	k = i
	l = j 
	n = len(B)-1

	#Downwards
	for q in range(i, n):
		B[k+1][l] += 1
		k += 1
	
	k = i
	l = j
	#Right Diagonal
	for q in range(i, n):
		if k<n and l<n:
			B[k+1][l+1] += 1
			k += 1
			l += 1
	
	k = i
	l = j
	#Left Diagonal
	for q in range(i, n):
		if 1<l:
			B[k+1][l-1] += 1
			k += 1
			l -= 1

def printBoard(B):
#Prints out a solution to n-queens
	n = len(B)
	a = list()
	for i in range(1,n):
		a.append(B[i][0])
	z = tuple(a)
	print(z)


def findSolutions(B, i, mode):
	n = len(B)-1
	a = 0

	if int(i)>n:
		if mode == 'verbose':
			printBoard(B) 
		return 1
	else:
		for j in range(1,n+1):
			if B[i][j] >= 0:
				placeQueen(B,i,j)
				if mode == 'verbose':
					a += findSolutions(B,i+1,'verbose')
				else:
					a += findSolutions(B,i+1,0)
				removeQueen(B,i,j)
	return a

#------------------------------------------------------------------------------
# definition of function main()
#------------------------------------------------------------------------------
def main():
	
	if len(sys.argv)==1:
		errorCode()

	elif sys.argv[1].isdigit():
		x = initList(sys.argv[1])
		print(str(sys.argv[1]) +'-Queens has ' + str(findSolutions(x,1,0)) + ' solutions')


	elif sys.argv[1]=='-v' and len(sys.argv)==2:
		errorCode()


	elif sys.argv[1]=='-v':
		try:
			b = initList(sys.argv[2])
			findSolutions(b,1,'verbose')
			print(str(sys.argv[2]) +'-Queens has ' + str(findSolutions(b,1,0)) + ' solutions')
		except ValueError:
			errorCode()

	else:
		errorCode()
# end
#------------------------------------------------------------------------------
# closing conditional that calls main()
#------------------------------------------------------------------------------
if __name__=='__main__':
	main()
# end
