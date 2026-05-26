import pandas as pd

# Load
df = pd.read_csv("sales_data.csv")

# Clean
df["date"] = pd.to_datetime(df["date"])
df["satisfied"] = df["satisfied"].map({"yes": True, "no": False})

# Basic filters
print("=== UNSATISFIED CLIENTS ===")
print(df[df["satisfied"] == False][["client", "project_type", "revenue"]])

print("\n=== REVENUE BY INDUSTRY ===")
print(df.groupby("industry")["revenue"].sum().sort_values(ascending=False))

print("\n=== REVENUE BY PROJECT TYPE ===")
print(df.groupby("project_type")["revenue"].mean().sort_values(ascending=False))

print("\n=== TOP CLIENT ===")
print(df.groupby("client")["revenue"].sum().sort_values(ascending=False).head(3))