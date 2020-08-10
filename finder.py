# Consider an array of non-negative integers. A second array is formed by shuffling the elements
# of the first array and deleting a random element. Given these two arrays, find which element 
# is missing in the second array

# Input: [Int], [Int]
# Output: Int

# Test Case: [1,2,3,4,5,6,7], [3,7,2,1,4,6]
# Output: 5

def finder(arr1,arr2):
	missing_element = 0
	for number in arr1:
		missing_element += number

	for number in arr2:
		missing_element -= number

	return missing_element

print(finder([1,2,3,4,5,6,7], [3,7,2,1,4,6]))