print ("please enter a number")
num = int(input())
total = num
count = num-1
while count > 0:
    total = total*count
    count-=1

print ("The factorial is " +str(total))
