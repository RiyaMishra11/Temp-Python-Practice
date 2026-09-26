"""Day 17 - File 71: Advanced Sorting and Searching | 11 Programs"""
import bisect
from functools import cmp_to_key

def program_1():
    data = [("Aman",82),("Riya",95),("Kabir",88)]
    print(sorted(data, key=lambda x:x[1], reverse=True))

def program_2():
    words = ["python","ai","programming","code"]
    print(sorted(words, key=len))

def program_3():
    students = [("Aman","IT",85),("Riya","HR",92),("Kabir","IT",91),("Neha","HR",88)]
    print(sorted(students, key=lambda x:(x[1], -x[2])))

def program_4():
    numbers = [10,20,30,40,50]
    target = 30
    i = bisect.bisect_left(numbers, target)
    print("Found:", i < len(numbers) and numbers[i] == target)

def program_5():
    numbers = [10,20,40,50]
    print("Insert position:", bisect.bisect_left(numbers,30))

def program_6():
    numbers = [1,2,2,2,3,4]
    print("Count of 2:", bisect.bisect_right(numbers,2)-bisect.bisect_left(numbers,2))

def program_7():
    a,b = [1,4,7],[2,3,8]
    result=[]; i=j=0
    while i<len(a) and j<len(b):
        if a[i] <= b[j]:
            result.append(a[i]); i+=1
        else:
            result.append(b[j]); j+=1
    result.extend(a[i:]); result.extend(b[j:])
    print(result)

def program_8():
    def compare(a,b):
        if len(a)!=len(b):
            return len(a)-len(b)
        return (a>b)-(a<b)
    words=["banana","cat","apple","dog","kiwi"]
    print(sorted(words,key=cmp_to_key(compare)))

def program_9():
    numbers=[7,2,9,1,5,3]
    k=3
    print("Kth smallest:", sorted(numbers)[k-1])

def program_10():
    numbers=[12,5,8,20,15,3]
    print("Top 3:", sorted(numbers,reverse=True)[:3])

def program_11():
    numbers=[4,5,6,7,0,1,2]
    target=0
    left,right=0,len(numbers)-1
    while left<=right:
        mid=(left+right)//2
        if numbers[mid]==target:
            print("Found at:",mid)
            break
        if numbers[left] <= numbers[mid]:
            if numbers[left] <= target < numbers[mid]:
                right=mid-1
            else:
                left=mid+1
        else:
            if numbers[mid] < target <= numbers[right]:
                left=mid+1
            else:
                right=mid-1
    else:
        print("Not found")

if __name__ == "__main__":
    program_1()
