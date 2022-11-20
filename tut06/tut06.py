import pandas as pd
from datetime import datetime
import openpyxl
start_time = datetime.now()
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import csv
from random import randint
from time import sleep



def send_mail(fromaddr, frompasswd, toaddr, msg_subject, msg_body, file_path):
    try:
        msg = MIMEMultipart()
        print("[+] Message Object Created")
    except:
        print("[-] Error in Creating Message Object")
        return

    msg['From'] = fromaddr

    msg['To'] = toaddr

    msg['Subject'] = msg_subject

    body = msg_body

    msg.attach(MIMEText(body, 'plain'))

    filename = file_path
    attachment = open(filename, "rb")

    p = MIMEBase('application', 'octet-stream')

    p.set_payload((attachment).read())

    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    try:
        msg.attach(p)
        print("[+] File Attached")
    except:
        print("[-] Error in Attaching file")
        return

    try:
        s = smtplib.SMTP('stud.iitp.ac.in', 587)
        print("[+] SMTP Session Created")
    except:
        print("[-] Error in creating SMTP session")
        return

    s.starttls()

    try:
        s.login(fromaddr, frompasswd)
        print("[+] Login Successful")
    except:
        print("[-] Login Failed")

    text = msg.as_string()

    try:
        s.sendmail(fromaddr, toaddr, text)
        print("[+] Mail Sent successfully")
    except:
        print('[-] Mail not sent')

    s.quit()


def isEmail(x):
    if ('@' in x) and ('.' in x):
        return True
    else:
        return False



def main_mail(to):
    FROM_ADDR = "chetan_2001me16@iitp.ac.in"
    FROM_PASSWD = "*****"

    Subject = "CS384 Tutorial 06 submission 2001ME16  "
    Body ='''
    Dear Sir,

    Please find THE attached attendance_consolidated_report.xlsx file.

    Thanking You.
     

    CHETAN CHAUDHARY
    2001ME16
    
    '''
    file_path="output\\attendance_report_consolidated.xlsx"
    if(len(to)==0):
        print("No email address entered")
    else:
       send_mail(FROM_ADDR, FROM_PASSWD, to, Subject, Body, file_path)

def attendance_report():
    
    # Try-except blocks
    # Reading input_attendance.csv file
    try:
        inp_atte = pd.read_csv('input_attendance.csv')
        inp = inp_atte.fillna("2001CCXX Random")
    except:
        print("Error in input attendance file!")

    # Reading input_registered_students.csv file
    try:
        stud=pd.read_csv('input_registered_students.csv')
    except:
        print('Error in input registered file!')

    try:
        all_dates=list()  # Empty list for all dates
        s=sum(1 for row in open("input_registered_students.csv"))
        s_consolidated=sum(1 for row in open("input_attendance.csv"))

        # Splitting timestamp into day, month, year
        for i in range(0,s_consolidated-1):
            day=inp.at[i,'Timestamp'].split()[0].split('-')[0]
            month=inp.at[i,'Timestamp'].split()[0].split('-')[1]
            year=inp.at[i,'Timestamp'].split()[0].split('-')[2]
            date=datetime.strptime(f'{year}-{month}-{day}', "%Y-%m-%d").date()
            day_name=date.strftime("%A")
            if day_name=="Monday" or day_name=="Thursday":    # Checking for Monday and Thursday
                if inp.at[i,'Timestamp'].split()[0] not in all_dates:
                    all_dates.append(inp.at[i,'Timestamp'].split()[0])  # Appending timestamp to list

        report_consolidated=".\output\\attendance_report_consolidated.xlsx"  # path for attendance_report_consolidated.xlsx
    except:
        print("Error in timestamp processing!")

    try:
        out_file=openpyxl.Workbook()
        output=out_file.active
        out_file.save(report_consolidated)
        
        attend_consolidated=pd.read_excel(report_consolidated)
    except:
        print("Error in opening workbook or reading report consolidated!")

    try:
        for i in range(0,s-1):
            total_present=0
            date_index=1
            roll=stud.at[i,'Roll No']
            fileName=".\output\\"+roll+'.xlsx'
            out_file=openpyxl.Workbook()
            output=out_file.active
            out_file.save(fileName)
            df=pd.read_excel(fileName)

            for k in all_dates:
                attendance_duplicate=0
                t_lec_actual,t_lec_fake,t_lec_count=0,0,0
                for j in range(0,s_consolidated-1):
                    if inp.at[j,'Attendance'].split()[0]==roll:
                        if inp.at[j,'Timestamp'].split()[0] == k:
                            t_lec_count+=1
                            time=inp.at[j,'Timestamp'].split()[1]
                            hour=time.split(':')[0]   # getting hour from timestamp
                            minutes=time.split(':')[1] # getting minutes from timestamp
                            if ((hour=='14') or (hour=='15' and minutes=='00')):
                                if t_lec_actual==0:
                                    t_lec_actual+=1
                                else:
                                    attendance_duplicate+=1
                            else:
                                t_lec_fake+=1
                
                # Storing values in df dataframe
                df.at[0,'Roll']=roll
                df.at[0,'Name']=stud.at[i,'Name']
                df.at[date_index,'Dates']=k
                attend_consolidated.at[i+1,'Roll']=roll
                attend_consolidated.at[i+1,'Name']=stud.at[i,'Name']
                df.at[date_index,'Total Attendance Count']=t_lec_count
                attend_consolidated.at[i+1,f'{k}']='P' if t_lec_actual>0 else 'A'
                if t_lec_actual>0: total_present+=1 
                df.at[date_index,'Real']=t_lec_actual
                df.at[date_index,'Duplicate']=attendance_duplicate
                df.at[date_index,'Invalid']= t_lec_fake
                df.at[date_index,'Absent']=1 if t_lec_actual==0 else 0
                date_index+=1
                
            attend_consolidated.at[i+1,'Actual Lecture Taken']=len(all_dates)
            attend_consolidated.at[i+1,'Total Real']=total_present
            attend_consolidated.at[i+1,'% Attendance']=round(total_present/len(all_dates)*100,2)
            df.to_excel(fileName,index=False) # Writing df to fileName
    except:
        print("Error in final output calculations!")
    
    # Writing consolidated dataframe to report_consolidated
    try:
        attend_consolidated.to_excel(report_consolidated,index=False)
    except:
        print("Error in writing output to output file!")



from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


attendance_report()
# Send email code
to="c" # Receiver's address
main_mail(to)



#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))