#  Given a string in the form "AAAABBBBCCCCCDDEEE" compress it to become "A4B4C5D2E4".

# Input: String
# Output: String

# Test Case : "AAAABBBBCCCCCDDEEEE"
# "A4B4C5D2E4"

# Create a hashtable to store counts of elements
# Iterate through the given string
#	If current element is in the hashtable:
		# Incremenet the value of current element
	# add key with an initial value


def string_compression(str):
	dict = {}
	compressed_string = []
	for letter in str:
		if letter in dict:
			dict[letter] += 1
		else:
			dict[letter] = 1

	print(dict)

	for key, value in dict:
		print(key)
		print(value)
		compressed_string.append(key)
		compressed_string.append(value)

	# print(compressed_string)

string_compression("AAAABBBBCCCCCDDEEEE")


