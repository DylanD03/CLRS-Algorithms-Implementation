Karatsuba's Algorithm: Idea

Instead of having 4 subproblems (multiplications), we only need 3 using Karatsuba's algorithm.


What are the 3 sub problems?

Suppose
I = w * 2^(n/2) + x
J = y * 2^(n/2) + z

Then 
I * J =   (w * y * 2^(n/2)) + ((w * z + x * y) * w^(n/2)) + x * z

note any multiplications of 2^k is done in O(1) time. As it corresponds to a left shift in bits in memory, which is relatively simple and fast.

This yields
4 subproblems :
w * y
w * z
x * y
x * z

let r = (w+x)(y+z) = w * y + (w * z + x * y) + x * z
Karatsuba's algorithm yields 
3 subproblems :
w * y = p
x * z = q
(w + x) * (y + z) = r

Then the middle term of I * J is 
r - p - q

To run the program use:
	python3 karatsuba_algorithm.py

![Example Usage](/8_Karatsuba_Algorithm/Example-Usage.png?raw=true)


