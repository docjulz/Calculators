# This program uses the class Car to identify
# the make and year of car and also display
# its speed at 5 different intervals.


class Car:

    # the __init__ attribute establishes
    # the private methods __year_model and __make.
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    # Use the accelerate method to add speed.
    def accelerate(self):
        self.__speed += 5

    # Use the brake method to reduce speed.
    def brake(self):
        self.__speed -= 5

    # The get_speed method returns the current speed at
    # each interval.
    def get_speed(self):
        return self.__speed

    # The __str_ method identifies the car's final speed.   
    def __str__(self):
        return self.__speed

# Start the main function.
def main():

    # get the car's description.
    year = int(input("Enter model year: "))
    style = input("Enter the style of car: ")

    # Import the class Car() 
    car = Car(year, style)

    # Display the car's description.
    print("*****************")
    print("Here is the car data you entered:")
    print("Make: ", style)
    print("Year: ", year)
    print("*****************")

    # set the initial speed at 0 mph.
    speed = 0

    # Identify car's acceleration at specified points . 
    for count in range(5):
        car.accelerate()
        print("You are accelerating to", car.get_speed(),"mph.")

    # Identify car's braking at specified points.  
    for count in range(5):
        car.brake()

        # Validation loop to ensure car is not traveling negative mph
        if car.get_speed() >= 0:
            print("You are braking and now going", car.get_speed(),"mph.")
        else:
            print("Your Car is not able to go negative mph")

    print()

    # Validation loop displaying error if traveling negative mph
    if car.get_speed() >= 0:
        print("Your current speed is:",car.get_speed(),"mph.")
    else:
        print("Your car cannot go any slower")
    
# Call the main function.
main()
