# Tuition calculator
# This program calculates the tuition increase
# over a period of years

TUITION = 8000      # Current tuition rate
PERCENT = 0.03      # Percentage increase each year
DURATION_START = 1  # First year of increase
DURATION_END = 5    # Final year of increase

# Table header
print("Rate of tuition increase over", DURATION_END, "years:")
print()
print("Year\tTuition")
print("-----------------")

# Loop through year
for year in range(DURATION_START, DURATION_END+1):
    # Reassign constant to account for tuition increase over each year
    TUITION += TUITION * PERCENT      
    print(year, '\t', "$", format(TUITION, ',.2f'), sep='')
print()
