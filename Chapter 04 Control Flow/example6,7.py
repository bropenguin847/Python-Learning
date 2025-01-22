# Input the taxable income
inc = float(input('Input an income: '))

#(6) Decision approach
# Calculate the tax payable based on the income range
# def practice6(inc):
#     if inc <= 10000:
#         tax = 0.1 * inc
#     elif inc <= 20000:
#         tax = 1000 + 0.2 * (inc - 10000)
#     else:
#         tax = 3000 + 0.5 * (inc - 20000)
#     return tax

# tax1 = practice6(inc)

#########################################################
#(7) Logical approach
# Calculate the tax payable using logical conditions
# def practice7(inc):
tax1 = (0.1 * inc) * (inc <= 10000)
tax2 = (1000 + 0.2 * (inc - 10000)) * (inc > 10000 and inc <= 20000)
tax3 = (3000 + 0.5 * (inc - 20000)) * (inc > 20000)
tax = tax1 + tax2 + tax3
    # return tax

# tax = practice7(inc)

# Sum the taxes based on conditions
# Only one condition will evaluate to True at a time. Therefore, the addition
# in the final line will produce the output of the formula corresponding to the True condition.

# Display the tax payable with two decimal points
print('Tax Payable =', format(tax, '.2f'))
