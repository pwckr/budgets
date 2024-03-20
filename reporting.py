from datetime import datetime
import pandas as pd

class Reporting:
    """
    This class serves the purpose of all kinds of reportings.
    
    Reports may be simple as computing the remaining budget or complex
    as predicting if the budget will be met or anything like that.
    """

    def compute_remaining_budget(self, budget: float, df: pd.DataFrame) -> float:
        """Compute the remaining budget of the current month"""
        df['month'] = df['date'].apply(lambda x: x.month)
        df = df[df["month"]== datetime.now().month]
        sum = df['expense'].sum()
        remaining_budget = budget - sum
        return remaining_budget

    def report_spendings(self, spendings: pd.DataFrame) -> None:
        """Report on spendings of user."""
        print("These are your spendings:")
        print(spendings)