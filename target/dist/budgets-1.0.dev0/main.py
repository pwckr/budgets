import os
from usermanagement import UserManager
from reporting import Reporting

if __name__ == "__main__":
    print("##################################################")
    print("Welcome to the budgets-app.")
    print("")
    os.chdir("/Users/pwecker/dev/budgets")
    user_manager = UserManager()

    user_name = user_manager.retrieve_username()
    print("")    
    budget = user_manager.set_budget(user_name)
    print("")
    spendings = user_manager.log_expense(username=user_name)
    print("")
    reporter = Reporting()

    reporter.report_spendings(spendings)
    print("")
    remaining_budget = reporter.compute_remaining_budget(budget, spendings)
    print(f"Your remaining budget is {remaining_budget}.")