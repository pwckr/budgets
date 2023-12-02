
from usermanagement import UserManager

def main():

    user_manager = UserManager()

    account = user_manager.ask_for_account()
    budget = user_manager.retrieve_budget(account)
    if budget is None:
        budget = user_manager.set_budget(account)
    expense = user_manager.retrieve_expense(account)
    remaining_budget = user_manager.retrieve_remaining_budget(account)

    print(f"You have spent {expense} euros.")
    print(f"Your remaining budget for this month is {remaining_budget}")

    user_manager.save_and_quit()
if __name__ == "__main__":
    print("####### Starting program")
    main()
# %%
