# Mini Projects - 10 Programs
import random,string
# 1. Number guessing game
secret=42
while True:
    g=int(input("Guess 1-100: "))
    if g==secret: print("Correct"); break
    print("Too low" if g<secret else "Too high")
# 2. ATM
balance=5000
choice=input("ATM deposit/withdraw/balance: ").lower()
if choice=="deposit": balance+=float(input("Amount: "))
elif choice=="withdraw":
    amount=float(input("Amount: ")); balance=balance-amount if amount<=balance else balance
print("Balance:",balance)
# 3. Quiz
qs={"Capital of India?":"delhi","2+2?":"4","Python extension?":".py"}; score=0
for q,a in qs.items():
    if input(q+" ").lower().strip()==a:score+=1
print("Score:",score)
# 4. To-do list
tasks=[input("Task: ") for _ in range(3)]
for i,t in enumerate(tasks,1):print(i,t)
# 5. Contact book
contacts={}; name=input("Contact name: "); contacts[name]=input("Phone: "); print(contacts)
# 6. Expense tracker
expenses=[float(input("Expense amount: ")) for _ in range(3)]; print("Total:",sum(expenses))
# 7. Password generator
length=int(input("Password length: ")); chars=string.ascii_letters+string.digits+"!@#$"; print("Password:",''.join(random.choice(chars) for _ in range(length)))
# 8. Rock paper scissors
choices=["rock","paper","scissors"]; user=input("rock/paper/scissors: ").lower(); computer=random.choice(choices); print("Computer:",computer)
if user not in choices: print("Invalid")
elif user==computer: print("Draw")
elif (user,computer) in [("rock","scissors"),("paper","rock"),("scissors","paper")]: print("You win")
else: print("Computer wins")
# 9. Shopping cart
cart=[float(input("Item price: ")) for _ in range(3)]; print("Cart total:",sum(cart))
# 10. Student result
marks=list(map(float,input("Five marks: ").split()))
if len(marks)==5: print("Total:",sum(marks),"Percentage:",sum(marks)/5,"Result:","Pass" if min(marks)>=33 else "Fail")
else: print("Enter exactly five marks")
