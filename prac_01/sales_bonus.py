"""
Program to calculate and display a user's bonus based on sales.  
If sales are under $1,000, the user gets a 10% bonus.  
If sales are $1,000 or over, the bonus is 15%.  
"""

sales = float(input("Enter sales: $"))
while sales != 0:
    if sales < 1000:
        sales_bonus = 10/100*sales
    if sales >= 1000:
        sales_bonus = 15/100*sales
    else:
        sales_bonus = 0
    print(f"bonus = ${sales_bonus}")
    sales = float(input("Enter sales: $"))