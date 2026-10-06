# 110 JSON & API Data Processing
import json
from urllib.parse import urlencode

# 1 Convert dict to JSON
user={"name":"Aman","age":22,"skills":["Python","Git"]}
print("1",json.dumps(user))

# 2 Pretty JSON
print("2\n",json.dumps(user,indent=2))

# 3 JSON to dict
data=json.loads('{"name":"Riya","age":21}')
print("3",data["name"],data["age"])

# 4 Save JSON
file="/mnt/data/sample_users_110.json"
with open(file,"w",encoding="utf-8") as f: json.dump([user,data],f,indent=2)
print("4",file)

# 5 Load JSON
with open(file,encoding="utf-8") as f: print("5",json.load(f))

# 6 Extract nested data
response={"status":"success","data":{"users":[{"id":1,"name":"Aman"},{"id":2,"name":"Riya"}]}}
print("6",[x["name"] for x in response["data"]["users"]])

# 7 Filter records
records=[{"name":"Aman","age":22},{"name":"Riya","age":17},{"name":"Rahul","age":25}]
print("7",[x for x in records if x["age"]>=18])

# 8 Sort records
products=[{"name":"Mouse","price":500},{"name":"Laptop","price":55000},{"name":"Keyboard","price":1500}]
print("8",sorted(products,key=lambda x:x["price"]))

# 9 Missing fields
print("9",{"name":"Neha"}.get("email","Not available"))

# 10 Query parameters
print("10",urlencode({"search":"python","page":2,"limit":10}))

# 11 Response analyzer
def analyze(r):
    users=r.get("data",{}).get("users",[])
    return {"status":r.get("status","unknown"),"count":len(users),"names":[u.get("name","Unknown") for u in users]}
print("11",analyze(response))
