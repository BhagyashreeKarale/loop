# 11 logon ka weight input le aur fir average weight print kare. 
# Aur fir yeh bhi check kare ki kya Average weight 5 ka multiple(Yaani 5 se bhaag karne par shesh 0 bachta)hai ya nahi?
# Note: Isme aapko input ka use karna padega. Aap loop ke andar raw input ka use kar ke 11 baar raw_input le sakte ho.
counter=1
sum=0
while counter <= 11:
    user_input=int(input("enter your weight"))
    sum+=user_input#this increment should be mentioned before
    if counter==11:
        avg=(sum/11)
        if avg%5==0:
            print(avg,"is average weight")
            print("it is divisible by 5")
            # counter+=1
            sum+=user_input
            
        else:
            print(avg,"is average weight")
            print("it isn't divisible by 5")
            # counter+=1
            sum+=user_input
            
    counter+=1#this is the counter increment.so should be mentioned at last.
    
        