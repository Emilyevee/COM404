print ("how many live cables must i avoid?")
cables = int(input())
live = 0
while live < cables:
    print("avoiding...")
    live+=1
    print ("...done!" + str(live ) + "live cables avoided")


print ("all live cables have been avoided")

