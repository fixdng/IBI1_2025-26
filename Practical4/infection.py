# Pseudocode:
# 1. Set total class size.
# 2. Set starting infected students.
# 3. Set growth rate.
# 4. Print day 1 infected count.
# 5. Use a for loop to calculate future days.
# 6. Update infected count each day.
# 7. If infected exceeds class size, set it equal to class size.
# 8. Print infected count for each day.
# 9. Stop once all students are infected.
# 10. Print total days needed.

total_students = 91
infected = 5
growth_rate = 0.4

print("Day 1 :", infected, "students infected")

#Use a for loop to calculate future days.
for day in range(2, 100): 
    infected = infected + infected * growth_rate

    if infected > total_students:
       infected = total_students 

    print("Day", day, ":", infected, "students infected")

# Stop once all students are infected
    if infected == total_students: 
        print("It took", day, "days to infect all students.") 
        break
