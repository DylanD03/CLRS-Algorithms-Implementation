import numpy as np
import random
# For integral knapsack you either take all of the item, or none of it.
# Compared to fractional knapsack, you can take any any amount/weight of the item.
DEBUG = False

class Item:
	def __init__(self, w, v, name):
		# w = weight of the item
		# b = total value 
		assert (w > 0)
		assert (v > 0)
		self.w = w
		self.v = v
		self.name = name

def fractional_knapsack(W, S):
	# Bottom up Implementation (faster than top down)
	# W is the weight of the knapsack, and S is set of items.
	
	# A 2D array with rows equalling the number of items (consistent with the pseudocode)
	DP_knapsack = np.zeros((len(S),W+2))  

	# when weight is 0 # redundant as we use np.zeros, just there to replicate pseudocode
	for i in range(len(S)): # for i<-1 to n do
		DP_knapsack[i,0] = 0

	# when number of items is 0 
	for D in range(W+2): 
		DP_knapsack[0,D] = 0

	# bottom up processing
	for i in range(1,len(S)): # pseudocode is 1-indexed and python is 0 indexed, so we adjust bounds here to (1,S)
		for D in range(1,W+1): 
			DP_knapsack[i,D] = DP_knapsack[i-1,D]
			if D >= S[i].w and DP_knapsack[i,D] < DP_knapsack[i-1, D - S[i].w] + S[i].v:
				DP_knapsack[i,D] = DP_knapsack[i-1, D - S[i].w] + S[i].v


	# All subproblems and the inital problem has been solved
	Print_Opt_Knapsack(DP_knapsack, len(S)-1, W, S)
	return DP_knapsack[len(S)-1,W] 


def Print_Opt_Knapsack(DP_knapsack, i, D, S):
	if (i > 0 and D > 0):
		if DP_knapsack[i, D] == DP_knapsack[i-1, D]:
			Print_Opt_Knapsack(DP_knapsack, i-1, D, S)
		else:
			Print_Opt_Knapsack(DP_knapsack, i-1, D-S[i].w, S)
			print(S[i].name)




def main():
	
	# first item is empty to replicate the 1-indexing of pseudocode
	test_cases = [[[], 
		Item(2, 6, 'Cumin'), # weight, value, name
		Item(2, 8, 'Saffron'),
		Item(5, 10, 'Pepper'),
		Item(1, 4, 'Nutmeg'),
		Item(1, 3, 'Turmeric'),
		Item(3, 9, 'Paprika')]]

	test_cases.append( [[],
		Item(2, 6, 'Cumin'),
		Item(2, 8, 'Saffron'),
		Item(5, 10, 'Pepper'),
		Item(2, 4, 'Nutmeg'),
		Item(1, 3, 'Turmeric'),
		Item(3, 9, 'Paprika')]
	)

	test_cases.append( [[],
		Item(2, 6, 'Cumin'),
		Item(2, 8, 'Saffron'),
		Item(5, 10, 'Pepper')]
	)

	for i, case in enumerate(test_cases):
		W = random.randint(1,11)
		print("Testing case number:", i, "\nWith weight:", W)
		print("Items selected: ")
		fractional_knapsack(W, case)
		print('\n')
		
	if DEBUG:
		edge_cases = [ [[],
			Item(1, 5, 'Cumin'),
			Item(4, 8, 'Saffron')]
		]
		for case in edge_cases:
			fractional_knapsack(0, case)
			fractional_knapsack(10000, case)




if __name__ == "__main__":
	main()