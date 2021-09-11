# Ek algorithm banao jo user se 2 number input`` lega. 
# Aur fir unn number ko multiply karke print kare. 
# Jaise, agar input hai 5 aur 4 tab 20 print hona chahiye.

# Note:- Aap * yaani ki multiply operator ka numbers ko multiply karne ke liye use nhi kar sakte. 
# Aap aur kisi bhi operator (+, -) ka use kar sakte ho.


# 2*3=6
# means 2 is repeated 3 times.i.e.2+2+2=6
num1=int(input("Enter first value\n"))
num2=int(input("Enter second value\n"))
counter=1
sum=0
while counter<=num2:
    sum+=num1
    if counter==num2:
        print(sum,"Is the product of",num1,"and",num2)
    counter+=1
    








        