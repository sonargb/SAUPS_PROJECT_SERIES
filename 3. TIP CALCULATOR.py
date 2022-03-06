meal=float(input("Enter your meal amount: "))
tip=int(input("Enter your tip in % : "))
tax=5/100
tip_amt=meal*tip/100
tax_amt=meal*tax
total=meal+tip_amt+tax_amt
print(f"Your tip is {tip_amt:.2f} \nYour tax on meal is {tax_amt:.2f}")
print(f"Your total bill amount with tax is {total:.2f}")