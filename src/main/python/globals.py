"""
Globals variables for the three data files.

In their respective dictionaries, their path, name and initialiser is stored.
"""

BUDGETS = {"path": "data_files/budgets.pkl",
           "name": "Budgets",
           "initialiser": dict()}

SPENDINGS = {"path": "data_files/spendings.pkl",
             "name": "Spendings",
             "initialiser": dict()}

USERS = {"path":"data_files/users.pkl",
         "name": "Users",
         "initialiser": set()}