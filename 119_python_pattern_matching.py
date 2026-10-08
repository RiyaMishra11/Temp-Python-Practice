# 119 Structural Pattern Matching
# Python 3.10+

def number_type(x):
    match x:
        case 0: return "zero"
        case 1: return "one"
        case _: return "other"
print("1.",number_type(1))

def command(x):
    match x:
        case "start": return "Starting"
        case "stop": return "Stopping"
        case _: return "Unknown"
print("2.",command("start"))

def status(code):
    match code:
        case 200|201: return "Success"
        case 400|404: return "Client Error"
        case 500|502: return "Server Error"
        case _: return "Other"
print("3.",status(404))

def age_type(age):
    match age:
        case n if n<0: return "Invalid"
        case n if n<18: return "Minor"
        case n if n<60: return "Adult"
        case _: return "Senior"
print("4.",age_type(25))

def point_type(p):
    match p:
        case (0,0): return "Origin"
        case (0,y): return f"Y-axis {y}"
        case (x,0): return f"X-axis {x}"
        case (x,y): return f"Point {x},{y}"
print("5.",point_type((0,8)))

def list_type(values):
    match values:
        case []: return "Empty"
        case [x]: return f"One {x}"
        case [a,b]: return f"Two {a},{b}"
        case [first,*rest]: return f"First={first}, Rest={rest}"
print("6.",list_type([1,2,3,4]))

def user_role(user):
    match user:
        case {"role":"admin","name":name}: return f"Admin {name}"
        case {"role":"user","name":name}: return f"User {name}"
        case _: return "Unknown"
print("7.",user_role({"name":"Aman","role":"admin"}))

response={"status":"success","data":{"items":[1,2,3]}}
match response:
    case {"status":"success","data":{"items":items}}: result=sum(items)
    case _: result=0
print("8.",result)

class User:
    def __init__(self,name,age): self.name=name; self.age=age
def describe(u):
    match u:
        case User(name=name,age=age) if age>=18: return f"{name} adult"
        case User(name=name,age=age): return f"{name} minor"
        case _: return "Not User"
print("9.",describe(User("Riya",21)))

def route(cmd):
    match cmd:
        case ["add",value]: return f"Adding {value}"
        case ["delete",value]: return f"Deleting {value}"
        case ["show"]: return "Showing"
        case _: return "Invalid"
print("10.",route(["add","Python"]))

events=[{"type":"login","user":"Aman"},{"type":"purchase","amount":500},{"type":"logout","user":"Aman"}]
def process(e):
    match e:
        case {"type":"login","user":u}: return f"{u} logged in"
        case {"type":"purchase","amount":a}: return f"Purchase {a}"
        case {"type":"logout","user":u}: return f"{u} logged out"
        case _: return "Unknown"
print("11.",[process(e) for e in events])
