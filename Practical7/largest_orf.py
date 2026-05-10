import re
seq="AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG"
orfs=re.findall(r'(?=(AUG(?:(?!UAA|UAG|UGA)[ACGU]{3})*(?:UAA|UAG|UGA)))',seq)
if orfs:
    longest_orf = max(orfs, key=len)
    print("The longest ORF is:", longest_orf)
    print("The ORF length is:", len(longest_orf))
else:
    print("No ORF found")