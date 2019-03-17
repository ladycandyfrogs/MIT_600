""" annual_salary = float(input("Enter your annual salary:"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = float(input("Enter the cost of your dream home:"))
semi_annual_rise = float(input("Enter the semiannual raise, as a decimal:")) """

annual_salary = float(120000)
portion_saved = float(.10)
total_cost = float(1000000)
semi_annual_rise = float(.15)

portion_down_payment = 0.25
current_savings = 0.0
r = 0.04

#Here we calculate the total amount of months it will take to pay the full amount
# print("Number of months:", int(total_cost/(annual_salary*portion_saved/12)))

#start counter for loop and initialize current_savings
i = 0
current_savings = annual_salary*portion_saved/12

for i in range(7):
    #every month we receive a return(r) of 0.04
    current_savings += current_savings*r
    print(current_savings, i)
    if i == 6:
        #every 6th month we receive a raise
        print("Annual salary before raise:", int(annual_salary))
        annual_salary += annual_salary*semi_annual_rise
#         print("Annual salary after raise:", int(annual_salary))
