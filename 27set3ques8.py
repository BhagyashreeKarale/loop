# Ab hum pichli wali game ko thoda change karenge. 
# Humne sirf yeh check kara the ki kya user ne jo number input kiya hai wo humare number ke barabar hai ya nahi.

# Ab hum user ko yeh bhi batayenge ki jo usne number guess kiya hai, woh humare number se chota hai ya bada hai.

# Jaise, agar user ne 4 input kiya. 
# Hum check karenge ki kya 4 5 se chota hai? Haan 4 5 se chota hai. 
# Hum print karenge ki "aapka number chota hai! Ek aur baar try karo".

# Phir hum user se ek baar aur number input lenge. 
# Socho iss baar user ne 7 daala. Ab hum check karenge ki kya 7 5 se chota hai. 
# Iska jawab nahi hoga. Ab hum print karenge ki "aapka number bada hai! Ek aur baar try karo".

# Ab socho user ne 5 input kar diya. 
# Yeh number humare number ke barabar ho jayega. 
# Ab hum print karenge ki " waah! Aapne number guess kar liya".

# Hum aisa tab tak karte rahenge jab tak user humara number guess nahi kar leta. 
# Ya uski chances (jo ki 10 hain) khatam nahi ho jaati.

# User ko aise hint denge toh user ke liye guess karna asaaan ho jayega.

num=5
counter=1
print("<<<<<<<<<<<<<<<You only have 5 chances>>>>>>>>>>>>>>")
while counter<=10:
    guess=int(input("guess the number"))
    if guess==num and counter<5:
        print("your won!")
        break#if break isn't applied it will ask to guess again even after correct guess
    elif counter==10 and guess!=num:
        print("Sorry you ran out of chances\nBetter luck next time:)")
    elif counter==10 and guess==num:
        print("Correct guess at last chance.\nYou won!")
    elif counter<10 and guess<num:
        print("Your guess is smaller than the actual number.\nTry again!")
    elif counter<10 and guess>num:
        print("Your guess is larger than the actual number.\nTry again!")
    counter+=1