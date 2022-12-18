def Partition(A, p ,r):
	i = p - 1
	pivot = A[r]

	for j in range(p, r):
		if A[j] < pivot:
			i += 1
			A[i], A[j] = A[j], A[i]
	i += 1
	A[i], A[r] = A[r], A[i]
	return i


def QuickSort(A, p, r):
	# In place quicksort
	if (p <= r):
		pivot = Partition(A, p, r)
		# A[pivot] = pivot
		# All elements <= pivot appear in A[p,....,pivot-1]
		# All elements >= pivot appear in A[pivot+1,....,r]

		QuickSort(A, p, pivot-1)
		QuickSort(A, pivot+1, r)


def main():
	TestCases = []
	TestCases.append([10, 80, 30, 90, 40, 50, 70])
	TestCases.append([1, 3, 5, 7, 2, 4, 6, 8, 10])
	TestCases.append([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])


	for A in TestCases:
		print('')
		print("before: \n", A)
		QuickSort(A, 0, len(A)-1)
		print("After: \n", A, '\n')


if __name__ == "__main__":
	main()









