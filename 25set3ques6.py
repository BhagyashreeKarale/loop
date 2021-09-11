# Iss pattern ko print karne ke liye code likho:

# 1, -2, 3, -4, 5, -6 ..99, -100
counter=1
while counter<=100:
    if counter%2!=0:
        print(counter)
    else:
        print(counter*-1)
    counter+=1