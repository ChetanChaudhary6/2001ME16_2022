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
# making average columns 
for ele in data['V']:
    x=data.at[row_no,"U'=U-Uavg"]=data.at[row_no,'U']-u_avg
    y=data.at[row_no,"U'=U-Vavg"]=data.at[row_no,'V']-v_avg
    z=data.at[row_no,"U'=U-Wavg"]=data.at[row_no,'W']-w_avg
    # check valid octant
    try:
        if x>0:
            if y>0:
                if z>0:
                    data.at[row_no,'Octant']='+1'
                    count_p1=count_p1+1
                else:
                    data.at[row_no,'Octant']="-1"
                    count_n1=count_n1+1
            else:
                if z>0:
                    data.at[row_no,'Octant']='+4'
                    count_p4=count_p4+1
                else:
                    data.at[row_no,'Octant']='-4'
                    count_n4=count_n4+1
        else:
            if y>0:
                if z>0:
                    data.at[row_no,'Octant']='+2'
                    count_p2=count_p2+1
                else:
                    data.at[row_no,'Octant']='-2'
                    count_n2=count_n2+1
            else:
                if z>0:
                    data.at[row_no,'Octant']='+3'
                    count_p3=count_p3+1
                else:
                    data.at[row_no,'Octant']='-3'
                    count_n3=count_n3+1
    except:
        print("Octant can't be created")
    string+=data.at[row_no,'Octant']
    row_no=row_no+1
Octant=data['Octant'].tolist()
length=row_no
dict={'-4':[[0],[0,0]],'-3':[[0],[0,0]],'-2':[[0],[0,0]],'-1':[[0],[0,0]],'+1':[[0],[0,0]],'+2':[[0],[0,0]],'+3':[[0],[0,0]],'+4':[[0],[0,0]]}
#function for longest continuous subarray
def fun(n):
    c=0
    mx=0
    for i in range(length):
        x=data.at[i,'Octant']
        if(x==n):
            c+=1
        else:
            if(mx<c):
                lst=[(i-c)/100,(i-1)/100]
                lst2=[c]
                dict[n][0]=lst2
                dict[n][1]=lst
                for j in range(2,len(dict[n])):
                        dict[n].pop()
            elif(mx==c):
                lst=[(i-c)/100,(i-1)/100]
                dict[n].append(lst)
            mx=max(mx,c)
            c=0
fun('-1')
fun('+1')
fun('-2')
fun('-3')
fun('-4')
fun('+2')
fun('+3')
fun('+4')

j=-4
i=0
k=""
#write the count and length in dataframe
while i<8:
    if(j>0):k='+'+str(j)
    else:k=str(j)
    if(j==0):
        j+=1
        continue
    data.at[i,"Value"]=k
    data.at[i,"Longest Subsequence Length"]=dict[k][0][0]
    data.at[i,"Count"]=len(dict[k])-1
    i+=1
    j+=1
