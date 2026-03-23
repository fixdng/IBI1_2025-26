# Pseudocode:
# 1. Set total class size, starting infected students, growth rate
# 2 Use a for loop to calculate future days.
# 3. Update infected count each day.
# 4. If infected exceeds class size, set it equal to class size.
# 5. Stop once all students are infected.


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
