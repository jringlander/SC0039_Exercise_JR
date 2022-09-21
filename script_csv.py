# Script to calculate the length of a region by substracting columns loc.end and loc.start
import csv
# create new file
new = open('brca_cnvs_tcga-1_new.csv', 'w')
writer = csv.writer(new)

# Open old file, read and add header to new column
with open('brca_cnvs_tcga-1.csv', 'r') as old:
    reader = csv.reader(old)

    for i in reader:
        if 'ID' in i:
            i.append('length')
            writer.writerow(i)
        else:
            locend = int(i[3])
            locstart = int(i[2])
            length = locend - locstart
            i.append(length)
            writer.writerow(i)
