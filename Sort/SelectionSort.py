def SelectionSort(arr):

    # range(len(arr)-1, 0, -1) arranges arr in backwords excluding the last element
    for fillslot in range(len(arr) - 1, 0, -1):
        positionMax = 0

        # For every set of 0 to fillslot+1
        for location in range(1, fillslot + 1):
            # Traverse through the array to find maximum's location
            if arr[location] > arr[positionMax]:
                positionMax = location

        temp = arr[fillslot]
        arr[fillslot] = arr[positionMax]
        arr[positionMax] = temp

    return arr
