import numpy as np
# Time Complexity, O(n + m + nm)
DEBUG = False

def LCS(X,Y):

	n = len(X) 
	m = len(Y) 
	D = np.zeros((n,m))

	# redundant since we use np.zeros()
	# however we keep it to be consistent with the pseudocode
	for i in range(1,n): # O(n)
		D[i, 0] = 0
	for j in range(1,m): # O(m)
		D[0, j] = 0


	for i in range (1, n): # O(nm)
		for j in range(1, m):
			D[i, j] = D[i-1, j] # above
			if D[i, j-1] > D[i, j]: # left
				D[i, j] = D[i, j-1]
			if (X[i] == Y[j] and D[i-1, j-1] + 1 > D[i,j]):
				D[i,j] = D[i-1, j-1] + 1

	PrintLCS(D, n-1, m-1, X, Y)
	return D[n-1, m-1]

def PrintLCS(D, i, j, X, Y):
	if (i > 0 and j > 0):
		if D[i,j] == D[i-1,j]:
			PrintLCS(D, i-1, j, X, Y)
		elif D[i,j] == D[i, j-1]:
			PrintLCS(D, i, j-1, X, Y)
		else:
			assert D[i,j] == 1 + D[i-1, j-1]
			PrintLCS(D, i-1, j-1, X, Y)
			print(X[i], end = '')


def main():
	test_cases = []

	# first item in each string is empty to replicate the 1-indexing of pseudocode
	test_cases.append([ 
		list(" AGCCTNGATC"),
		list(" GAGCCGATTC")
	])	

	test_cases.append([ 
		list(" ACGGA"),
		list(" ACTG")
	])	

	test_cases.append([ 
		list(" 23r1opq@@wepofq kwopfqk2pok"),
		list(" powkafp3fofqw##@!peofkoqpf. pak2p")	
	])

	for case in test_cases:
		print("\n\nExample: ")
		print(1, "".join(case[0]).strip())
		print(2, "".join(case[1]).strip())
		print("LCS:", end = '')
		LCS(case[0], case[1])
	print('\n\n')

	if DEBUG:
		edge_cases = []

		edge_cases.append([
			list(" "),
			list(" ")
		])
		edge_cases.append([
			list(" 11111111111"),
			list("    111111111111")
		])

		for case in edge_cases:
			print("\n\nExample: ")
			print(1, "".join(case[0]).strip())
			print(2, "".join(case[1]).strip())
			print("LCS:", end = '')
			LCS(case[0], case[1])
		print('\n\n')




if __name__ == "__main__":
	main()








