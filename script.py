#Add fifth column with column 1 value subtracted from column 2 value 

import csv

with open('brca_cnvs_tcga-1.csv', 'r') as csvinput
    
    with open('brca_cnvs_tcga-1.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        all = []
        row = next(reader)
        row = append('
