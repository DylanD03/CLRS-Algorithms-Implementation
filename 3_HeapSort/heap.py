# Implementation for a min-heap data structure


def leftchild(index):
	lc = 2*index
	return lc

def rightchild(index):
	rc = (2*index) +1
	return rc

def heapsize(heap):
	size = len(heap) - 1
	return size


def min_heapify(heap, index):
	# turns an almost-heap into a heap
	# pre-condition: tree rooted at A[i] is an almost-heap
	# post-condiiton: tree rooted at A[i] is a heap
	lc = leftchild(index)
	rc = rightchild(index)
	smallest = index

	if lc <= heapsize(heap) and heap[lc] < heap[smallest]:
		smallest = lc
	if  rc <= heapsize(heap) and heap[rc] < heap[smallest]:
		smallest = rc
	if smallest != index:
		heap[index], heap[smallest] = heap[smallest], heap[index]
		min_heapify(heap, smallest)







