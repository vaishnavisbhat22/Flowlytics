import pandas as pd

# Load dataset
df = pd.read_csv("flowlytics_data.csv")

# Task Completion Rate
df["Completion_Rate"] = df["Tasks_Completed"] / df["Tasks_Planned"]

# Sleep Score Function
def sleep_score(hours):
    if 7 <= hours <= 8:
        return 100
    elif 6 <= hours < 7 or 8 < hours <= 9:
        return 70
    else:
        return 40

df["Sleep_Score"] = df["Sleep_Hours"].apply(sleep_score)

# Productivity Score Calculation
df["Productivity_Score"] = (
    (df["Study_Hours"] * 0.4) +
    (df["Completion_Rate"] * 40) +
    (df["Sleep_Score"] * 0.2)
)

# ✅ Define function OUTSIDE loop
def generate_insights(row):
    insights = []

    if row["Productivity_Score"] < 50:
        insights.append("Your productivity is very low today.")

    if row["Sleep_Hours"] < 6:
        insights.append("Lack of sleep is reducing your efficiency.")

    if row["Completion_Rate"] < 0.6:
        insights.append("You are planning too much but completing less.")

    if row["Screen_Time"] > 5:
        insights.append("High screen time is affecting your focus.")

    if row["Productivity_Score"] > 75:
        insights.append("Great job! You had a productive day.")

    return insights

# Apply insights
df["Insights"] = df.apply(generate_insights, axis=1)

# Print results
for index, row in df.iterrows():
    print(f"Date: {row['Date']}")
    print(f"Productivity Score: {round(row['Productivity_Score'], 2)}")

    print("Insights:")
    for insight in row["Insights"]:
        print(f"- {insight}")

    print("-" * 40)