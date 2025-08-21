# Program 19: Gross salary
basic = float(input("Enter basic salary: "))
da = 0.6 * basic
hra = 0.15 * basic
gross = basic + da + hra
print("Gross Salary:", gross)