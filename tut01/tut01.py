# tut01 solution
# import pandas as pd and csv module
import csv
import pandas as pd
# read the input file
with open('octant_input.csv','r') as input_file:
    reader=csv.reader(input_file)
# write in output file
    with open('f.csv','w',newline='') as output_file:
        writer=csv.writer(output_file)
        for row in reader:
            writer.writerow(row)