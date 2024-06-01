number = input("Enter a number: ")

if number > 0:
    print("The number is positive.")
elif number == 0:      # the correction is that instead of using "=" operator it should've been "=="
    print("The number is zero.")
else number < 0:
    print("The number is negative.")