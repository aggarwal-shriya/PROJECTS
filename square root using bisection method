#finding quare root using bisection search
c= int (input ("\n enter a number to find its square root"))
l= 0
h= max (1,abs(c))
r= ((l+h)/2)
while (abs(r**2-abs(c))>=0.000001):
    if (r**2-abs(c)>0):
        h=r
    else:
        l=r
    r= (h+l)/2

if (c>=0):
    print (r)
else :
    print (-r)
