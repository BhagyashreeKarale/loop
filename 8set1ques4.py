# Ek loop banao jo user se 10 numbers ko input le. 
# Input lene ke baad unn saare numbers ka sum print kare.

# Yeh program kuch aise chalega. 
# Har baar input() ka use kar ke user se ek number input lega.
# Step 1 of 10 :- Koi bhi number daaliye > 10
# Step 2 of 10 :- Koi bhi number daaliye > 16
# Step 3 of 10 :- Koi bhi number daaliye > 9
# Step 4 of 10 :- Koi bhi number daaliye > 10
# Step 5 of 10 :- Koi bhi number daaliye > 56
# Step 6 of 10 :- Koi bhi number daaliye > 78
# Step 7 of 10 :- Koi bhi number daaliye > 98
# Step 8 of 10 :- Koi bhi number daaliye > 43
# Step 9 of 10 :- Koi bhi number daaliye > 21
# Step 10 of 10 :- Koi bhi number daaliye > 76

# Total Sum: 417
# Final line mein isne Total Sum: 417 print kara hai. 
# Yeh isiliye print kia hai kyunki 10+16+9+10+56+78+98+43+21+76 ka sum 417 hai.
counter=1
sum=0
while counter<=10:
    user_input=int(input("please enter a value"))
    sum+=user_input#it's position is very important
    if counter==10:
        print("total sum of the 10 values entered is",sum)
    counter+=1
    #we have to add the values,her the value isn't i,it is the input from the value.
    #therefore instead of i we mention the variable storing user input for producing the sum
   



