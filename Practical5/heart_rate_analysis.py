
import matplotlib.pyplot as plt
heart_rates = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]

num_patients = len(heart_rates)
mean_heart_rate = sum(heart_rates) / num_patients

print(f"\nThere are {num_patients} patients in the dataset and the mean heart rate is {mean_heart_rate:.2f} bpm.")

low_count = 0
normal_count = 0
high_count = 0

for rate in heart_rates:
    if rate < 60:
        low_count += 1
    elif rate <= 120:
        normal_count += 1
    else:
        high_count += 1

print(f"Low category (<60 bpm): {low_count} patients")
print(f"Normal category (60-120 bpm): {normal_count} patients")
print(f"High category (>120 bpm): {high_count} patients")

categories = { "Low": low_count,"Normal": normal_count,"High": high_count}

largest_category = max(categories, key=categories.get)
print(f"The category with the largest number of patients is: {largest_category}")

plt.figure(figsize=(6, 6))
plt.pie(
    categories.values(),
    labels=categories.keys(),
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Distribution of Heart Rate Categories")
plt.tight_layout()
plt.savefig("heart_rate_pie_chart.png")
plt.show()