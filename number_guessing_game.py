import random
randNumber = random.randint(1, 100)
userinput=None
guesses=0
while userinput != randNumber:
    userinput= int(input("enter your guess here : "))
    guesses+=1
    if userinput== randNumber :
        print ("this is the right guess!!")
        
    elif userinput>randNumber:
        print ("this is the wrong guess try lower number !!")
    elif userinput<randNumber:
        print ("this is the wrong guess try higer number !!")

print (userinput)
print(f"you have guesed right answer after {guesses} trials")
