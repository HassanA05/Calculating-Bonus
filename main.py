salesamount = 0

def get_sale_amount():
 print("Enter sales amount:£")
 salesamount = int(input())

 bonusB = salesamount / 100
 return bonusB, salesamount

def get_bonus( salesamount, bonusB):
 if salesamount > 5000:
   bonuspercent = bonusB * 20
 elif salesamount > 2000 and salesamount <= 5000:
   bonuspercent = bonusB * 10
 else: bonuspercent = 0
 return salesamount, bonuspercent, bonusB

def get_total_pay(bonuspercent, salesamount):
 totalmoney = bonuspercent + salesamount
 return totalmoney, bonuspercent, salesamount

def declare_tax():
 tax = 21
 return tax

def get_tax_percent(tax):
 taxpercent = 21 / 1000
 return taxpercent, tax


def get_tax_amount(totalmoney, taxpercent):
 taxamount = totalmoney * taxpercent
 return taxamount, totalmoney, taxpercent

def get_pay_after_tax(totalmoney, taxamount):
 payaftertax = totalmoney - taxamount
 return payaftertax, totalmoney, taxamount

def output_figures(bonuspercent, totalmoney, taxamount, payaftertax):
 print("Bonus amount is:£", round(bonuspercent,2))
 print("Total pay is:£",round(totalmoney,2))
 print("Tax amount of total pay is:£", round(taxamount,2))
 print("Pay after tax:£", round(payaftertax,2))
 return

bonusB, salesamount = get_sale_amount()
salesamount, bonuspercent, bonusB = get_bonus(salesamount, bonusB)
totalmoney, bonuspercent, salesamount = get_total_pay(bonuspercent, salesamount)
tax = declare_tax()
taxpercent, tax = get_tax_percent(tax)
taxamount, totalmoney, taxpercent = get_tax_amount(totalmoney, taxpercent)
payaftertax, totalmoney, taxamount =  get_pay_after_tax(totalmoney, taxamount)
output_figures(bonuspercent, totalmoney, taxamount, payaftertax)



