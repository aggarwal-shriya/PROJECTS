x= str(input("i will cheer for u. Enter a word: "))
n= int(input ("Enter your enthusiams level (1-10): "))
vowel= "aeiouAEIOU"
for a in range (0,len(x)):
    if x[a] in (vowel):
        print ("Give me an "+ x[a] + "! " + x[a])
    else :
        print ("Give me a "+ x[a] + "! " + x[a])

print ("What does that spell?")
for _ in range (n):
    print (x)
