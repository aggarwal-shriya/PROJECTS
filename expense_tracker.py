#Expense Tracker 
e=[]
m=[]
while True:
    print ("Hi")
    a= input ("Do u want to add ur expense ? yes or no")
    if (a.lower()!="yes"):
        break
    else :
        b= input ("enter the expense")
        c= int (input ("enter the amount"))
        e.append(b)
        m.append(c)
print (f"the items you spent money on is {e}")
print ("the total sum is", sum(m))
