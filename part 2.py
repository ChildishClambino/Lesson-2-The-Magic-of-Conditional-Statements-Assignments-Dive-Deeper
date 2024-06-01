num1 = int(input("pick a number "))       #prompt user for numbers
num2 = int(input("pick another number "))
num3 = int(input("pick one last number "))

print("the greatest number is ",max(num1,num2,num3))  #picking the max and min
print("the smallest number is ",min(num1,num2,num3))

if num1 == num2 and num1 == num3:                      #using if and elif in order to identify how many inputs are equal to eachother
    print("there are 3 numbers equal to eachother")
elif num1 == num2 or num1 == num3 or num2 == num3:
    print("there are 2 numbers equal to eachother")    