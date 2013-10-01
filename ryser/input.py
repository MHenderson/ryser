# Created Tue Oct  1 16:25:40 BST 2013.
# Last updated: Tue Oct  1 17:13:16 BST 2013.
import csv

import ryser

def latin_from_file(source, size):
    reader = csv.DictReader(filter(lambda row: row[0]!='#', source), range(size), delimiter=' ')
    row_list = []
    for row in reader:
        row_list.append(row)
    return ryser.designs.Latin(row_list, size = size, format = 'com')

