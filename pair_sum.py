# Given an integer array, output all the unique pairs that sum up to a specific value k

# Input: [Int], Int
# Output: [[Int]] || []

# Test Case: [1,3,2,2], 4
# Output: [[1,3], [2,2]]

# Create an empty array to store pairs
# Create a hashtable to store elements of the array
# Iterate through the given array
	# Check if k - current element is in array
		# Add to the pair array
# Return pair array

def pair_sum(arr, k):
	pairs = []
	elements = {}

	for number in arr:
		if k - number in elements:
			pairs.append((number, k - number))
		elements[number] = True

	return pairs

print(pair_sum([1,3,2,2], 4))
