import time
import random


"""
Cite: https://www.geeksforgeeks.org/python-program-for-merge-sort/
Merges two subarrays of arr[].
First sub-array is arr[l..m]
Second sub-array is arr[m+1..r]
"""
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# l is for left index and r is right index of the
# sub-array of arr to be sorted
def mergeSort(arr, l, r):
    if l < r:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l + (r - l) // 2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


"""
Cite: https://www.geeksforgeeks.org/python-program-for-insertion-sort/
"""
def InsertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def DoMergeSort(arr: list):
    start = time.time()
    mergeSort(arr, 0, len(arr) - 1)
    end = time.time()
    print("Time for merge sort:", end - start)


def DoInsertionSort(arr: list):
    start = time.time()
    InsertionSort(arr)
    end = time.time()
    print("Time for insertion sort:", end - start)


if __name__ == '__main__':
    N = 100
    random.seed(10)
    array = [random.random() for _ in range(N)]
    array_ = [i for i in array]
    DoMergeSort(array)
    DoInsertionSort(array_)
