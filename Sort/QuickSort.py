def QuickSort(arr):

    QuickSortHelper(arr, 0, len(arr) - 1)
    return arr


def QuickSortHelper(arr, first, last):

    if first < last:

        splitPoint = Partition(arr, first, last)

        # Quick sort on left and right half of the split point
        QuickSortHelper(arr, first, splitPoint - 1)
        QuickSortHelper(arr, splitPoint + 1, last)


def Partition(arr, first, last):

    pivotValue = arr[first]

    leftMark = first + 1
    rightMark = last

    done = False

    while not done:

        # Move left mark to the right
        while leftMark <= rightMark and arr[leftMark] <= pivotValue:
            leftMark += 1

        # Move right mark to the left
        while rightMark >= leftMark and arr[rightMark] >= pivotValue:
            rightMark -= 1

        # If right mark crosses over to the left, stop
        if rightMark < leftMark:
            done = True
        # Else, swap
        else:
            temp = arr[leftMark]
            arr[leftMark] = arr[rightMark]
            arr[rightMark] = temp

    # Swap first element with the right mark after going through the above loop
    temp = arr[first]
    arr[first] = arr[rightMark]
    arr[rightMark] = temp

    return rightMark
