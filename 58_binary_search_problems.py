# File 58: Binary Search Problems
# 11 practice programs

def search(a,t):
    l,r=0,len(a)-1
    while l<=r:
        m=(l+r)//2
        if a[m]==t:return m
        if a[m]<t:l=m+1
        else:r=m-1
    return -1

# 1 Basic binary search
print("1.",search([1,3,5,7,9],7))

# 2 First occurrence
def first(a,t):
    l,r,ans=0,len(a)-1,-1
    while l<=r:
        m=(l+r)//2
        if a[m]==t:ans=m;r=m-1
        elif a[m]<t:l=m+1
        else:r=m-1
    return ans
print("2.",first([1,2,2,2,5],2))

# 3 Last occurrence
def last(a,t):
    l,r,ans=0,len(a)-1,-1
    while l<=r:
        m=(l+r)//2
        if a[m]==t:ans=m;l=m+1
        elif a[m]<t:l=m+1
        else:r=m-1
    return ans
print("3.",last([1,2,2,2,5],2))

# 4 Count occurrences
a=[1,2,2,2,5]
print("4.",last(a,2)-first(a,2)+1)

# 5 Search insert position
def insert_pos(a,t):
    l,r=0,len(a)
    while l<r:
        m=(l+r)//2
        if a[m]<t:l=m+1
        else:r=m
    return l
print("5.",insert_pos([1,3,5,6],4))

# 6 Integer square root
def isqrt(n):
    l,r,ans=0,n,0
    while l<=r:
        m=(l+r)//2
        if m*m<=n:ans=m;l=m+1
        else:r=m-1
    return ans
print("6.",isqrt(50))

# 7 Peak element
def peak(a):
    l,r=0,len(a)-1
    while l<r:
        m=(l+r)//2
        if a[m]<a[m+1]:l=m+1
        else:r=m
    return l
print("7.",peak([1,3,7,5,2]))

# 8 Rotated array search
def rotated(a,t):
    l,r=0,len(a)-1
    while l<=r:
        m=(l+r)//2
        if a[m]==t:return m
        if a[l]<=a[m]:
            if a[l]<=t<a[m]:r=m-1
            else:l=m+1
        else:
            if a[m]<t<=a[r]:l=m+1
            else:r=m-1
    return -1
print("8.",rotated([4,5,6,7,0,1,2],0))

# 9 Minimum in rotated array
def rot_min(a):
    l,r=0,len(a)-1
    while l<r:
        m=(l+r)//2
        if a[m]>a[r]:l=m+1
        else:r=m
    return a[l]
print("9.",rot_min([4,5,6,1,2,3]))

# 10 Floor value
def floor_val(a,t):
    l,r,ans=0,len(a)-1,None
    while l<=r:
        m=(l+r)//2
        if a[m]<=t:ans=a[m];l=m+1
        else:r=m-1
    return ans
print("10.",floor_val([2,4,6,8],7))

# 11 Minimum shipping capacity
def capacity(w,days):
    l,r=max(w),sum(w)
    while l<r:
        cap=(l+r)//2
        d=1;cur=0
        for x in w:
            if cur+x>cap:d+=1;cur=0
            cur+=x
        if d<=days:r=cap
        else:l=cap+1
    return l
print("11.",capacity([1,2,3,1,1],4))
