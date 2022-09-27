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
Octant=data['Octant'].tolist()
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

 #now for different mod range values
count_p1=0
count_n1=0
count_p2=0
count_n2=0
count_p3=0
count_n3=0
count_p4=0
count_n4=0
length=row_no
mod=5000
j=1
curr_p1=1
curr_p2=1
curr_p3=1
curr_p4=1
curr_n1=1
curr_n2=1
curr_n3=1
curr_n4=1
curr_oct=1
cnt=0

for i in range(length):
        x=data.at[i,'Octant']
        if(x==1): count_p1+=1
        elif(x==2): count_p2+=1
        elif(x==3): count_p3+=1
        elif(x==4): count_p4+=1
        elif(x==-1): count_n1+=1
        elif(x==-2): count_n2+=1
        elif(x==-3): count_n3+=1
        elif(x==-4): count_n4+=1
        cnt+=1
        if(cnt==mod or i==length-1):
            cnt=0
            data.at[curr_p1,'1']=count_p1
            data.at[curr_p2,'2']=count_p2
            data.at[curr_p3,'3']=count_p3
            data.at[curr_p4,'4']=count_p4
            data.at[curr_n1,'-1']=count_n1
            data.at[curr_n2,'-2']=count_n2
            data.at[curr_n3,'-3']=count_n3
            data.at[curr_n4,'-4']=count_n4
            if(j==6):
                data.at[curr_oct,'Octant ID']="25001-30000"
            elif(i==4999):
                str1="{} - {}".format(i-mod+1, i+1)
                data.at[curr_oct,'Octant ID']=str1
            else:
                str1="{} - {}".format(i-mod+2, i+1)
                data.at[curr_oct,'Octant ID']=str1
            curr_p1+=1
            curr_p2+=1
            curr_p3+=1
            curr_p4+=1
            curr_n1+=1
            curr_n2+=1
            curr_n3+=1
            curr_n4+=1
            curr_oct+=1

            count_p1=0
            count_n1=0
            count_p2=0
            count_n2=0
            count_p3=0
            count_n3=0
            count_p4=0
            count_n4=0
            j+=1
