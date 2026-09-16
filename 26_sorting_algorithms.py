# Day 7 - 26: Sorting Algorithms

def bubble_sort(numbers):  # 1. Bubble sort
    a = numbers.copy()
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]: a[j], a[j+1] = a[j+1], a[j]
    return a

def selection_sort(numbers):  # 2. Selection sort
    a = numbers.copy()
    for i in range(len(a)):
        m = i
        for j in range(i+1, len(a)):
            if a[j] < a[m]: m = j
        a[i], a[m] = a[m], a[i]
    return a

def insertion_sort(numbers):  # 3. Insertion sort
    a = numbers.copy()
    for i in range(1, len(a)):
        key, j = a[i], i-1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]; j -= 1
        a[j+1] = key
    return a

def sort_names(names):  # 4. Alphabetical names
    return sorted(names, key=str.lower)

def descending(numbers):  # 5. Descending order
    return sorted(numbers, reverse=True)

def sort_by_absolute(numbers):  # 6. Sort by absolute value
    return sorted(numbers, key=abs)

def sort_students(students):  # 7. Sort students by marks
    return sorted(students, key=lambda x: x["marks"], reverse=True)

def unique_sorted(numbers):  # 8. Remove duplicates and sort
    return sorted(set(numbers))

def merge_sorted(a, b):  # 9. Merge sorted lists
    result=[]; i=j=0
    while i<len(a) and j<len(b):
        if a[i] <= b[j]: result.append(a[i]); i+=1
        else: result.append(b[j]); j+=1
    return result+a[i:]+b[j:]

def top_three(numbers):  # 10. Top three values
    return sorted(numbers, reverse=True)[:3]

if __name__ == "__main__":
    data=[64,25,12,22,11]
    print(bubble_sort(data))
    print(selection_sort(data))
    print(insertion_sort(data))
    print(sort_names(["Riya","aman","Karan"]))
    print(descending(data))
    print(sort_by_absolute([-5,2,-1,8,-3]))
    print(sort_students([{"name":"Aman","marks":82},{"name":"Riya","marks":95}]))
    print(unique_sorted([4,2,4,1,3,2]))
    print(merge_sorted([1,4,7],[2,3,8]))
    print(top_three([10,45,23,89,67,12]))
