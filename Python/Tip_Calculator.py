print("Please enter percentages as decimals. example write 6% as .06")
bill_amount= float(input("How much is the total cost? "))
tax_percentage=(input("Is that with or without sales tax (with/without) "))

if tax_percentage=="with":
  tax_percentage=0
  
else:
  tax_percentage=float(input("what is your states sales tax?"))
tip_percentage=.15
tip_percentage=(input("Would you like to leave a standard tip of 15% (yes/no)"))


if tip_percentage=="yes":
  tip_percentage=.15

else:
    tip_percentage= float(input("What percentage of a tip would you like to leave? (Enter as a decimal)"))
tip_amount= bill_amount*tip_percentage
total_without_tax=bill_amount+tip_amount
total_with_tax= bill_amount*tax_percentage+total_without_tax
total=total_with_tax
print(f"your total cost will be ${total}")