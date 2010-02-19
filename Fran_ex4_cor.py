import sys
program_name = sys.argv[0]
if len(sys.argv) != 2:
    sys.exit(program_name + ": Expecting one argument: [filename]")
 
if len(sys.argv) == 2:
    filename = sys.argv[1]
    input_stream = open(filename, 'rU')
else:
    input_stream = sys.stdin

#def read_codon(cod):
    #input in a codon, spits out amino acid
genetic_code = {'GUC': 'V', 'ACC': 'T', 'GUA': 'V', 'GUG': 'V', 'ACU': 
'T', 'AAC': 'N', 'CCU': 'P', 'UGG': 'W', 'AGC': 'S', 'AUC': 'I', 
'CAU': 'H', 'AAU': 'N', 'AGU': 'S', 'GUU': 'V', 'CAC': 'H', 'ACG': 
'T', 'CCG': 'P', 'CCA': 'P', 'ACA': 'T', 'CCC': 'P', 'UGU': 'C', 
'GGU': 'G', 'UCU': 'S', 'GCG': 'A', 'UGC': 'C', 'CAG': 'Q', 'GAU': 
'D', 'UAU': 'Y', 'CGG': 'R', 'UCG': 'S', 'AGG': 'R', 'GGG': 'G', 
'UCC': 'S', 'UCA': 'S', 'UAA': '*', 'GGA': 'G', 'UAC': 'Y', 'GAC': 
'D', 'UAG': '*', 'AUA': 'I', 'GCA': 'A', 'CUU': 'L', 'GGC': 'G', 
'AUG': 'M', 'CUG': 'L', 'GAG': 'E', 'CUC': 'L', 'AGA': 'R', 'CUA': 
'L', 'GCC': 'A', 'AAA': 'K', 'AAG': 'K', 'CAA': 'Q', 'UUU': 'F', 
'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'GCU': 'A', 'GAA': 'E', 'AUU': 
'I', 'UUG': 'L', 'UUA': 'L', 'UGA': '*', 'UUC': 'F'}
#    print cod, genetic_code[cod]

trans_on=False
protein_list=[]
fat_string=""
for line in input_stream:      #concatenates all the lines of input together
    fat_string = fat_string+line
fat_string = fat_string.replace("\n","")  #removes the return char
for pos in range(0,(len(fat_string)),3):  #Positions at every 3 until the end
    codon = fat_string[pos:(pos+3)] #makes a codon out of a string of 3 from a certain position
    if codon =='AUG':
        trans_on = True
    if len(codon)==3 and trans_on:  #Only appends to list if codon is a triplet
        translated = genetic_code[codon]
        protein_list.append(translated)
        if translated == '*':
            trans_on=False
protein_string = ''.join(protein_list)
print protein_string.split('*')  #the lazy person's way of splitting by stop codons.  I totally didn't add anything for start codon.
