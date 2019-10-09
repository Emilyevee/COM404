print ("How many bars should be charged?")
charge = int(input())
bars = 0
while bars < charge:
    print ("Charging")
    bars+=1
    print (" █" * (bars))

print ("the battery is fully charged")


    