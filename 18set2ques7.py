# Prime numbers woh numbers hote hai jo sirf 1 aur apne aap se divisible hote hain. 
# Jaise 13 prime hai kyunki 13 sirf 13 aur 1 se perfectly divide hota hai. 
# Aur kisi bhi number se perfectly divide nahi hota.
# 4 prime nahi hai kyunki 4 apne aap se aur 2 aur 1 se perfectly divide hota hai.
# Prime number ke liye aapko check karna hoga ki woh number kaun kaun se numbers se divisible hai. 
# Yeh loop chala ke kar sakte ho.
#(FOR LOOP QUESTION)
counter=1
while counter<=100:
    user_input=int(input("enter a value"))
    if user_input%2!=0:
        print("It's a prime number")
    else:
        print("It's a composite number")
counter+=1
    