total_students = 91
infected = 5
growth_rate = 0.4

print("Day 1 :", infected, "students infected")

for day in range(2, 100): #Use a for loop to calculate future days.
    infected = infected + infected * growth_rate

    if infected > total_students:
        infected = total_students #If infected exceeds class size, set it equal to class size.

    print("Day", day, ":", infected, "students infected")

    if infected == total_students: # Stop once all students are infected.
        print("It took", day, "days to infect all students.") # Print total days needed.
        break
