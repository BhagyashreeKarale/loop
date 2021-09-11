# Ek loop banao jo user se 10 numbers ko input le. Input lene ke baad unn saare numbers ka sum print kare.
# **Note: Iss program ka counter 50 se shuru hona chaiye. 
# Aur aise code likho ki counter mein subtract karke loop chale. 
# Dimaag mein yeh rakhiye ki hum humesha **
# Yeh program kuch aise chalega. Har baar input() ka use kar ke user se ek number input lega.
# Koi bhi number daaliye > 10
# Koi bhi number daaliye > 16
# Koi bhi number daaliye > 9
# Koi bhi number daaliye > 10
# Koi bhi number daaliye > 56
# Koi bhi number daaliye > 78
# Koi bhi number daaliye > 98
# Koi bhi number daaliye > 43
# Koi bhi number daaliye > 21
# Koi bhi number daaliye > 76
# Total Sum: 417
# Final line mein isne Total Sum: 417 print kara hai. 
# Yeh isiliye print kia hai kyunki 10+16+9+10+56+78+98+43+21+76 ka sum 417 hai.
counter=50
i=counter-50#=1
sum=0#sum should have 1 for adding
while i<10:#59 because 50 to 60 is 11(considering 50 because initialization is also included)
    user_input=int(input("Enter a value:\n"))#here we are adding inputs taken from user 
                                             #so no need of mentioning specific condition
                                             #such as if i==10
    sum+=user_input
    i+=1
print("The sum of the 10 values entered:",sum)
 
#another way without changing the initializer
i=50
sum=0
while i < 60:#here we cannot use = as then it will take 11 inputs.because from 50 t0 60 it is 11 numbers considering 60.    
    num=int(input("Enter any number:\n"))
    sum=sum+num
    i=i+1
print(sum,"is the sum of all the 10 values entered")



