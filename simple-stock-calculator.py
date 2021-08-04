#Stock Transaction Program

#Set constants
STOCK_BOUGHT = 2000         #Stock Shares Bought
STOCK_SOLD = 2000           #Stock Shares Sold
PRICE_BOUGHT = 40.00        #Price Stock was purchased
PRICE_SOLD = 42.75          #Price Stock was sold
COMMISSION = .03            #Percentage of Commission for Bought/Sold

#Sum total of stocks bought and sold
bought = STOCK_BOUGHT * PRICE_BOUGHT
sold = STOCK_SOLD * PRICE_SOLD

#Commission on bought and sold
commission_bought = bought * COMMISSION
commission_sold = sold * COMMISSION

#calculate sub-totals
total_bought = bought + commission_bought
total_sold = sold - commission_sold
total_after_sale = total_sold - total_bought

#Display calculations of stocks bought and sold along with commission rates
print("Purchase price for stock position: $", format(bought, ',.2F'), sep='')
print("Commission for stock purchase: $", format(commission_bought, ',.2F'), sep='')
print("Selling price for stock position: $", format(sold, ',.2F'), sep='')
print("Commission for stock sold: $", format(commission_sold, ',.2F'), sep='')

#Display final total bought and sold
print("Stock purchase price after stockbroker commission: $", format(total_bought, ',.2F'), sep='')
print("Stock sell price after stockbroker commission: $", format(total_sold, ',.2F'), sep='')

#pass the if/else test if profitable or not
if total_after_sale > 0:
    print("You made a profit of: $" ,format(total_after_sale, ',.2f'), sep='')
else:
    print("You had a loss of: $" ,format(total_after_sale, ',.2f'), sep='')
