#  Given two strings, check to see if they are anagrams.

# Input: String, String
# Output: Boolean

# Test Case: 

# Input: "dog", "god"
# Output: True

# Create a hashatable for first string
# Create a hashtable for second string

# Iterate through first string
	# Add element and count to hashtable

# Iterate through second string
	# Add element and count to hashtable

# Compare first and second hashtable

def anagram(s1,s2):

	string_one_histogram = {}
	string_two_histogram = {}

	for letter in s1:
		if letter in string_one_histogram:
			string_one_histogram[letter] += 1
		else:
			string_one_histogram[letter] = 1

	for letter in s2:
		if letter in string_two_histogram:
			string_two_histogram[letter] += 1
		else:
			string_two_histogram[letter] = 1

	return string_one_histogram == string_two_histogram

print(anagram("dog","god")) 
# Returns true
print(anagram("dog","egg"))
# Returns false
			

