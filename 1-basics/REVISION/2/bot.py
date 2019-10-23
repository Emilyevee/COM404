health = 100
print ("your health is " + str(health) + "%. Escape in progress...")

for count in range (0,5,1):
    print ("...oh dear, who is that?")
    name = input ()
    if name == ("smilers bot"):
        health -=20
        print ("time to jam out of here")
    elif name == ("hacker"):
        health +=20
        print ("yay! better follow this one!")
    else:
        print ("phew, jusy another emoji!")

print ("escaped! health is " + str(health) + "%")
