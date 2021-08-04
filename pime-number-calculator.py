# This program determines if a number is
# a Prime Number and then lists all
# Prime Numbers 1-100

# Main function
def main():
    # Ask for value
    value = int(input("Please enter a number to determine if it is " \
                    "a Prime Number: "))

    # Call is_prime function
    prime = is_prime(value)

    # Call all_prime function
    list = all_prime(prime)

# Determines if number is prime or not
def is_prime(num):
    if num%2 !=0 and num%3 !=0:
        print(num,"is a Prime Number")
    else:
        print(num,"is NOT a Prime Number")
    return num

# Gives all Prime Numbers 1-100
def all_prime(numbers):
    print("------------------------------------------")
    print("Here is a list of all Prime Numbers 1-100:")
    print("------------------------------------------")    
    for numbers in range(1,101):
        if numbers%2 !=0 and numbers%3 !=0:
            print(numbers,end=" ")

main()
