num = int(input("Enter a Number:"))
order = len(str(num))
temp = num
sum = 0
while(temp>0):
    digit =temp%10#removing single digit
    sum = sum + (digit **order)
    temp = temp//10#reducing the number by removing digits one by one
if(sum==num):
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")
######################################################################################################
#practice
#using list and loop(for loop)
n=153
s=str(n)
sum=0
for i in s:
    sum=sum+(int(i)**3)
if sum==n:
    print("It's an armstrong number")
else:
    print("It isn't an armstrong number")


# using while loop
num=153
temp=num
sum=0
order=len(str(num))
while temp>0:
    digit=temp%10#note that we use temp 
    sum=sum+(digit**order)
    temp=temp//10
if sum==num:
    print("It is an Armstrong number")
else:
    print("It isn't an Armstrong number")



