# factorial
num = int(input("Enter any number:"))
fact = 1
for i in range(1, num+1):
    fact = fact * i
print("The factorial is {}".format(fact))



# sum of the series
num = int(input("Enter any number:"))
sum = 0
for i in range(1, num+1):
    a = (i**i)/i
    sum = sum + a
print("The sum of the series is {}".format(sum))



# odd or even
def oddeven(a):
    if(a%2==0):
        return "Even"
    else:
        return "Odd"
num = int(input("Enter a number:"))
print("The number is {}".format(oddeven(num)))



# reverse
str = input("Enter a string:")
print(str[::-1])



#remove odd numbers
num_list = list(range(1, 11))
for i in num_list:
    if (i%2==1):
        num_list.remove(i)
print("The list after removing odd numbers is {}".format(num_list))



#set ops
odd_set = set(range(1, 20, 2))
prime_set = set()
for i in range(2, 20):
    j = 2
    prime = True
    while j<i:
        if(i%j==0):
            prime = False
        j+=1
    if (prime == True):
        prime_set.add(i)
print("Odd set values    :", odd_set)
print("Prime set values :", prime_set)
print("Union:", odd_set|prime_set)
print("Intersection:", odd_set&prime_set)
print("Difference: ", odd_set-prime_set)
print("Symmetric Difference:", odd_set^prime_set)