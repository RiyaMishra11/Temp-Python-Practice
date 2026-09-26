"""Day 16 - File 69: Mini Project - Expense Tracker | 11 Programs"""
from datetime import date

def program_1():
    expenses=[]
    expenses.append({"title":"Lunch","amount":250,"category":"Food"})
    print(expenses)

def program_2():
    expenses=[{"amount":250},{"amount":400},{"amount":300}]
    print("Total:",sum(x["amount"] for x in expenses))

def program_3():
    expenses=[{"title":"Lunch","amount":250,"category":"Food"},{"title":"Taxi","amount":400,"category":"Travel"},{"title":"Dinner","amount":500,"category":"Food"}]
    print([x for x in expenses if x["category"]=="Food"])

def program_4():
    expenses=[{"amount":250,"category":"Food"},{"amount":400,"category":"Travel"},{"amount":500,"category":"Food"},{"amount":200,"category":"Travel"}]
    totals={}
    for x in expenses: totals[x["category"]]=totals.get(x["category"],0)+x["amount"]
    print(totals)

def program_5():
    expenses=[{"title":"Phone","amount":900},{"title":"Groceries","amount":1800},{"title":"Coffee","amount":180}]
    print(max(expenses,key=lambda x:x["amount"]))

def program_6():
    expenses=[{"date":"2026-09-25","amount":200},{"date":"2026-09-25","amount":350},{"date":"2026-09-26","amount":500}]
    d="2026-09-25"
    print(d,"total:",sum(x["amount"] for x in expenses if x["date"]==d))

def program_7():
    expenses=[1200,900,1500,800]; budget=5000
    total=sum(expenses)
    print("Spent:",total,"Remaining:",budget-total,"Exceeded:",total>budget)

def program_8():
    print({"title":"Coffee","amount":150,"date":date.today().isoformat()})

def program_9():
    expenses=[{"title":"Food","amount":500},{"title":"Travel","amount":1200},{"title":"Books","amount":800}]
    print(sorted(expenses,key=lambda x:x["amount"],reverse=True))

def program_10():
    expenses=[{"title":"Amazon Books","amount":800},{"title":"Amazon Electronics","amount":2200},{"title":"Local Grocery","amount":600}]
    q="amazon"
    print([x for x in expenses if q.lower() in x["title"].lower()])

def program_11():
    expenses=[
        {"title":"Lunch","amount":250,"category":"Food"},
        {"title":"Bus","amount":80,"category":"Travel"},
        {"title":"Dinner","amount":450,"category":"Food"},
        {"title":"Movie","amount":600,"category":"Entertainment"},
        {"title":"Metro","amount":120,"category":"Travel"}]
    total=sum(x["amount"] for x in expenses)
    groups={}
    for x in expenses: groups[x["category"]]=groups.get(x["category"],0)+x["amount"]
    print("===== EXPENSE REPORT =====")
    print("Count:",len(expenses),"Total:",total,"Average:",round(total/len(expenses),2))
    print("Largest:",max(expenses,key=lambda x:x["amount"]))
    print("Category totals:",groups)

if __name__ == "__main__":
    program_11()
