
import pandas as pd
import matplotlib.pyplot as plt

# Read employee data
df = pd.read_csv("employees.csv")

# Check the data
print(df.head())

# --------------------------------
# Chart 1: Bar Chart - Average Salary
# --------------------------------

avg_salary = df.groupby("department")["salary"].mean()

plt.figure(figsize=(8, 5))
bars = plt.bar(avg_salary.index, avg_salary.values)

plt.title("Average Salary per Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

# Display values on bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.0f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.savefig("bar_chart.png")
plt.close()


# --------------------------------
# Chart 2: Histogram - Salary
# --------------------------------

plt.figure(figsize=(8, 5))

plt.hist(df["salary"], bins=5, edgecolor="black")

plt.title("Employee Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.savefig("histogram.png")
plt.close()


# --------------------------------
# Chart 3: Scatter Plot - ID vs Salary
# --------------------------------

plt.figure(figsize=(8, 5))

for department in df["department"].unique():
    dept_data = df[df["department"] == department]

    plt.scatter(
        dept_data["id"],
        dept_data["salary"],
        label=department
    )

plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend(title="Department")

plt.tight_layout()
plt.savefig("scatter_plot.png")
plt.close()


# --------------------------------
# Chart 4: Line Chart - Monthly Sales
# --------------------------------

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12, 15, 14, 18, 22, 25]

plt.figure(figsize=(8, 5))

plt.plot(
    months,
    sales,
    marker="o",
    label="Monthly Sales"
)

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()

plt.tight_layout()
plt.savefig("line_chart.png")
plt.close()


print("All 4 charts created successfully!")
