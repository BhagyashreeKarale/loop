# Aisa code likho jisse 1 se 100 mein wahi numbers print ho jo 7 se divisible hai 
# yaani unka 7 se bhaag karne per remainder 0 bachta hai.
counter=1
while counter<=100:
    if counter%7==0:
        print(counter)
    counter+=1