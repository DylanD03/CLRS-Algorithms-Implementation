import time


def karatsuba_multiply(I, J):
	# I = w * 2^(n/2) + x
	# J = y * 2^(n/2) + z
	n = max(I.bit_length(), J.bit_length())
	if n <= 32:
		return I*J # small numbers 

	n_2 = n // 2

	# Splitting I, and J. 
	w = I >> (n_2) # first half of I
	x = I % (w << n_2) # last half of I
	y = J >> (n_2) 
	z = J % (y << n_2)

	# subproblem 1: w * y
	p = karatsuba_multiply(w, y)

	# subproblem 2: x * z
	q = karatsuba_multiply(x, z)

	# subproblem 3: (w + x) * (y + z)
	r = karatsuba_multiply(w+z, y+z)

	# Inexpensive : w * z + x * y 
	middle_term = r - p - q 

	# (w * y * 2^(n/2)) + ((w * z + x * y) * w^(n/2)) + x * z
	IJ = (p << (2*n_2)) + (middle_term << (n_2)) + q
	return IJ



def main():
	print()
	x = 3141592653589793238462643383279502884197169399375105820974944592
	y = 2718281828459045235360287471352662497757247093699959574966967627
	print('x',x)
	print('y',y)

	start_karatsuba = time.time()
	karatsuba_multiply(x,y)
	end_karatsuba = time.time()
	print("Time for Karatsuba's Algorithm ~O(n^1.58):", end_karatsuba - start_karatsuba)


	start_elementary_multiply = time.time()
	z = x * y
	end_elementary_multiply = time.time()
	print("Time for Elementary Multiplication O(n^2):", end_karatsuba - start_karatsubaend_elementary_multiply - start_elementary_multiply)


if __name__ == "__main__":
	main()