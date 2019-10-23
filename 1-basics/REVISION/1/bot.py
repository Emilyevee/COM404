print ("by what name are you known?")
name = input()
print ("live long and prosper " + name)

#question 2
print ("where is forky?")
location =input ()
if location == ("with bonnie"):
    print ("phew! bonnie will be happy")

elif location == ("running away"):
    print ("Oh no! bonnie will be upset!")

else: 
    print ("Ah! i better look for him")

#question 3 
print ("how many miles must i travel before i reach the secret base?")
miles = int(input())
print ("i will count the miles...")
while miles > 0:
    print ("i have " + str(miles) + "miles to go before i reach the base.")
    miles -=1
print ("i have arrived at the secret headquarters of the MIB!")
print ("It is time to sneak in")


#question 4
def item_from_suitcase(item):
    if item == ("toothbrush"):
        print ("A toothbrush. Well, got to have clean teeth!")
    elif item == ("spidey suit"):
        print ("My spidey suit! i wont be needing this. I am on holiday")
    else: 
        print ("An unecpected item! It could be useful")


item_from_suitcase("toothbrush")
item_from_suitcase("belt")
item_from_suitcase("spidey suit")

print ("i wonder what is in my suitcase...")