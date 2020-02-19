class bank():
 def budget():
    print("Welcome to BudgetCheck.")
    income = int(input("How much do you earn in a month? £"))
    rent = int(input("How much is your rent? £"))
    elec = int(input("How much is your electricity bill? £")) #electricity
    water = int(input("How much is your water bill? £"))
    gas = int(input("How much is your gas bill? £"))
    phone = int(input("How much is your phone bill? £"))
    wifi = int(input("How much is your broadband bill? £"))
    totalbill = rent + elec + water + gas + phone + wifi
    total = income - totalbill
    print("You have £", total ," to spend on food and other essentials.")
bank.budget()    
