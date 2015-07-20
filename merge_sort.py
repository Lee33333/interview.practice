def merge_sort(array):
# base case is list of one
	if len(array) == 1:
		return array
	else:
		#split array in half and return array recursively
		array_length = len(array)//2
		#import pdb; pdb.set_trace()
		array1 = merge_sort(array[0:array_length])
		array2 = merge_sort(array[array_length:])

		sorted_array = merge(array1, array2)

	print sorted_array
	return sorted_array

def merge(array1, array2):

	sorted_array = []

	while array1 or array2:
		if array1 and not array2:
			sorted_array.extend(array1)
			array1 = []
		elif array2 and not array1:
			sorted_array.extend(array2)
			array2.pop()
			array2 = []
		elif array1[0] <= array2[0]:
			sorted_array.append(array1[0])
			array1.pop(0)
		else:
			sorted_array.append(array2[0])
			array2.pop(0)
	return sorted_array


if __name__ == "__main__":
	array = [5, 4, 1, 8, 12, 3, 9, 11]
	merge_sort(array)