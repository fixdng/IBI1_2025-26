import re

i = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
o = open('stop_genes.fa', 'w')

gene_name = ''
seq = ''

for line in i:
    line = line.rstrip()

    if line.startswith(">"):

        if gene_name != '':
            results = re.findall(r'ATG(?:[ACGT]{3})*?(?:TAA|TAG|TGA)', seq)

            if results:
                stop_codons = []

                for result in results:
                    stop = result[-3:]
                    if stop not in stop_codons:
                        stop_codons.append(stop)

                o.write(">" + gene_name + ";" + ",".join(stop_codons) + "\n")
                o.write(results[0] + "\n")

        gene_name = line[1:].split()[0]
        seq = ''

    else:
        seq += line.upper()


if gene_name != '':
    results = re.findall(r'ATG(?:[ACGT]{3})*?(?:TAA|TAG|TGA)', seq)

    if results:
        stop_codons = []

        for result in results:
            stop = result[-3:]
            if stop not in stop_codons:
                stop_codons.append(stop)

        o.write(">" + gene_name + ";" + ",".join(stop_codons) + "\n")
        o.write(results[0] + "\n")


i.close()
o.close()
