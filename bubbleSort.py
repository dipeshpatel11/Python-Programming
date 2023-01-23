def bubbleSort(toSort_arr):
	n = len(toSort_arr)

	for i in range(n):  # Traverse through all array elements
		for j in range(0, n-i-1):

			# Swap if the element found is greater than the next element
			if toSort_arr[j] > toSort_arr[j+1]:
				toSort_arr[j], toSort_arr[j+1] = toSort_arr[j+1], toSort_arr[j]


if __name__ == "__main__":
    
    toSort_arr = [7, 45, 11, 4, 5, 12, 6 , 8]

    bubbleSort(toSort_arr)

    print("Sorted array is:")
    for i in range(len(toSort_arr)):
        print("%d" % toSort_arr[i], end=" ")
