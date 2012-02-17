import csv

def tsv2csv(input, output, columns=None):
    reader = csv.reader(input, dialect='excel-tab')
    writer = csv.writer(output, dialect='excel')
    for row in reader:
        writer.writerow(row)

if __name__ == '__main__':
    import sys
    tsv2csv(sys.stdin, sys.stdout)
