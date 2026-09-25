"""Day 16 - File 66: CSV Data Analysis | 11 Programs"""
import csv
from io import StringIO

def program_1():
    text = "name,age,city\nAman,22,Delhi\nRiya,24,Mumbai\nKabir,21,Pune"
    for row in csv.DictReader(StringIO(text)):
        print(row)

def program_2():
    rows = [{"age": "22"}, {"age": "24"}, {"age": "21"}]
    print("Average age:", sum(int(r["age"]) for r in rows) / len(rows))

def program_3():
    rows = [{"name":"Aman","city":"Delhi"},{"name":"Riya","city":"Mumbai"},{"name":"Kabir","city":"Delhi"}]
    print([r for r in rows if r["city"] == "Delhi"])

def program_4():
    rows = [{"name":"Aman","salary":45000},{"name":"Riya","salary":62000},{"name":"Kabir","salary":51000}]
    print(max(rows, key=lambda r: r["salary"]))

def program_5():
    rows = [{"name":"Aman","marks":78},{"name":"Riya","marks":91},{"name":"Kabir","marks":85}]
    print(sorted(rows, key=lambda r: r["marks"], reverse=True))

def program_6():
    rows = [{"name":"Aman","department":"IT"},{"name":"Riya","department":"HR"},{"name":"Kabir","department":"IT"}]
    groups = {}
    for r in rows:
        groups.setdefault(r["department"], []).append(r["name"])
    print(groups)

def program_7():
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["name","score"])
    writer.writerow(["Aman",88])
    writer.writerow(["Riya",94])
    print(output.getvalue())

def program_8():
    text = "product,price\nLaptop,65000\nMouse,1200\nKeyboard,2500"
    print(list(csv.DictReader(StringIO(text))))

def program_9():
    sales = [{"quantity":2,"price":65000},{"quantity":5,"price":1200},{"quantity":3,"price":2500}]
    print("Total sales:", sum(r["quantity"] * r["price"] for r in sales))

def program_10():
    ids = [101,102,103,101,104,102,105]
    seen, dup = set(), set()
    for x in ids:
        if x in seen: dup.add(x)
        seen.add(x)
    print("Duplicates:", sorted(dup))

def program_11():
    rows = [{"name":"Aman","marks":82},{"name":"Riya","marks":95},{"name":"Kabir","marks":74},{"name":"Neha","marks":88}]
    print("Students:", len(rows))
    print("Average:", sum(r["marks"] for r in rows) / len(rows))
    print("Topper:", max(rows, key=lambda r:r["marks"]))

if __name__ == "__main__":
    program_1()
