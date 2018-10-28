'''
POC for quicksort
'''


def partition(A: [], p: int, r:int) -> int:
    pivot = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    i += 1
    A[i], A[r] = A[r], A[i]
    return i

def quicksort(A: [], p:int, r: int):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

arr = [0, 10, 7, 5, 3, 2, 200, 50, 17, 32, 9]
n = len(arr)-1
quicksort(arr, 0, n)

print(arr)
