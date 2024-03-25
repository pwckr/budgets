try:
    from globals import BUDGETS, USERS, SPENDINGS
except:
    from ...main.python.globals import BUDGETS, USERS, SPENDINGS

try:
    from datamanager import DataManager
except:
    from ...main.python.datamanager import DataManager

from datetime import datetime

import pandas as pd


class UserManager:
    """This class handles all user operations."""
    def __init__(self):
        # Load users, budgets and spendings data from "database"
        self.data_manager = DataManager()
        self.users = self.data_manager.load_create(USERS)
        self.spendings = self.data_manager.load_create(SPENDINGS)
        self.budgets = self.data_manager.load_create(BUDGETS)


    def create_new_account(self, username) -> None:
        """Create a new account and store it."""
        self.users.add(username)
        self.data_manager.write_data(USERS, self.users)


    def check_for_account(self, username) -> bool:
        """Check if a given username corresponds to an account."""
        return username in self.users


    def retrieve_username(self) -> str:
        """Ask the user for username and return it as string."""
        
        username = input("Please enter your username: ")

        return username


    def set_budget(self, username:str) -> int:
        """
        Let user set a budget.
        
        If user has no budget set already, setting one is mandatory.
        If there is a budget, user may decide to change it or to leave it as it is.
        """

        if username in self.budgets:
            print(f"Your old budget is {self.budgets[username]}.")
            initiate_new_budget = input("Would you like to set a new budget? (y/n): ")
            if initiate_new_budget == "y":
                self.budgets[username] = int(input("Please enter a new budget as integer: "))
                print(f"Your new budget is now: {self.budgets[username]}")
            else:
                print("You chose to not change your budget")
        else:
            print("You haven't set a budget yet.")
            self.budgets[username] = int(input("Please enter a new budget as integer: "))
            print(f"Your new budget is now: {self.budgets[username]}")

        self.data_manager.write_data(BUDGETS, self.budgets)
        return self.budgets[username]


    def log_expense(self, username:str)-> pd.DataFrame:
            """User gets to enter a new expense.
            
            If there is not spendings data of this user, an empty data frame is created.
            The expense is added to the users data frame.
            """

            if username not in self.spendings:
                df = pd.DataFrame(columns=['date', 'expense'])
                df['date'] = pd.to_datetime(df['date'], format='%y-%m-%d')
                self.spendings[username] = df

            date = datetime.now()
            expense_input = float(input("Enter the expense amount: "))

            self.spendings[username].loc[len(self.spendings[username])] = [date, expense_input]
            self.data_manager.write_data(SPENDINGS, self.spendings)
            print("Your spendings have been recorded.")
            return self.spendings[username]
