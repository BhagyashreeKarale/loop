#Neeche diye huye codes mai kuch bugs hai. Ab aapko error find kar ke unhe solve karne hai.(number of bugs)

# i = 1
# while(i <= 140):
#     if(i % 3 == 0):
#     sum = sum + i
#     i = i - 1
# print(sum)


#errors
# after if python expects a condition or if we want nested we can put another if.anything but with indentation
# therefore it shows indentation error also 
# sum is not defined or initialized in the case of loop before incrementing it 
# another thing is we should mention the statement or the body of the loop before incrementing the initializers.
# inappropriate increment
# no else block therefore code stops when the if block evaluates false.pythin doesn't understand where to go next

#correct code
# i = 1
# sum=0
# while(i <= 140):
#     if(i % 3 == 0):
#         print(sum)
#         sum = sum + i
#         i = i + 1
#     else:
#         print(i)
#     sum = sum + i
#     i = i + 1
    


i = 1
sum=0
while(i <= 140):
    if(i % 3 == 0):
        print(sum)
    sum = sum + i
    i = i + 1
