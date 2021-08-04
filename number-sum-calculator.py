# This program calculates the sum of a series of numbers

def main():

    # Get series of number input from user
    numbers = (input("Enter a series of numbers to calculate its sum: "))

    # Validate that user only includes whole numbers
    if numbers.isdigit():
        # Pass value to get_sum function
        sum = get_sum(numbers)
        print()
        print("You entered:",numbers)
        print("When you add each number you get a total of:", sum)

    # If user enters anything other than whole numbers,
    # display the following error message
    else:
        print("ERROR:", numbers, "must include ONLY whole numbers.")

# Get sum of series of numbers
def get_sum(num):

    # The total variable holds the sum of each number
    total = 0

    # Loop through each number in series
    for series in range(len(num)):

        # Separate each number into a list
        digits = num[series]

        # Convert string of numbers into integers
        sum_total = int(digits)

        # Calculate the total
        total += sum_total

    # Return the total back to main()
    return total

main()
