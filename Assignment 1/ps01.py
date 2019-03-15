annual_salary = float(input("Enter your annual salary:"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = float(input("Enter the cost of your dream home:"))

portion_down_payment = 0.25
current_savings = 0.0
r = 0.04

monthly_savings = (annual_salary*portion_saved)/12
months = total_cost/monthly_savings
years = months/12

print("Number of months:", int(months))
print("Number of years:", "%.1f" % round(years, 1))