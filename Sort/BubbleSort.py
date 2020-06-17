# Bubling up (Bigger element on the right)


def BubbleSort(arr):
    # range(len(arr)-1, 0, -1) arranges arr in backwords excluding the last element
    for n in range(len(arr) - 1, 0, -1):
        for k in range(n):
            if arr[k] > arr[k + 1]:
                # Swap
                temp = arr[k]
                arr[k] = arr[k + 1]
                arr[k + 1] = temp
            # print(arr) # to print after each step
    return arr

# arr = [5, 3, 7, 2]
# BubbleSort(arr)
