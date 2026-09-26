"""Day 17 - File 73: Mini Project - Inventory Management | 11 Programs"""

def program_1():
    inventory={
        "Laptop":{"price":65000,"quantity":5},
        "Mouse":{"price":1200,"quantity":20},
        "Keyboard":{"price":2500,"quantity":10}
    }
    print(inventory)

def program_2():
    inventory={}
    inventory["Monitor"]={"price":15000,"quantity":8}
    print(inventory)

def program_3():
    inventory={"Mouse":{"price":1200,"quantity":20}}
    inventory["Mouse"]["quantity"]+=10
    print(inventory)

def program_4():
    inventory={"Laptop":{"price":65000,"quantity":5}}
    sold=2
    if inventory["Laptop"]["quantity"]>=sold:
        inventory["Laptop"]["quantity"]-=sold
        print("Sale completed")
    else:
        print("Insufficient stock")
    print(inventory)

def program_5():
    inventory={
        "Laptop":{"price":65000,"quantity":5},
        "Mouse":{"price":1200,"quantity":20},
        "Keyboard":{"price":2500,"quantity":10}
    }
    total=sum(x["price"]*x["quantity"] for x in inventory.values())
    print("Inventory value:",total)

def program_6():
    inventory={
        "Laptop":{"price":65000,"quantity":5},
        "Mouse":{"price":1200,"quantity":2},
        "Keyboard":{"price":2500,"quantity":10}
    }
    print([name for name,x in inventory.items() if x["quantity"]<=5])

def program_7():
    inventory={
        "Laptop":{"price":65000,"quantity":5},
        "Mouse":{"price":1200,"quantity":20},
        "Monitor":{"price":18000,"quantity":7}
    }
    print(max(inventory.items(),key=lambda x:x[1]["price"]))

def program_8():
    inventory={
        "Laptop":{"price":65000,"quantity":5},
        "Mouse":{"price":1200,"quantity":20},
        "Keyboard":{"price":2500,"quantity":10}
    }
    query="mouse"
    print([(name,data) for name,data in inventory.items() if query.lower() in name.lower()])

def program_9():
    inventory={
        "Laptop":{"price":65000,"quantity":5},
        "Mouse":{"price":1200,"quantity":20},
        "Keyboard":{"price":2500,"quantity":10}
    }
    print(sorted(inventory.items(),key=lambda x:x[1]["quantity"],reverse=True))

def program_10():
    inventory={
        "Laptop":{"price":65000,"quantity":5},
        "Mouse":{"price":1200,"quantity":20},
        "Keyboard":{"price":2500,"quantity":10}
    }
    print("===== STOCK REPORT =====")
    for name,item in inventory.items():
        value=item["price"]*item["quantity"]
        print(f"{name}: price={item['price']}, qty={item['quantity']}, value={value}")

def program_11():
    inventory={
        "Laptop":{"price":65000,"quantity":5},
        "Mouse":{"price":1200,"quantity":20},
        "Keyboard":{"price":2500,"quantity":10},
        "Monitor":{"price":18000,"quantity":3}
    }
    inventory["Monitor"]["quantity"]+=5
    inventory["Mouse"]["quantity"]-=4
    total=sum(x["price"]*x["quantity"] for x in inventory.values())
    low=[name for name,x in inventory.items() if x["quantity"]<=5]
    highest=max(inventory.items(),key=lambda x:x[1]["price"]*x[1]["quantity"])
    print("===== INVENTORY REPORT =====")
    print("Products:",len(inventory))
    print("Total value:",total)
    print("Low stock:",low)
    print("Highest stock value:",highest)

if __name__ == "__main__":
    program_11()
