
import matplotlib.pyplot as plt
population_2020 = { "UK": 66.7,"China": 1426.0, "Italy": 59.4, "Brazil": 208.6, "USA": 331.6}

population_2024 = {"UK": 69.2,"China": 1410.0,"Italy": 58.9,"Brazil": 212.0, "USA": 340.1}

population_change = {}

print("\nPercentage population change for each country:")
for country in population_2020:
    percent_change = ((population_2024[country] - population_2020[country]) / population_2020[country]) * 100
    population_change[country] = percent_change
    print(f"{country}: {percent_change:.2f}%")

# Sort descending from largest increase to largest decrease
sorted_changes = sorted(population_change.items(), key=lambda x: x[1], reverse=True) #dictionary sorting

print("\nPopulation changes from largest increase to largest decrease:")
for country, change in sorted_changes:
    print(f"{country}: {change:.2f}%")

largest_increase_country = sorted_changes[0][0]
largest_decrease_country = sorted_changes[-1][0]

print(f"\nCountry with the largest increase in population: {largest_increase_country}")
print(f"Country with the largest decrease in population: {largest_decrease_country}")

# Bar chart for population changes
countries = list(population_change.keys())
changes = list(population_change.values())

plt.figure(figsize=(8, 5))
plt.bar(countries, changes)
plt.title("Population Change from 2020 to 2024")
plt.xlabel("Country")
plt.ylabel("Percentage Change (%)")
plt.tight_layout()
plt.savefig("population_change_bar_chart.png")
plt.show()