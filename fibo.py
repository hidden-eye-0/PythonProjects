a=int(input("Enter any number:"))
b=-1
c=1
for i in range(0,a):
    d=b+c
    print("{}".format(d))
    b=c
    c=d
