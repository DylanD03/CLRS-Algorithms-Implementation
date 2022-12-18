from math import floor
from heap import *
EDGECASES = False

# Heap data structure is implemented in the heap.py file.

def build_min_heap(heap):
	size = heapsize(heap)
	for i in range(floor(size/2),-1,-1):
		min_heapify(heap, i)

def heap_sort(heap):
	build_min_heap(heap)
	ordered = []

	for i in range(0, heapsize(heap)+1):
		ordered.append(heap[0]) # node has the minimal value in the heap
		heap[0], heap[heapsize(heap)] = heap[heapsize(heap)], heap[0]
		heap.pop()
		min_heapify(heap,0)

	return ordered


def main():
	tests = []
	tests.append([1,5,7,3,2,4,6,8])
	tests.append([1,3,5,7,9,11,13,15])
	tests.append([9,5,3,21,2,53,5,21,59,3,5,7])
	tests.append([-1,-2,-1,3,5,6,7,5])

	if EDGECASES:
	    # Testing edge cases
	    print("Edge cases\n\n")
	    tests.append([1,1,1,1,1,1])
	    tests.append([0,0,0,0,0,0,0,0])
	    tests.append([0])

	print("Sorting . . .")
	for test in tests:
		copy = test.copy()
		print("\nBefore:")
		print('\t',test)
		print("After:")
		print('\t', heap_sort(copy))









if __name__ == "__main__":
	main()

