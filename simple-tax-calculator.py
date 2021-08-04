#SALES TAX CALCULATOR

#This program will calculate sales
#tax and produce the total sale amount

#Enter Tax constants
STATE_TAX = 0.05
COUNTY_TAX = 0.025

#Ask for cost before tax
purchase = float(input("Enter the amount of your purchase before tax: "))

#Calculate tax and total cost
state = purchase * STATE_TAX
county = purchase * COUNTY_TAX
total = purchase + state + county

#Print results
print("Your subtotal is: $", format(purchase, ',.2f'), sep='')
print("State sales tax: $", format(state, ',.2f'), sep='')
print("County sales tax: $", format(county, ',.2f'), sep='')
print("Total cost: $", format(total, ',.2f'), sep='')

