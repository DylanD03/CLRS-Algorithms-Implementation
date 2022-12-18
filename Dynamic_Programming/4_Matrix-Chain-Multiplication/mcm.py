import numpy as np
DEBUG = False


def QuickestMultiplication(d, n):
	# Pseudo code has input as individual entries (d_0, d_1, ...., d_n)
	# Simplifying it using an array
	M = np.zeros((n+2, n+2))
	S = np.zeros((n+2, n+2))
	for i in range(1, n+1):
		M[i,i] = 0
		S[i,i] = float('-inf') # flag
	for gap in range(1, n): # O(n^3)
		for i in range(1, n - gap + 1):
			M[i, i+gap] = float('inf')
			for k in range(0, gap):
				cut_at_k = M[i, i+k] + M[i+k+1, i+gap] + d[i-1]*d[i+k]*d[i+gap]
				if (cut_at_k < M[i, i+gap]):
					M[i,i+gap] = cut_at_k
					S[i,i+gap] = i+k
	Print_Opt_Order(S, 1, n)
	return M[1,n]

def Print_Opt_Order(S, i, j):
	if (i == j):
		print('A'+str(i), end='')
	else:
		print('(', end='')
		Print_Opt_Order(S,int(i),int(S[i,j]))
		print(')x(', end='') 
		Print_Opt_Order(S, int(S[i,j])+1,int(j))
		print(')', end='')


def main():

	test_cases = []
	test_cases.append([1,3,2]) 									# 6 
	test_cases.append([5,2,6,4,3]) 								# 102
	test_cases.append([5,4,10,6,2,7,15,17,23]) 					# 1972
	test_cases.append([12,11,7,6,5,4,3,2,1,10,9,8,1,2,3,7,8,9,4,5,6,10,11])	# 1034

	for case in test_cases:
		print("\nMultiplying an array with dimensions:")
		for i in range(len(case)):
			print(case[i], end = '')
			if i != len(case)-1:
				print('x', end = '')
		print('')
		value = QuickestMultiplication(case, len(case)-1)
		print("\nOptimal cost:", int(value))
	print()



if __name__ == "__main__":
	main()
