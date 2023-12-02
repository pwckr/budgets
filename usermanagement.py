from datetime import date
from pathlib import Path
from typing import Optional

import pandas as pd

class UserManager():
    def __init__(self) -> "UserManager":
        if Path("budgets").is_file():
            self.budgets = pd.read_parquet("budgets")
        else:
            data = {"account": [],
                    "budget": []}
            self.budgets = pd.DataFrame(data=data)
            self.budgets.to_parquet("budgets")

        if Path("expenses").is_file():
            self.expenses = pd.read_parquet("expenses")
        else:
            data = {"date": [],
                    "account": [],
                    "expense": []}
            self.expenses = pd.DataFrame(data=data)
            self.expenses.to_parquet("expenses")

    @staticmethod
    def ask_for_account() -> str:
        print("Please type in your account name.")
        print("If you don't have an account, a new account will be created.")
        account = input("Your Account name: ")
        return account
    
    def retrieve_budget(self, account: str) -> Optional[float]:
        if account not in self.budgets["account"].values:
            return None
        else:
            return self.budgets[self.budgets["account"]==account]["budget"].values

    def set_budget(self, account: str) -> float:
        budget = float(input("Please enter your budget: "))
        # Use dict instead
        df = pd.DataFrame(data={"account": [account],
                                "budget": [budget]})
        self.budgets = pd.concat([self.budgets, df])
        return budget

    def retrieve_expense(self, account) -> float:
        expense = float(input("How much did you spend? "))
        d = date.today()
        df = pd.DataFrame(data={"account": [account],
                                "date": [d],
                                "expense": [expense]})

        self.expenses = pd.concat([self.expenses, df])
        return expense

    def retrieve_remaining_budget(self, account):
        month = date.today().month
        budget = self.retrieve_budget(account)

        all_expenses = self.expenses[self.expenses["account"]==account]["expense"].sum()
        remaining_budget = budget - all_expenses
        return remaining_budget[0]
    
    def save_and_quit(self):
        self.budgets.to_parquet("budgets")
        self.expenses.to_parquet("expenses")
