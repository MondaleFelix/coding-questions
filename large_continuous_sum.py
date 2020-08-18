# Given an array of integers (positive and negative) find the largest continuous sum

# Input: [Int]
# Output: Int

# Test Case: 
# Input: [1, 2, -1, 3, 4, 10, 10, -10, -1]
# Output: 29

# Have a count variable
# Have a highest sum variable
# Iterate through the array 
	# Increment count variable
	# Check if count variable is less than  highest sum variable
		# Reassign Highest Variable
# Return  the highest variabel

def largest_continous_sum(arr):
	count = 0
	largest_sum = 0
	for number in arr:
		count += number
		if count > largest_sum:
			largest_sum = count
	return largest_sum

print(largest_continous_sum([1, 2, -1, 3, 4, 10, 10, -10, -1]))