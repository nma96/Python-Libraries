def MergeSort(arr):

	if len(arr) > 1:

		# Split into left half and right half
		mid = len(arr) // 2
		leftHalf = arr[:mid]
		rightHalf = arr[mid:]

		# recursivly merge the 2 halves
		MergeSort(leftHalf)
		MergeSort(rightHalf)

		# i is for left half and j is for right half and k is for final merging
		i = 0
		j = 0
		k = 0

		# Check: are we still in the left half and right half?
		while i < len(leftHalf) and j < len(rightHalf):
			if leftHalf[i] < rightHalf[j]:
				arr[k] = leftHalf[i]

				i += 1

			else:
				arr[k] = rightHalf[j]
				j += 1

			k += 1

		while i < len(leftHalf):
			arr[k] = leftHalf[i]
			i += 1
			k += 1

		while j < len(rightHalf):
			arr[k] = rightHalf[j]
			j += 1
			k += 1
	# print(arr)
	return arr
