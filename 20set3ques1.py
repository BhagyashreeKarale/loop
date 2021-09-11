# Aisa code likho jisse 20 se 100 mein wahi numbers print ho jo 2 se divisible hai
# yaani numbers ka 2 se bhaag karne par remainder (shesh) 0 bachta hai.
counter=20
while counter<=100:
    if counter%2==0:
        print(counter)
    # elif counter%2!=0:
    #     continue
    counter+=1
    