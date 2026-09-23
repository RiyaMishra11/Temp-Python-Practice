# File 59: Bit Manipulation
# 11 practice programs

# 1 Odd/even
n=17
print("1.",bool(n&1))

# 2 Power of two
def power2(n): return n>0 and (n&(n-1))==0
print("2.",power2(32))

# 3 Count set bits
def bits(n):
    c=0
    while n:n&=n-1;c+=1
    return c
print("3.",bits(29))

# 4 Unique number
def unique(a):
    x=0
    for v in a:x^=v
    return x
print("4.",unique([4,1,2,1,2]))

# 5 Swap with XOR
a,b=10,20
a^=b;b^=a;a^=b
print("5.",a,b)

# 6 Get kth bit
print("6.",(13>>2)&1)

# 7 Set kth bit
print("7.",8|(1<<1))

# 8 Clear kth bit
print("8.",15&~(1<<1))

# 9 Toggle kth bit
print("9.",10^(1<<1))

# 10 Two unique numbers
def two_unique(a):
    x=0
    for v in a:x^=v
    mask=x&-x
    p=q=0
    for v in a:
        if v&mask:p^=v
        else:q^=v
    return p,q
print("10.",two_unique([1,2,1,3,2,5]))

# 11 Reverse 8 bits
def reverse8(n):
    r=0
    for _ in range(8):
        r=(r<<1)|(n&1);n>>=1
    return r
print("11.",reverse8(13))
