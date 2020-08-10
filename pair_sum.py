#  Given an integer array, output all the unique pairs that sum
 # up to a specific value k



def pair_sum(num_list, k):

	for num1 in num_list:
		for  num2 in num_list:
			if num1 + num2 == k:
				print((num1,num2))




pair_sum([1,4,5,2,4], 10)