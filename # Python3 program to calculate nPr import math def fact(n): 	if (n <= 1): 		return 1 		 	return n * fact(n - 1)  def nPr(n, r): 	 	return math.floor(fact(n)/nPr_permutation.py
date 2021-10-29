# Python3 program to calculate nPr
import math
def fact(n):
	if (n <= 1):
		return 1
		
	return n * fact(n - 1)

def nPr(n, r):
	
	return math.floor(fact(n) /
				fact(n - r))
	
# Driver code
n = 5
r = 2

print(n, "P", r, "=", nPr(n, r))

# This code contributed by Rajput-Ji
