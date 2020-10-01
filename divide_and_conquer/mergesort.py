def mergeSort(array):
    """
    >>> mergeSort([3, 2, 1])
    [1, 2, 3]
    >>> mergeSort([3, 2, 1, 0, 1, 2, 3, 5, 4])
    [0, 1, 1, 2, 2, 3, 3, 4, 5]
    >>> mergeSort([10])
    [10]
    """
    if len(array) == 1:
        return array

    middle = len(array) // 2

    # Split the array into halves till the array length becomes equal to One
    # merge the arrays of single length returned by mergeSort function and
    # pass them into the merge arrays function which merges the array
    leftHalf = array[:middle]
    rightHalf = array[middle:]

    return mergeArrays(mergeSort(leftHalf), mergeSort(rightHalf))


def mergeArrays(leftHalf, rightHalf):
    sortedArray = [None] * (len(rightHalf) + len(leftHalf))

    p1 = 0  # pointer to current index for left Half
    p2 = 0  # pointer to current index for the right Half
    idx = 0  # pointer to current index for the sorted array Half

    while p1 < len(leftHalf) and p2 < len(rightHalf):
        if leftHalf[p1] < rightHalf[p2]:
            sortedArray[idx] = leftHalf[p1]
            p1 += 1
            idx += 1
        else:
            sortedArray[idx] = rightHalf[p2]
            p2 += 1
            idx += 1
    while p1 < len(leftHalf):
        sortedArray[idx] = leftHalf[p1]
        p1 += 1
        idx += 1

    while p2 < len(rightHalf):
        sortedArray[idx] = rightHalf[p2]
        p2 += 1
        idx += 1

    return sortedArray


if __name__ == "__main__":
    import doctest

    doctest.testmod()
