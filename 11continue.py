# continue
# continue python ka ek keyword hai.
# continue statement se loop mein iterate ho rahe kuchh statement ko skip karake 
# agale statement ko execute karata hai.

# content
i = 1
while(i <= 10):
    if(i == 5):
        print("Skipped Element :", i)
        continue
    print(i)
# Output 1 2 3 4 Skipped Element: 5 6 7 8 9 10

counter = 0
string = "navgurukul"
while (counter < len(string)):
    counter += 1

    if string[counter] == "a":
        continue

    if string[counter] == "u":
        continue
    
    print(string[counter])

print("The end", string[counter])
