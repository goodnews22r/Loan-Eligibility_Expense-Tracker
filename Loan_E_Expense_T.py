print("=== LOAN ELIGIBILITY & EXPENSE CALCULATOR ===")

#Age Validation
age = int(input("Enter your age: "))
if age < 18:
    print("Sorry, you are too young to proceed.")
else:
    print("Age verification successful.")

    #sign up
    created_username = input("Create a username: ")
    created_password = input("Create a password: ")

    print("\nAccount created successfully!")

    print("\n=== LOGIN ===")


    #login
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == created_username and password == created_password:
        print("Login successful.")
        
        #Loan Eligibility
        income = float(input("Enter your monthly income: "))
        expenses = float(input("Enter your monthly expenses: "))
        
        if age >=21 and income >= 50000 and expenses <= 30000:
            print("Congratulations! You are eligible for a loan.")
        else:
            print("Sorry, you are not eligible for a loan.")
       

        #Expense Tracker
        budget = float(input("Enter your monthly budget: "))
        expense = float(input("Enter your total monthly expenses: "))

        if expense > budget:
            print("You are over budget. Consider reducing your expenses.")
        else:           
            print("You are within your budget. Keep it up!")
    else:
        print("Invalid username or password. Please try again.")