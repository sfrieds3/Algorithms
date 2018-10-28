def mergesort(arr: []):
    res = []

    if len(arr) < 2:
        return arr

    mid = len(arr)//2
    left_sorted = mergesort(arr[mid:])
    right_sorted = mergesort(arr[:mid])

    i = 0
    j = 0

    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] < right_sorted[j]:
            res.append(left_sorted[i])
            i += 1
        else:
            res.append(right_sorted[j])
            j += 1

    res += left_sorted[i:]
    res += right_sorted[j:]

    return res


if __name__ == "__main__":
    test_array =[0, 5, 6, 2, 7, 1]
    print(mergesort(test_array))
