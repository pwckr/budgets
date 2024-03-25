from usermanagement import UserManager

class BudgetDSL:
    """This class defines a DSL for the budgeting app."""
    def __init__(self):
        self.user_manager = UserManager()
    
    def execute(self, command):
        """Execute DSL commands."""
        parts = command.split()
        verb = parts[0].lower()

        if verb == "create":
            return self._create_account(parts)
        elif verb == "set":
            return self._set_budget(parts)
        elif verb == "log":
            return self._log_expense(parts)
        else:
            return "Invalid command"

    def _create_account(self, parts):
        if len(parts) != 3 or parts[1] != "account":
            return "Invalid command"
        username = parts[2]
        self.user_manager.create_new_account(username)
        return f"Account '{username}' created successfully."

    def _set_budget(self, parts):
        if len(parts) != 4 or parts[1] != "budget" or parts[2] != "for":
            return "Invalid command"
        username = parts[3]
        return f"Budget set to {self.user_manager.set_budget(username)} for user '{username}'."

    def _log_expense(self, parts):
        if len(parts) != 4 or parts[1] != "expense" or parts[2] != "for":
            return "Invalid command"
        username = parts[3]
        return f"Expense logged: {self.user_manager.log_expense(username)} for user '{username}'."


# Example usage of the DSL
dsl = BudgetDSL()
commands = [
    "create account John",
    "set budget for John",
    "log expense for John"
]

for command in commands:
    print(dsl.execute(command))
