number1 = int(input ("please enter the first number"))
number2 = int(input ("please enter the second number"))
number3 = int(input ("please enter the third number"))
evenCount = 0 
oddCount = 0

if number1 % 2 == 0:
    evenCount+=1
else:
    oddCount+=1
if number2 % 2 == 0:
    evenCount+=1
else:
    oddCount+=1
if number3 % 2 == 0:
    evenCount+=1
else:
    oddCount+=1
print ("there were "+ str(evenCount)+" even and"+ str(oddCount)+ " odd")

