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
data=pd.read_csv('f.csv')
# taking average using predefine mean method
u_avg=data['U'].mean()
v_avg=data['V'].mean()
w_avg=data['W'].mean()
# write average on output file
data.at[0,'U_avg']=u_avg
data.at[0,'V_avg']=v_avg
data.at[0,'W_avg']=w_avg
row_no=0