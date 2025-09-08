import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("data.csv")
print("Dataset loaded successfully!\n")
print("Available columns:", list(df.columns))
print("\nPreview:\n", df)


col = input("\nEnter the column name to calculate average: ")
if col in df.columns and pd.api.types.is_numeric_dtype(df[col]):
    avg = df[col].mean()
    print(f"Average of {col}: {avg:.2f}")
else:
    print("Invalid column or not numeric.")


xcol = input("\nEnter X column for bar chart (categorical): ")
ycol = input("Enter Y column for bar chart (numeric): ")
df.groupby(xcol)[ycol].mean().plot(kind="bar", title=f"Average {ycol} by {xcol}")
plt.xlabel(xcol)
plt.ylabel(f"Average {ycol}")
plt.show()

# Scatter plot
xcol = input("\nEnter X column for scatter plot: ")
ycol = input("Enter Y column for scatter plot: ")
df.plot(kind="scatter", x=xcol, y=ycol, title=f"{xcol} vs {ycol}")
plt.show()

# Heatmap
print("\nCorrelation Heatmap:")
corr = df.corr()
plt.imshow(corr, cmap="coolwarm", interpolation="nearest")
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title("Correlation Heatmap")
plt.show()
