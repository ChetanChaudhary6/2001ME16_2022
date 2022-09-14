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
# initializing different octant 
# p1 ->positive 1 
# n1 ->negative 1
count_p1=0
count_n1=0
count_p2=0
count_n2=0
count_p3=0
count_n3=0
count_p4=0
count_n4=0

# making average columns 
for ele in data['V']:
    x=data.at[row_no,"U'=U-Uavg"]=data.at[row_no,'U']-u_avg
    y=data.at[row_no,"U'=U-Vavg"]=data.at[row_no,'V']-v_avg
    z=data.at[row_no,"U'=U-Wavg"]=data.at[row_no,'W']-w_avg
    if x>0:
        if y>0:
            if z>0:
                data.at[row_no,'Octant']=1
                count_p1=count_p1+1
            else:
                data.at[row_no,'Octant']=-1
                count_n1=count_n1+1
        else:
            if z>0:
                data.at[row_no,'Octant']=4
                count_p4=count_p4+1
            else:
                data.at[row_no,'Octant']=-4
                count_n4=count_n4+1
    else:
        if y>0:
            if z>0:
                data.at[row_no,'Octant']=2
                count_p2=count_p2+1
            else:
                data.at[row_no,'Octant']=-2
                count_n2=count_n2+1
        else:
            if z>0:
                data.at[row_no,'Octant']=3
                count_p3=count_p3+1
            else:
                data.at[row_no,'Octant']=-3
                count_n3=count_n3+1
    row_no=row_no+1

    # count of all octant
data.at[0,'Octant ID']='Overall Count'
data.at[0,'1']=count_p1
data.at[0,'-1']=count_n1
data.at[0,'2']=count_p2
data.at[0,'-2']=count_n2
data.at[0,'3']=count_p3
data.at[0,'-3']=count_n3
data.at[0,'4']=count_p4
data.at[0,'-4']=count_n4