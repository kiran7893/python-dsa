#Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

x=int(input("enter max number"))

odd_numbers =[]


for i in range(x):
    if(i%2==1):
        odd_numbers.append(i)
    else:
        continue

print(odd_numbers)    