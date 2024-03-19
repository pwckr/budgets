from datetime import datetime
import pandas as pd
import pickle
from typing import List
import os

print("Welcome to spendings_app.")

#Load usernames
if os.path.exists("users.pkl"):
    with open("users.pkl", "rb") as f:
        users_set = pickle.load(f)
        print("Users loaded.")
else:
    print("Creating users-file.")
    users_set = set()

#Load budgets
if os.path.exists("budgets.pkl"):
    with open("budgets.pkl", "rb") as f:
        budgets = pickle.load(f)
        print("Budgets loaded")
else:
    print("Creating budgets file.")
    budgets = dict()

#Load spendings
if os.path.exists("spendings.pkl"):
    with open("spendings.pkl", "rb") as f:
        spendings = pickle.load(f)
        print("Spendings loaded.")
else:
    print("Creating spendings file in working memory.")
    spendings = dict()



username = input("Please enter your username: ")
print("We will check if we can find your account...")

if username in users_set:
    print("We have retrieved your account from our system.")
else:
    print("We could not find your account. Would you like to create a new account with this username?")
    create_new_account = input("Please respond with y/n: ")
    if create_new_account == "y":
        users_set.add(username)
        with open("users.pkl", "wb") as f:
            pickle.dump(users_set, f)
        print(f"Your account has been created with the username <{username}>.")
    elif create_new_account == "n":
        print("You chose to not create an account. Thanks for using this app.")
        quit()
    else:
        print("Your response was invalid. The program will stop here but we're happy to see you again.")
        quit()

# Now retrieve a budget, if existent
if username in budgets:
    print(f"Your budget is {budgets[username]}")
    initiate_new_budget = input("Would you like to set a new budget? (y/n): ")
    if initiate_new_budget == "y":
        budgets[username] = int(input("Please enter a new budget as integer: "))
        print(f"Your new budget is now: {budgets[username]}")
    else:
        print("You chose to not change your budget")
else:
    print("You haven't set a budget yet.")
    budgets[username] = int(input("Please enter a new budget as integer: "))
    print(f"Your new budget is now: {budgets[username]}")
with open("budgets.pkl", "wb") as f:
    pickle.dump(budgets, f)
print("The budgets file has been saved.")

enter_expense = input("Would you like to enter an expense and save it to your spendings table (y/n)? ")

if enter_expense == "y":
    if username not in spendings:
        df = pd.DataFrame(columns=['date', 'expense'])
        df['date'] = pd.to_datetime(df['date'], format='%y-%m-%d')

        spendings[username] = df

    date = datetime.now()
    print(date)
    expense_input = float(input("Enter the expense amount: "))

    spendings[username].loc[len(spendings[username])] = [date, expense_input]
    with open("spendings.pkl", "wb") as f:
        pickle.dump(spendings, f)
    print("Your spendings have been recorded. These are your total spendings:")
    print(spendings[username])
else:
    print("You chose to not enter an expense.")
df = spendings[username]
df['month'] = df['date'].apply(lambda x: x.month)
df = df[df["month"]== 3]
sum = df['expense'].sum()
print(f"For this month, you have spent X. You still have {budgets[username] - sum} to spend.")