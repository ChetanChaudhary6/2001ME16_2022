# tut01 solution
# import pandas as pd and csv module
import pandas as pd
# read the input file
reader=pd.read_excel('input_octant_transition_identify.xlsx',"Sheet1")
# write in output file
writer=pd.ExcelWriter('out.xlsx',engine="openpyxl")
reader.to_excel('out.xlsx')
data=pd.read_excel('out.xlsx',engine="openpyxl",sheet_name="Sheet1")
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
string=""