#Write a program to find the greatest common divisor (GCD) or highest common factor (HCF) of given two numbers.
num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
counter=1
while counter<=num1 and counter<=num2:
    if num1%counter==0 and num2%counter==0:
        gcd=counter
    counter+=1
print(gcd,"is the HCF/GCD of",num1 ,"and", num2)
