#Convert Celcius to Fahrenheit
celcius = float(input("Enter temperature in Celcius: "))

#Formula with only one trailing decimal point
fahrenheit = format((9/5*celcius)+32,".1f")
print (celcius, "degrees Celcius equals", fahrenheit, "degrees Fahrenheit.")
