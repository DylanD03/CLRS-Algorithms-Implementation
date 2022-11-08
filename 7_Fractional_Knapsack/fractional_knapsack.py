
class Item:
	def __init__(self, w, b, name):
		# w = weight of the item
		# b = total value 
		assert (w > 0)
		assert (b > 0)
		self.w = w
		self.b = b
		self.name = name


def fractional_knapsack(W, S):
	# W is the weight of the knapsack, and S is set of items.
	# O(nlogn) time complexity dominated by the sorting.
	S.sort(key=lambda item: (item.b/item.w), reverse = True)

	optimal_value = 0
	current_weight = 0
	x = [0]*(len(S))
	# S is sorted by value, using greedy algorithm.
	i = 0
	while current_weight < W and i < len(S):
		x[i] = min(S[i].w, W - current_weight)
		current_weight += x[i]
		optimal_value += ((S[i].b)/(S[i].w))
		i += 1

	print('\nGreedy Solution Yields: ')
	for i in range(0,i):
		print(x[i],"of",S[i].name)
	print('With a total knapsack value of',optimal_value)




def main():

	S = [Item(2, 6, 'Cumin'),
		Item(2, 8, 'Saffron'),
		Item(5, 10, 'Pepper'),
		Item(1.5, 4, 'Nutmeg'),
		Item(1, 3, 'Turmeric'),
		Item(3, 9, 'Paprika')]
	fractional_knapsack(4, S)

	S = [Item(2, 6, 'Cumin'),
		Item(2, 8, 'Saffron'),
		Item(5, 10, 'Pepper'),
		Item(1.5, 4, 'Nutmeg'),
		Item(1, 3, 'Turmeric'),
		Item(3, 9, 'Paprika')]
	fractional_knapsack(10, S)

	S = [Item(2, 6, 'Cumin'),
		Item(2, 8, 'Saffron'),
		Item(5, 10, 'Pepper')]
	fractional_knapsack(40, S)










if __name__ == "__main__":
	main()