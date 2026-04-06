#variant2
monthly_income = float(input("Enter your monthly income: "))
print("Enter your expense amounts:")
expenses = {
    "housing": float(input("Housing: ")),
    "food": float(input("Food: ")),
    "transport": float(input("Transport: ")),
    "utilities": float(input("Utilities: ")),
    "entertainment": float(input("Entertainment: ")),
    "other": float(input("Other: "))
}

current_savings = float(input("Current savings amount: "))
goal_amount = float(input("Goal amount: "))
target_months = int(input("Months to reach goal: "))

total_expenses = sum(expenses.values())
monthly_savings = monthly_income - total_expenses
savings_rate = (monthly_savings / monthly_income) * 100
future_savings = current_savings + (monthly_savings * target_months)
gap = goal_amount - current_savings
required_monthly_saving = gap / target_months

below_recommended = savings_rate < 20
on_track = monthly_savings >= required_monthly_saving
overspending = total_expenses > monthly_income
goal_possible = monthly_savings > 0

print("\n====== Financial Report ======")
print(f"Monthly Income: ${monthly_income}")
print(f"Total Expenses: ${total_expenses}")
print(f"Monthly Savings: ${monthly_savings}")
print(f"Savings Rate: {savings_rate:.2f}%")

print("\n--- Status Indicators ---")
print(f"Below Recommended (<20% Savings Rate): {below_recommended}")
print(f"On Track for Goal: {on_track}")
print(f"Overspending (Expenses > Income): {overspending}")
print(f"Goal Possible with Current Savings Rate: {goal_possible}")

print("\n--- Future Projection ---")
print(f"Projected Savings in {target_months} months: ${future_savings}")
print(f"Required Monthly Saving to Reach Goal: ${required_monthly_saving}")


