# Day 13 - 49: Sorting and Searching Algorithms
# 10 practical programs

# 1. Bubble sort
def bubble_sort(arr):
    arr = arr[:]
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 2. Selection sort
def selection_sort(arr):
    arr = arr[:]
    for i in range(len(arr)):
        minimum = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[i], arr[minimum] = arr[minimum], arr[i]
    return arr

# 3. Insertion sort
def insertion_sort(arr):
    arr = arr[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# 4. Binary search
def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# 5. Find first occurrence
def first_occurrence(arr, target):
    left, right, answer = 0, len(arr)-1, -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            answer = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return answer

# 6. Find maximum and minimum
def min_max(arr):
    return min(arr), max(arr)

# 7. Find kth largest
def kth_largest(arr, k):
    return sorted(arr, reverse=True)[k-1]

# 8. Merge two sorted arrays
def merge_sorted(a, b):
    i = j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i]); i += 1
        else:
            result.append(b[j]); j += 1
    return result + a[i:] + b[j:]

# 9. Find missing number from 1..n
def missing_number(arr, n):
    return n*(n+1)//2 - sum(arr)

# 10. Check if array is sorted
def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))


numbers = [64, 25, 12, 22, 11]
print("1. Bubble:", bubble_sort(numbers))
print("2. Selection:", selection_sort(numbers))
print("3. Insertion:", insertion_sort(numbers))
sorted_numbers = sorted([1, 3, 5, 7, 9, 11])
print("4. Binary search:", binary_search(sorted_numbers, 7))
print("5. First occurrence:", first_occurrence([1,2,2,2,5], 2))
print("6. Min/Max:", min_max(numbers))
print("7. 2nd largest:", kth_largest(numbers, 2))
print("8. Merge:", merge_sorted([1,3,5], [2,4,6]))
print("9. Missing:", missing_number([1,2,3,5], 5))
print("10. Sorted?:", is_sorted([1,2,3,4]))
