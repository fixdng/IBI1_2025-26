import matplotlib.pyplot as plt

input_file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_plot = 'codon_frequency_pie.png'

stop_codon = input("Enter a stop codon (TAA, TAG, or TGA): ").strip().upper()

if stop_codon not in ['TAA', 'TAG', 'TGA']:
    print("Invalid stop codon. Please enter TAA, TAG, or TGA.")
    exit()

codon_counts = {}

def process_gene(sequence, chosen_stop, codon_counts_dict):
    longest_orf = ''
    all_stop_codons = ['TAA', 'TAG', 'TGA']

    # Try every possible ATG start position
    for start in range(len(sequence) - 2):
        if sequence[start:start+3] == 'ATG':

            # Move in-frame from this ATG
            for pos in range(start + 3, len(sequence) - 2, 3):
                codon = sequence[pos:pos+3]

                # ORF ends at the first in-frame stop codon
                if codon in all_stop_codons:

                    # Only use this ORF if it ends with the user-chosen stop codon
                    if codon == chosen_stop:
                        orf = sequence[start:pos+3]

                        if len(orf) > len(longest_orf):
                            longest_orf = orf

                    # Stop checking this ORF once any stop codon is reached
                    break

    # Count codons upstream of the final stop codon
    if longest_orf != '':
        for pos in range(0, len(longest_orf) - 3, 3):
            codon = longest_orf[pos:pos+3]

            if codon in codon_counts_dict:
                codon_counts_dict[codon] += 1
            else:
                codon_counts_dict[codon] = 1


# Read FASTA file
i = open(input_file, 'r')

gene_name = ''
seq = ''

for line in i:
    line = line.rstrip()

    if line.startswith(">"):

        # Process the previous gene
        if gene_name != '':
            process_gene(seq, stop_codon, codon_counts)

        # Start a new gene
        gene_name = line[1:].split()[0]
        seq = ''

    else:
        seq += line.upper()

# Process the final gene
if gene_name != '':
    process_gene(seq, stop_codon, codon_counts)

i.close()


# Report results and make pie chart
if len(codon_counts) == 0:
    print("No genes found containing an ORF ending with", stop_codon)

else:
    print("Codon counts for ORFs ending with", stop_codon)

    for codon in sorted(codon_counts):
        print(codon, codon_counts[codon])

    labels = []
    sizes = []

    total = sum(codon_counts.values())

    for codon in sorted(codon_counts):
        count = codon_counts[codon]
        percentage = count / total * 100
        labels.append(codon + " (" + str(count) + ", " + format(percentage, ".1f") + "%)")
        sizes.append(count)

    plt.figure(figsize=(12, 10))

    wedges, texts = plt.pie(sizes, startangle=90)

    plt.title('Codon Frequency for ORFs Ending with ' + stop_codon)

    plt.legend(
        wedges,
        labels,
        title="Codons",
        loc="center left",
        bbox_to_anchor=(1, 0, 0.5, 1),
        fontsize=8
    )

    plt.tight_layout()
    plt.savefig(output_plot, bbox_inches='tight')
    plt.close()

    print("Pie chart saved to", output_plot)
