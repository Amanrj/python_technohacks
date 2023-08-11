
print("Select the operation you want to perform ")

print("1. ADDITION")

print("2. SUBTRACTION")

print("3. MULTIPLICATION")

print("4. DIVISION")

Num1=int(input("Enter First Value"))

Num2=int(input("Enter Second Value"))

operation=input("Enter The Operation")

if operation=="1":

    print("The number is" +str(int ( Num1+Num2)))

elif operation=="2":

    print("The number is" + str(int(Num1-Num2)))

elif operation=="3":

    print("The number is"+ str(int(Num1*Num2)))

elif operation=="4":

    print("The number is"+ str(int(Num1/Num2)))

else:

    print("Error")    
    
    
