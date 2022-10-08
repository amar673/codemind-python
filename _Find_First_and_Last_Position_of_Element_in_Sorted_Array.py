# Python 3 program to find first and
# last occurrence of an elements in
# given sorted array


# Function for finding first and last
# occurrence of an elements
def findFirstAndLast(arr, n, x):
	first = -1
	last = -1
	for i in range(0, n):
		if (x != arr[i]):
			continue
		if (first == -1):
			first = i
		last = i

	if (first != -1):
		print(first,last)
	else:
		print("-1 -1")


# Driver code
n =int(input())
arr = list(map(int,input().split()))
x =int(input())
findFirstAndLast(arr, n, x)


# This code is contributed by Nikita Tiwari.
