# making a simple calculator with operations between 2 numbers
o= input ("select the operator : +,-,/,*")
a= int (input ("enter first number"))
b= int (input ("enter second number"))

if (o=="+"):
    print (a+b)
elif (o=="-"):
    print (a-b)
elif (o=="/"):
    if (b!=0):
        print (a/b)
    else :
        print ("division is not possible")
elif (o=="*"):
    print (a*b)
else :
    print (f"{o} is invalid")
