a=int(input("Enter any number:"))
c=0
d=a
while a!=0:
    b=a%10
    c=c+(b**3)
    a=a//10
if d==c:
    print("{} is an armstrong number".format(d))
else:
    print("{} is not an armstrong number".format(d))


