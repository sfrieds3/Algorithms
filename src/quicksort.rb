
def partition(array, p, r)
  pivot = array[r]
  i = p-1

  j = p
  until j == r do
    if array[j] <= pivot
      i += 1
      array[i], array[j] = array[j], array[i]
    end
    j += 1
  end

  i += 1
  array[i], array[r] = array[r], array[i]

  i
end

def quicksort(array, p, r)
  if p < r
    q = partition(array, p, r)
    quicksort(array, p, q-1)
    quicksort(array, q+1, r)
  end
  array
end

arr = [1, 7, 3, 0, 10, 50, 30, 2]

n = arr.size - 1
puts(quicksort(arr, 0, n))
