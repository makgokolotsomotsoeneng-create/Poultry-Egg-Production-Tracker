import matplotlib.pyplot as plt
from datetime import datetime

# Step 1: Store records here
records = []

# Step 2: Get number of days to record
days = int(input("How many days of data do you want to enter? "))

# Step 3: Loop to collect data
for i in range(days):
    date = input(f"Enter date for day {i +1} (YYYY-MM-DD): ")
    eggs = int(input("Enter number of eggs collected: "))
    hens = int(input("Enter number of hens: "))

    record = {"date": date, "eggs": eggs, "hens": hens}
    records.append(record)

# Step 4: Calculations
total_eggs = sum(r["eggs"] for r in records)
total_hens = records[0]["hens"] if records else 0  # Assume hens stay the same
avg_eggs_per_hen = total_eggs / (total_hens * days) if total_hens > 0 else 0
avg_daily_eggs = total_eggs / days if days > 0 else 0

# Step 5: Output results
print("Egg Collection Summary:")
print(f"Total eggs collected: {total_eggs}")
print(f"Average daily eggs: {avg_daily_eggs:.2f}")
print(f"Average eggs per hen per day: {avg_eggs_per_hen:.2f}")

# Step 6: Detect drop in production (below 80% of average daily eggs)
print("Production Alerts:")
for r in records:
    if r["eggs"] < 0.8 * avg_daily_eggs:
        print(f"{r['date']}: Production dropped ({r['eggs']} eggs)")

# Step 7: Visualization - line chart
dates = [datetime.strptime(r["date"], "%Y-%m-%d") for r in records]
eggs_collected = [r["eggs"] for r in records]

def plot_graph(dates, eggs_collected):
    plt.plot(dates, eggs_collected, marker='o', linestyle='-', color='green')
    plt.xlabel("Date")
    plt.ylabel("Eggs Collected")
    plt.title("Poultry Egg Production Over Time")
    plt.grid(True)
    plt.show()

plot_graph(dates, eggs_collected)

# Step 1: Store records
records = []

# Step 2: Get number of days to record
days = int(input("How many days of data do you want to enter? "))

# Step 3: Loop to collect data
for i in range(days):
    date = input(f"Enter date for day {i+1} (YYYY-MM-DD): ")
    eggs = int(input("Enter number of eggs collected: "))
    hens = int(input("Enter number of hens: "))
    
    record = {"date": date, "eggs": eggs, "hens": hens}
    records.append(record)

# Step 4: Calculate totals and averages
total_eggs = sum(r["eggs"] for r in records)
total_hens = records[0]["hens"] if records else 0  # assume hens same each day
avg_daily_eggs = total_eggs / days if days > 0 else 0
avg_eggs_per_hen = total_eggs / (total_hens * days) if total_hens > 0 else 0

# Step 5: Print summary
print("Egg Collection Summary:")
print(f"Total eggs collected: {total_eggs}")
print(f"Average daily eggs: {avg_daily_eggs:.2f}")
print(f"Average eggs per hen per day: {avg_eggs_per_hen:.2f}")