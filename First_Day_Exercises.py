def printOdd():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    z = int(input("Enter third number: "))

    oddX = -1
    oddY = -1
    oddZ = -1
    isOdd = False

    if x%2 != 0:
        oddX = x
        isOdd = True

    if y%2 != 0:
        oddY = y
        isOdd = True

    if z%2 != 0:
        oddZ = z
        isOdd = True

    if isOdd == False:
        print(min(x, y, z))
        return
    
    print(max(oddX, oddY, oddZ))

def printDayOfBirth(): # format dd/mm/yyyy
    dayOfBirth = input("Enter your day of birth: ")
    yearOfBirth = dayOfBirth[6:]  # Extract the year from the string input
    print("Your year of birth is:", yearOfBirth)

def printLargestOdd():
    largestOdd = -1
    for i in range(10):
        input_number = int(input(f"Enter a number {i+1}: "))
        if input_number % 2 != 0 and input_number > largestOdd:
            largestOdd = input_number
    if largestOdd != -1:
        print("The largest odd number is:", largestOdd)
    else:
        print("No odd numbers were entered.")

if __name__ == "__main__":
    printDayOfBirth()

