# Code likho jisse 30 se 420 tak ke unn numbers ka sum calculate ho jo 8 ke multiple hai 
# yaani wo numbers 8 ke table (paahade) mein aate hai.
# counter=30
# sum=1
# while counter<=420:
#     # if counter==420:
#     if counter%8==0:
#         if counter==420:
#             print(sum)
#     sum+=counter
#     counter+=


sum = 0  # Making a variable sum to store the value of sum of all the integers divisible by 4 till n
i = 30  # To make the loop work we need a variable whose value gets increased every the code executes
while i <= 420:    # Initialising while loop which will execute till n
    if i%8 == 0 : # checking if the value in i divided by 4 gives remainder 0 or not
        sum +=i  # Adding the integers inside the variable sum
        i+=1  # Incrementing the value of i
    else:   # if the condition is not true else part will execute
        i+=1 #Incrementing the value of i
        continue # continue will take the pointer to the starting of while loop

print("Sum is : ",sum) # Printing the sum





