def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        piv = arr[len(arr) // 2]
        left = [x for x in arr if x < piv]
        middle = [x for x in arr if x == piv]
        right = [x for x in arr if x > piv]
        return quicksort(left) + middle + quicksort(right)
