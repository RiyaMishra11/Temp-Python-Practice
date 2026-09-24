# 62 Lambda, Map, Filter, Reduce - 11 programs
from functools import reduce
nums=[1,2,3,4,5]
print("1 Squares:",list(map(lambda x:x*x,nums)))
print("2 Cubes:",list(map(lambda x:x**3,nums)))
print("3 Evens:",list(filter(lambda x:x%2==0,nums)))
vals=[-5,3,-1,7,0,9]
print("4 Positives:",list(filter(lambda x:x>0,vals)))
print("5 Sum:",reduce(lambda a,b:a+b,nums))
print("6 Product:",reduce(lambda a,b:a*b,nums,1))
print("7 Maximum:",reduce(lambda a,b:a if a>b else b,nums))
print("8 Uppercase:",list(map(str.upper,["alice","bob","charlie"])))
students=[("A",82),("B",95),("C",76)]
print("9 Sorted:",sorted(students,key=lambda x:x[1],reverse=True))
words=["cat","python","code","developer","AI"]
print("10 Long words:",list(filter(lambda x:len(x)>4,words)))
result=reduce(lambda a,b:a+b,map(lambda x:x*x,filter(lambda x:x%2==0,range(1,11))),0)
print("11 Even-square sum:",result)
