def bubble_sort(array):
	p1 = 0
	p2 = 1
	end = len(array)

	while end > 0:

		while p1 < len(array) and p2 < len(array):
			if array[p1] <= array[p2]:
				p1 += 1
				p2 += 1
			else:
				array = swap(array, p1, p2)
				p1 += 1
				p2 += 1
		p1 =0
		p2 =1
		end -= 1

	return array


def swap(array, index1, index2):
	temp = array[index1]
	array[index1] = array[index2]
	array[index2] = temp
	print "in swap {}".format(array)
	return array


if __name__ == "__main__":
	array = [5,4,1,3, -3, 3, 10, 0]
	sorted_array = bubble_sort(array)
	print sorted_array