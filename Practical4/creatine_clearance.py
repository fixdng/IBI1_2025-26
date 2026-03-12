
# 1. Ask the user to enter age, weight, gender, and creatine concentration.
# 2. Convert age, weight, and creatine concentration into numbers.
# 3. Check whether age is less than 100.
# 4. Check whether weight is greater than 20 and less than 80.
# 5. Check whether creatine concentration is greater than 0 and less than 100.
# 6. Check whether gender is either "male" or "female".
# 7. If any input is invalid, print which variable needs corrected.
# 8. If all inputs are valid, calculate creatine clearance.
# 9. If gender is female, multiply the result by 0.85.
# 10. Print the final creatine clearance rate.

age = int(input("Enter age in years: "))
weight = float(input("Enter weight in kg: "))
gender = input("Enter gender (male or female): ")
cr = float(input("Enter creatine concentration in umol/l: "))

valid = True

if age >= 100:
    print("Age needs corrected.")
    valid = False

if weight <= 20 or weight >= 80:
    print("Weight needs corrected." , "weight should be	>	20	kg	and	< 80	kg")
    valid = False

if cr <= 0 or cr >= 100:
    print("Creatine concentration needs corrected.")
    valid = False

if gender != "male" and gender != "female":
    print("Gender needs corrected.")
    valid = False

if valid:
    crcl = ((140 - age) * weight) / (72 * cr)

    if gender == "female":
        crcl = crcl * 0.85

    print("Creatine clearance rate is " + str(crcl))
