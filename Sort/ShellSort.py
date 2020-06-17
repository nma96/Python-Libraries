def ShellSort(arr):

    sublistCount = len(arr) // 2

    # While we still have sub lists
    while sublistCount > 0:
        for start in range(sublistCount):

            # Use a gap insertion
            gapInsertionSort(arr, start, sublistCount)

        sublistCount = sublistCount // 2


def gapInsertionSort(arr, start, gap):
    for i in range(start + gap, len(arr), gap):

        currentvalue = arr[i]
        position = i

        # Using the Gap
        while position >= gap and arr[position - gap] > currentvalue:
            arr[position] = arr[position - gap]
            position -= gap

        # Set current value
        arr[position] = currentvalue
