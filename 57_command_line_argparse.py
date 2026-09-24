# 65 Command Line and argparse - 11 programs
import argparse,sys
print("1 Raw arguments:",sys.argv)
parser=argparse.ArgumentParser(description="CLI practice")
parser.add_argument("--name",default="Guest")
parser.add_argument("--age",type=int,default=0)
parser.add_argument("--numbers",nargs="*",type=float,default=[])
parser.add_argument("--verbose",action="store_true")
parser.add_argument("--operation",choices=["sum","max","min"],default="sum")
args,unknown=parser.parse_known_args()
print("2 Name:",args.name)
print("3 Age:",args.age)
print("4 Numbers:",args.numbers)
print("5 Verbose:",args.verbose)
print("6 Operation:",args.operation)
print("7 Unknown:",unknown)
if args.numbers:
    result=sum(args.numbers) if args.operation=="sum" else max(args.numbers) if args.operation=="max" else min(args.numbers)
else: result=0
print("8 Result:",result)
print("9 Age valid:",args.age>=0)
def calculate(numbers,operation):
    if not numbers:return 0
    return sum(numbers) if operation=="sum" else max(numbers) if operation=="max" else min(numbers)
print("10 Function:",calculate([5,2,8],"max"))
print("11 CLI practice complete")
