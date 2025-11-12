import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read dataset
df = pd.read_csv(r"C:\Users\hp\Downloads\Python_Lab\member.csv", sep='\t')

# Display basic info
print("Dataset Columns:", df.columns.tolist())
print(df.head())

# Create BooksBorrowed column if missing
if 'BooksBorrowed' not in df.columns:
    df['BooksBorrowed'] = np.random.randint(1, 20, size=len(df))
    print("\n[INFO] Added synthetic 'BooksBorrowed' column for analysis.\n")

# -----------------------------
# Step 1: Define age group bins
# -----------------------------
def categorize_age(age):
    if 16 <= age <= 19:
        return "Teens (16-19)"
    elif 20 <= age <= 29:
        return "Young Adults (20-29)"
    elif 30 <= age <= 49:
        return "Adults (30-49)"
    elif 50 <= age <= 64:
        return "Middle-aged (50-64)"
    elif age >= 65:
        return "Seniors (65+)"
    else:
        return "Unknown"

df['AgeGroup'] = df['Age'].apply(categorize_age)

# -----------------------------
# Step 2: Membership type borrowing
# -----------------------------
membership_borrow = df.groupby('Membership_Type')['BooksBorrowed'].sum().sort_values(ascending=False)
print("\nBooks Borrowed by Membership Type:\n", membership_borrow)

plt.figure(figsize=(8,5))
sns.barplot(x=membership_borrow.index, y=membership_borrow.values, palette="crest")
plt.title("Books Borrowed by Membership Type")
plt.ylabel("Total Books Borrowed")
plt.xlabel("Membership Type")
plt.show()

# -----------------------------
# Step 3: Borrowing frequency by Age Group
# -----------------------------
age_borrow = df.groupby('AgeGroup')['BooksBorrowed'].mean().sort_values(ascending=False)
print("\nAverage Borrowing by Age Group:\n", age_borrow)

plt.figure(figsize=(8,5))
sns.barplot(x=age_borrow.index, y=age_borrow.values, palette="mako")
plt.title("Average Borrowing Frequency by Age Group")
plt.ylabel("Average Books Borrowed")
plt.xlabel("Age Group")
plt.show()

# -----------------------------
# Step 4: Seasonal Borrowing Trends
# -----------------------------
if 'BorrowDate' in df.columns:
    df['BorrowDate'] = pd.to_datetime(df['BorrowDate'], errors='coerce')
    df['Month'] = df['BorrowDate'].dt.month_name()
    
    month_borrow = df.groupby('Month')['BooksBorrowed'].sum()
    ordered_months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    month_borrow = month_borrow.reindex(ordered_months)
    
    plt.figure(figsize=(10,5))
    sns.lineplot(x=month_borrow.index, y=month_borrow.values, marker='o')
    plt.title("Seasonal Borrowing Pattern")
    plt.ylabel("Total Books Borrowed")
    plt.xticks(rotation=45)
    plt.show()

# -----------------------------
# Step 5: Most Active and Inactive Members
# -----------------------------
member_activity = df.groupby('Member_ID')['BooksBorrowed'].sum().sort_values(ascending=False)
most_active = member_activity.head(5)
least_active = member_activity.tail(5)

print("\nMost Active Members:\n", most_active)
print("\nLeast Active Members:\n", least_active)
