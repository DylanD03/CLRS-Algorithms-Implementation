def Bottom_Up_Cut_Rod(p, n):
	r = [0]*(n+1)

	r[0] = 0 # redundant, just to emulate pseudocode.
	for j in range(1,n+1):
		q = float('-inf')
		for i in range(1, j+1):
			q = max(q, p[i] + r[j-i])
		r[j] = q
	return r[n]


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
		value = Bottom_Up_Cut_Rod(case, len(case)-1)
		print("Optimal profit that can be obtained:", value)
	print()


if __name__ == "__main__":
	main()