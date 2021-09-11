# Ab hum loops ka use karke ek game banayenge. 
# Iss game ko hum "guessing game" bolte hai.

# Iss game mein humare pass pehle se ek number hota hai. 
# Abhi ke liye maan lo yeh number 5 hai.

# Uske baad hum user se 1 se 10 ke beech mein ek number input lete hai. 
# Phir user humare number ko guess karni ki koshish karta hai.

# Jaise, agar user ne 3 input kiya. 
# Hum check karenge ki kya 3, 5 ke barabar hai?

# 3, 5 ke barabar nahi hai isliye hum user se phir koi number input lenge.

# Aur check karenge ki kya woh number 5 ke barabar hai?

# User ko 5 chances milenge number guess karne ke liye.

# Agar usne 5 chances mein number guess kar liya toh sahi hai, nahi toh ek message aa jayega ki user ne guess nahi kiya.

# Hint: Python mein ek break statement hoti hai. Iske baare mein Google kar ke padh lo.
num=5
counter=1
print("<<<<<<<<<<<<<<<You only have 5 chances>>>>>>>>>>>>>>")
while counter<=5:
    guess=int(input("guesss a number between 1-10"))
    if guess==num and counter<5:
        print("your won!")
        break#if break isn't applied it will ask to guess again even after correct guess
    elif counter==5 and guess!=num:
        print("Sorry you ran out of chances\nBetter luck next time:)")
    elif counter==5 and guess==num:
        print("Correct guess at last chance")
    else:
        print("wrong guess try again")
    counter+=1
    