# Performs Binary Search for a key in a sorted array. 
# O(log (n)) time complexity
from math import floor
EDGECASES = False



def binary_search(array, key, lo, hi):
	# searching in a sorted array
	assert (sorted(array) == array)

	while lo <= hi:
		mid = floor((lo + hi)/2)
		if array[mid] < key:
			lo = mid+1
		elif array[mid] > key:
			hi = mid-1
		elif array[mid] == key:
			return mid
	
	return None # did not find the key in the array

def main():
	tests = []
	tests.append([1,5,7,3,2,4,6,8])
	tests.append([1,3,5,7,9,11,13,15])
	tests.append([9,5,3,21,2,53,5,21,59,3,5,7])
	tests.append([-1,-2,-1,3,5,6,7,5])

	searches = [3,6,21,-1]

	if EDGECASES:
		# Testing edge cases
		print("Edge cases\n\n")
		tests.append([1,1,1,1,1,1])
		tests.append([0,0,0,0,0,0,0,0])
		tests.append([0])
		searches.extend([0,0,0])

	print("\nUsing 0-indexing:")
	for i, test in enumerate(tests):
		test.sort()
		print("\nSearching for:",searches[i],  "\nIn Array: ", test)
		index = binary_search(test, searches[i], 0, len(test)-1)
		if index == None:
			print("The key is not in the array!")
		else:
			print("Key Index:", index)


if __name__ == "__main__":
	main()