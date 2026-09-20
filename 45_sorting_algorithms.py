# Day 12 - 45: Sorting Algorithms

# 1. Bubble Sort
def bubble_sort(a):
    a = a[:]
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

# 2. Selection Sort
def selection_sort(a):
    a = a[:]
    for i in range(len(a)):
        m = i
        for j in range(i+1, len(a)):
            if a[j] < a[m]:
                m = j
        a[i], a[m] = a[m], a[i]
    return a

# 3. Insertion Sort
def insertion_sort(a):
    a = a[:]
    for i in range(1, len(a)):
        key, j = a[i], i-1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a

# 4. Merge Sort
def merge_sort(a):
    if len(a) <= 1:
        return a[:]
    mid = len(a)//2
    left, right = merge_sort(a[:mid]), merge_sort(a[mid:])
    result = []
    while left and right:
        result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
    return result + left + right

# 5. Quick Sort
def quick_sort(a):
    if len(a) <= 1:
        return a[:]
    pivot = a[len(a)//2]
    return (quick_sort([x for x in a if x < pivot]) +
            [x for x in a if x == pivot] +
            quick_sort([x for x in a if x > pivot]))

# 6. Sort in descending order
def descending(a):
    return sorted(a, reverse=True)

# 7. Find kth smallest after sorting
def kth_smallest(a, k):
    s = sorted(a)
    return s[k-1] if 1 <= k <= len(s) else None

# 8. Sort words by length
def sort_by_length(words):
    return sorted(words, key=len)

# 9. Sort pairs by second value
def sort_pairs(pairs):
    return sorted(pairs, key=lambda x: x[1])

# 10. Check whether a list is sorted
def is_sorted(a):
    return all(a[i] <= a[i+1] for i in range(len(a)-1))

nums = [7, 2, 9, 1, 5, 3]
print("1. Bubble:", bubble_sort(nums))
print("2. Selection:", selection_sort(nums))
print("3. Insertion:", insertion_sort(nums))
print("4. Merge:", merge_sort(nums))
print("5. Quick:", quick_sort(nums))
print("6. Descending:", descending(nums))
print("7. 3rd smallest:", kth_smallest(nums, 3))
print("8. By length:", sort_by_length(["Python", "AI", "Programming"]))
print("9. Pairs:", sort_pairs([("A", 3), ("B", 1), ("C", 2)]))
print("10. Sorted:", is_sorted([1, 2, 3, 4]))
