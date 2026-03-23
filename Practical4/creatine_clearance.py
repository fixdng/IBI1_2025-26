
# 1. enter age, weight, gender, and creatine concentration.
# 2. Check the input is valid
# 3. If any input is invalid, print which variable needs corrected.
# 4. If gender is female, multiply the result by 0.85.


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
