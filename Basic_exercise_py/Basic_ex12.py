# Exercise 12: Calculate income tax
# Calculate income tax for the given income by adhering to the rules below
#
# Taxable Income	Rate (in %)
# First $10,000	0
# Next $10,000	10
# The remaining	20
# Expected Output:
#
# For example, suppose the income is 45000, and the income tax payable is
#
# 10000*0% + 10000*10%  + 25000*20% = $6000


# tax_emp = int(input("entr the income:- "))
#
# tax1 = 0
# if tax_emp <= 10000:
#     tax1 = 0
# elif tax_emp <= 20000 and tax_emp > 10000:
#
#    tax1 += (tax_emp - 10000) * 10 /100
#
# elif tax_emp > 20000:
#     tax1 = 1000
#     tax1 += (tax_emp - 20000) * 20 /100
# print(tax1)
# ##########################################################33
# income  = 45000
#
# if income < 10000:
#     tax1 = 0
#     print(tax1)
# elif income > 10000 and income < 20000:
#     tax2 = (income-10000)*0.1
# elif income >20000:
#     income = income-20000
#     tax3 = income*0.2 +(10000*0.1)
#     print(tax3)
# ########################################
income = int(input("enter the income: "))
def tax_calculation():
    global income
    if income < 10000:
        tax1 = 0
        print(tax1)
    elif income > 10000 and income < 20000:
        tax2 = (income-10000)*0.1
    elif income >20000:
        income = income-20000
        tax3 = income*0.2 +(10000*0.1)
        print(tax3)
tax_calculation()
