import matplotlib.pyplot as plt
import os

# X-axis values (Months from April 2025 to December 2026)
months = [
    "April 2025", "May 2025", "June 2025", "July 2025", "August 2025",
    "September 2025", "October 2025", "November 2025", "December 2025",
    "January 2026", "February 2026", "March 2026", "April 2026", "May 2026",
    "June 2026", "July 2026", "August 2026", "September 2026", "October 2026",
    "November 2026", "December 2026"
]

# Y-axis values (same rainfall for all)
rainfall_mm = [264.93] * len(months)

# Create graph
plt.figure(figsize=(12, 6))
plt.plot(months, rainfall_mm, marker='o', color='green')
plt.xticks(rotation=45, ha='right')
plt.xlabel("Month (Year)")
plt.ylabel("Predicted Rainfall (mm)")
plt.title("Rainfall Prediction (April 2025 to December 2026)")
plt.tight_layout()

# Save image to static folder
static_path = os.path.join("static", "prediction_plot.png")
plt.savefig(static_path)
plt.close()

print(f"Graph saved at: {static_path}")
