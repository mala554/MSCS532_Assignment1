def insertion_sort_decreasing(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Compare with arr[j] < key instead of arr[j] > key
        # so smaller elements shift right, producing descending order
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    sample = [5, 2, 9, 1, 5, 6]
    print("Original:", sample)
    print("Sorted (decreasing):", insertion_sort_decreasing(sample))

    sample2 = [3, 7, 4, 9, 1]
    print("Original:", sample2)
    print("Sorted (decreasing):", insertion_sort_decreasing(sample2))
    