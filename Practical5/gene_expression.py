import matplotlib.pyplot as plt
gene_of_interest = "MYC"


gene_expression = {"TP53": 12.4,"EGFR": 15.1,"BRCA1": 8.2,"PTEN": 5.3,"ESR1": 10.7}

gene_expression["MYC"] = 11.6

print("\ngene expression dictionary:")
print(gene_expression)

print(f"\nSelected gene: {gene_of_interest}")
if gene_of_interest in gene_expression:
    print(f"Expression value of {gene_of_interest}: {gene_expression[gene_of_interest]}")
else:
    print(f"Error: gene '{gene_of_interest}' is not present in the dataset.")

average_expression = sum(gene_expression.values()) / len(gene_expression)
print(f"Average gene expression level: {average_expression:.2f}")

# Bar chart for gene expression
plt.figure(figsize=(8, 5))
plt.bar(gene_expression.keys(), gene_expression.values())
plt.title("Gene Expression Levels")
plt.xlabel("Gene")
plt.ylabel("Expression Value")
plt.tight_layout()
plt.savefig("gene_expression_bar_chart.png")
plt.show()
