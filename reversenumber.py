user_input=(input("Enter a number:\n"))   
n=int(user_input)
counter=1
count=len((user_input))
rev = 0
while(counter <= count):
    a = n % 10#to remove single digit
    rev = rev * 10 + a
    print(rev,end="")
    rev=rev*0#no need
    n = n // 10#to reduce the number=reducing original number by removing the removed digit 
    counter+=1



