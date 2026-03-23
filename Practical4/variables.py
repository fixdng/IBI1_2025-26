a=5.08 #2004 population
b=5.33 #2014 population
c=5.55 #2024 population

# Calculate the population change
d=b-a
e=c-b

# Compare d and e
if d > e:
    print("d is larger than e")
elif e > d:
    print("e is larger than d")
else:
    print("d and e are equal")

#comment：Since d is larger than e, the population change is decelerating


# Create Boolean variables
X = True
Y = False
W = X or Y
print("W =", W)

# Truth table for W = X or Y
# X      Y      W
# True   True   True
# True   False  True
# False  True   True
# False  False  False
