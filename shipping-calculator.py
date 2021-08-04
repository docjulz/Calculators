# Shipping Charges
# This program will calculate the shipping charges
# based on the weight of the package

# Established rates for shipping
RATE_1 = 1.5
RATE_2 = 3.0
RATE_3 = 4.0
RATE_4 = 4.75

# Get the number of pounds for the package
weight = float(input("What is the weight of the package? "))

# Determine the cost based on the weight and display the results.
# If the package weight is above 0.0 lbs.
if weight > 0:
    if weight < 2:
        shipping_rate= RATE_1
    elif weight <= 6:
        shipping_rate= RATE_2
    elif weight <= 10:
        shipping_rate= RATE_3
    else: 
        shipping_rate= RATE_4
    total = weight * shipping_rate

    print("The shipping rate for ", weight, " lbs. is: $", format(total, ',.2f'), sep='')

# If the package weight is entered incorrectly.    
else:
    print("INVALID: You must enter a positive number for package weight.")
    
    
   

        
