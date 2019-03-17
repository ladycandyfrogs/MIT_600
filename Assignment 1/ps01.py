annual_salary = float(input("Enter your annual salary:"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = float(input("Enter the cost of your dream home:"))

portion_down_payment = 0.25
current_savings = 0.0
r = 0.04

#Here we calculate the total amount of months it will take to pay the full amount
print("Number of months:", int(total_cost/(annual_salary*portion_saved/12)))

# print("Number of years:", "%.1f" % round(years, 1))                                                    