# using memoization
# memoization: Compute the smaller sub problems "on demand"
	# Initialize all table entries with a special "not computed" flag
	# at flagged entry,
	# compute, then replace the flag with true value


def Top_Down_Cut_Rod(n,p):
	memoized = [0]*(n+1)

	# can be simplified. But would rather keep it similar to pseudocode.
	for i in range(1,n+1): 
		memoized[i] = float('-inf') # "not computed" flag
	return Memoized_Cut_Rod(n,p, memoized)

def Memoized_Cut_Rod(n,p, memoized):
	if memoized[n] >= 0:
		return memoized[n] # already computed
	if n == 0:
		return 0 
	else:
		q = float('-inf')
		for i in range(1,n+1):
			q = max(q, p[i] + Memoized_Cut_Rod(n-i,p,memoized))
		
		memoized[n] = q
		Print_Memoized(memoized, n, p)
		return q

def Print_Memoized(memoized, n, p):
	if n == len(p)-1:
		print("Memoized Array:")
		print(memoized)

def main():

	test_cases = []
	# first item is empty to replicate the 1-indexing of pseudocode
	test_cases.append([None, 2, 6, 7, 11, 13])				# value = 14
	test_cases.append([None, 1, 5, 8, 9])					# value = 10
	test_cases.append([None, 1, 5, 8, 9, 10, 17, 17, 20])	# value = 22
	test_cases.append([None, 1, 5, 8, 9, 10, 17, 17, 30])	# value = 30


	for case in test_cases:
		print("\nExample: ")
		print(case)
		value = Top_Down_Cut_Rod(len(case)-1, case)
		print("Optimal profit that can be obtained:", value)
	print()


if __name__ == "__main__":
	main()