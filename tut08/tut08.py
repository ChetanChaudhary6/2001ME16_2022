#tut8
from platform import python_version
from datetime import datetime
import os

import re
import os
os.system('cls')
start_time = datetime.now()

# Help


def scorecard():

    file = open("Scorecard.txt", "w")

    india = []
    pak = []
    india_ply = ["Rohit", "Rahul", "Kohli", "Suryakumar Yadav", "Karthik", "Hardik Pandya",
                 "Jadeja", "Bhuvneshwar Kumar", "Avesh Khan", "Yuzvendra Chahal", "Arshdeep Singh"]
    pak_ply = ["Babar Azam", "Rizwan", "Fakhar Zaman", "Iftikhar Ahmed", "Khushdil Shah",
               "Asif Ali", "Shadab Khan", "Nawaz", "Naseem Shah", "Haris Rauf", "Dahani"]
    india_bolwer = ['Bhuvneshwar', 'Arshdeep Singh',
                    'Hardik Pandya', 'Avesh Khan', 'Chahal', 'Jadeja']
    pak_bolwer = ['Naseem Shah', 'Shahnawaz Dahani',
                  'Haris Rauf', 'Shadab Khan', 'Mohammad Nawaz']
    f = open("pak_inns1.txt", "r")
    for x in f:
        pak.append(x)

    f = open("india_inns2.txt", "r")
    for x in f:
        india.append(x)

    file.write(f'{"Pakistan Innings  147-10 " } {" (19.5 Ov)" :>85}'+'\n')

    file.write(
        f'{"Batter" :<20}{" ":50}{"R":<10}{"B":<10}{"4S":<10}{"6S":<10}{"SR":>}'+'\n')
    overall_total_pak = 0

    pak_bye = 0
    pak_leg_bye = 0
    pak_wide = 0
    for x in pak_ply:

        play_list = []
        # x="Shadab Khan"
        for p in pak:
            if (re.search(x.split()[0], re.split(',', p)[0])):
                play_list.append(p)

        total_bol = len(play_list)
        bye1 = 0
        leg_bye1 = 0

        wide1 = 0

        SIX = 0
        FOUR = 0
        total_run = 0
        # single=0?
        out_display = "not out"

        for p1 in range(0, len(play_list)):
            p = play_list[p1]

            # print(re.split(",", p, 2)[1],end=" ");
            runs = re.split(",", p, 2)[1]
            if (re.search('!!', runs)):
                continue
            if (re.search("wide", runs)):
                wide1 += 1
            if (re.search("FOUR", p)):
                FOUR += 1
            if (re.search("SIX", p)):
                SIX += 1

            if (re.search("bye", p)):
                bye1 += 1
            if (re.search("leg bey", p)):
                leg_bey1 += 1

            # runs=re.split(",", p, 2)[1]
            runs = re.findall("\d", runs)
            if (runs):
                # print(runs,p,end=" ")
                total_run += int(runs[0])

            # break

        # print(total_run)
        pak_bye += bye1
        pak_leg_bye += leg_bye1
        pak_wide += wide1
        total_run += FOUR*4+SIX*6
        total_bol_played = total_bol-wide1
        overall_total_pak += total_run

        out = re.split(",", play_list[len(play_list)-1], 2)
        # print(total_run)

        if (re.search('out', out[1]) and re.search('!!', out[1])):

            # mod;
            bowler = ""
            out_by = ""
            if (re.search('Caught', out[1])):
                mod = 'c'
            elif (re.search('Lbw', out[1])):
                mod = 'lbw'
            elif (re.search('Bowled', out[1])):
                mod = 'b'

            for f in india_ply:
                if (re.search(f.split()[0], out[1])):
                    out_by = f
                    break
            for f in india_ply:
                if (re.search(f.split()[0], out[0])):
                    bowler = f
                    break

            if (mod == 'c'):
                out_display = mod+" "+out_by+" b "+bowler
            else:
                out_display = mod+" b "+bowler

        sr = round((total_run/total_bol_played)*100, 2)
        file.write(
            f'{x :<20}{out_display:<50}{total_run:<10}{total_bol_played:<10}{FOUR:<10}{SIX:<10}{sr:>}'+'\n')

    file.write(
        f'{"Extras":<90}{pak_leg_bye+pak_wide+pak_bye}(b {pak_bye} ,Lb {pak_leg_bye},w {pak_wide},nb 0,p 0)'+'\n')

    overall_total_pak += pak_leg_bye+pak_wide+pak_bye

    print(overall_total_pak)
    # Fall of Wickets
    Fall_of_Wickets = []

    pak_power_play_runs = 0
    wicket = 0
    run_till_now = 0
    for com in pak:

        if (len(com) == 1):
            continue
        if ((re.search('!!', com)) and (re.search('out', com))):
            out1 = re.split("!!", com, 2)
            batsman = ""

            for p in pak_ply:
                if (re.search(p.split()[0], out1[0])):
                    batsman = p
                    break
            wicket += 1
            overs = re.split("\s", com)[0]
            s2 = str(run_till_now)+"-"+str(wicket) + \
                "( "+batsman+", "+str(overs)+") ,"
            # print(s2);
            Fall_of_Wickets.append(s2)
            continue

        com1 = re.split(",", com, 2)[1]

        if (re.search("wide", com1)):
            run_till_now += 1
        if (re.search("FOUR", com1)):
            run_till_now += 4
        if (re.search("SIX", com1)):
            run_till_now += 6

        if (re.search("bye", com1)):
            run_till_now += 1
        if (re.search("leg bey", com1)):
            run_till_now += 1

            # runs=re.split(",", p, 2)[1]
        runs = re.findall("\d", com1[1])
        if (runs):
            # print(runs,p,end=" ")
            run_till_now += int(runs[0])

        # for power play runs
        if (re.search('5.6 ', com) and re.search('15.6 ', com) == None):
            pak_power_play_runs = run_till_now

    # # print(Fall_of_Wickets)

    file.write(f'{"Totel":<90}{overall_total_pak}({wicket} wkts,19.5 Ov)'+'\n')
    file.write(3*'\n')
    file.writelines("Fall_of_Wickets"+"\n")
    file.write(1*'\n')

    file.writelines(Fall_of_Wickets)
    file.write(3*'\n')

    file.write(
        f'{"Bowler" :<60}{"O":<10}{"M":<10}{"R":<10}{"W":<10}{"NB":<10}{"WD":<10}{"ECO":<5}'+'\n')

    # bolwers comtributions

    for com in india_bolwer:
        bowler_list = []
        # com='Jadeja'
        for p in pak:
            if (re.search(com.split()[0], re.split(',', p, 1)[0])):
                bowler_list.append(p)

        bowler_run = 0
        bowler_wide = 0
        bowler_wicket = 0
        bowler_bye = 0
        bowler_leg_bye = 0
        for p1 in range(0, len(bowler_list)):
            p = bowler_list[p1]
            if ((re.search('!!', p)) and (re.search('out', p))):
                bowler_wicket += 1
                continue

            runs = re.split(",", p, 2)[1]
            if (re.search("wide", runs)):
                bowler_wide += 1
                bowler_run += 1

            if (re.search("FOUR", p)):
                bowler_run += 4
            if (re.search("SIX", p)):
                bowler_run += 6

            runs = re.split(",", p, 2)[1]
            runs = re.findall("\d", runs)
            if (runs):
                # print(runs,p,end=" ")
                bowler_run += int(runs[0])

        bo = (len(bowler_list)-bowler_wide) % 6
        bowler_overs = (len(bowler_list)-bowler_wide)//6
        Eco = round(bowler_run/(bowler_overs+bo/6), 1)
        bowler_overs += bo/10
        file.write(
            f'{com :<60}{bowler_overs:<10}{0:<10}{bowler_run:<10}{bowler_wicket:<10}{"0":<10}{bowler_wide:<10}{Eco:<5}'+'\n')

        # break
    file.write(2*'\n')
    file.write(f'{"Powerplays" :<60}{"Overs":<50}{"Runs":<5}'+'\n')
    file.write(f'{"Mandatory" :<60}{"0.1-6":<50}{pak_power_play_runs}'+'\n')

    file.write(4*'\n')


    file.write(f'{"India Innings  148-5 " } {" (19.4 Ov)" :>85}'+'\n')
    file.write(2*'\n')

    file.write(
        f'{"Batter" :<20}{" ":50}{"R":<10}{"B":<10}{"4S":<10}{"6S":<10}{"SR":>}'+'\n')
    overall_total_ind = 0
    # that playes how unable not play the match
    did_not_play = []

    ind_bye = 0
    ind_leg_bye = 0
    ind_wide = 0
    for x in india_ply:

        play_list = []
        # x="Rohit"
        for p in india:
            if (re.search(x.split()[0], re.split(',', p)[0])):
                play_list.append(p)

        # print(play_list);
        if (len(play_list) == 0):
            did_not_play.append(x)
            did_not_play.append(" ")
            continue

        total_bol = len(play_list)
        bye1 = 0
        leg_bye1 = 0

        wide1 = 0

        SIX = 0
        FOUR = 0
        total_run = 0
        # single=0?
        out_display = "not out"

        for p1 in range(0, len(play_list)):
            p = play_list[p1]

            # print(re.split(",", p, 2)[1],end=" ");
            runs = re.split(",", p, 2)[1]
            if (re.search('!!', runs)):
                continue
            if (re.search("wide", runs) or re.search("wides", runs)):
                wide1 += 1
                # continue
            if (re.search("FOUR", re.split(",", p, 2)[2])):
                FOUR += 1
                if ((re.search("leg bye", re.split(",", p, 2)[1]))):
                    leg_bye1 += 4

                continue
            if (re.search("SIX", p)):
                SIX += 1
                continue

            if (re.search("leg bye", p)):
                leg_bye1 += 1
                continue
            if (re.search("bye", p)):
                bye1 += 1
                continue

            runs = re.findall("\d", runs)
            if (runs):

                total_run += int(runs[0])

        ind_bye += bye1
        ind_leg_bye += leg_bye1
        ind_wide += wide1
        total_run += FOUR*4+SIX*6
        total_bol_played = total_bol-wide1

        out = re.split(",", play_list[len(play_list)-1], 2)
        # print(total_run)

        if (re.search('out', out[1]) and re.search('!!', out[1])):

            # mod;
            bowler = ""
            out_by = ""
            if (re.search('Caught', out[1])):
                mod = 'c'
            elif (re.search('Lbw', out[1])):
                mod = 'lbw'
            elif (re.search('Bowled', out[1])):
                mod = 'b'

            for f in pak_ply:
                if (re.search(f.split()[0], out[1])):
                    out_by = f
                    break
            for f in pak_ply:
                if (re.search(f.split()[0], out[0])):
                    bowler = f
                    break

            if (mod == 'c'):
                out_display = mod+" "+out_by+" b "+bowler
            else:
                out_display = " b "+bowler

        sr = round((total_run/total_bol_played)*100, 2)
        file.write(
            f'{x :<20}{out_display:<50}{total_run:<10}{total_bol_played:<10}{FOUR:<10}{SIX:<10}{sr:>}'+'\n')

    file.write(
        f'{"Extras":<90}{ind_leg_bye+ind_wide+ind_bye+3}(b {ind_bye} ,Lb {ind_leg_bye},w {ind_wide+3},nb 0,p 0)'+'\n')

    Fall_of_Wickets = []

    ind_power_play_runs = 0

    wicket = 0
    run_till_now = 0
    for com in india:

        if (len(com) == 1):
            continue
        if ((re.search('!!', com)) and (re.search('out', com))):
            out1 = re.split("!!", com, 2)
            batsman = ""
            # print(out1)
            # break
            for p in india_ply:
                if (re.search(p.split()[0], out1[0])):
                    batsman = p
                    break
            wicket += 1
            overs = re.split("\s", com)[0]
            s2 = str(run_till_now)+"-"+str(wicket) + \
                "( "+batsman+", "+str(overs)+") ,"
            # print(s2);
            Fall_of_Wickets.append(s2)
            continue

        com1 = re.split(",", com, 3)

        if (re.search("wide", com1[1]) or (re.search("wides", com1[1]))):
            run_till_now += 1
            # continue
        if (re.search("FOUR", com1[1]) or (re.search("leg bye", com1[1]) and (re.search("FOUR", com1[2])))):
            run_till_now += 4
            # print("yes")
            continue
        if (re.search("SIX", com1[1])):
            run_till_now += 6
            continue

        if (re.search("leg bye", com1[1])):
            run_till_now += 1
            continue
        if (re.search("bye", com1[1])):
            run_till_now += 1
            continue

            # runs=re.split(",", p, 2)[1]
        runs = re.findall("\d", re.split(',', com, 2)[1])

        if (runs):
            if (re.search("wide", com1[1])):
                run_till_now += int(runs[0])-1
            else:  # print(runs,p,end=" ")
                run_till_now += int(runs[0])

        if (re.search('5.6 ', com) and re.search('15.6 ', com) == None):
            ind_power_play_runs = run_till_now

    # # print(Fall_of_Wickets)
    total_overs = re.split("\s", india[len(india)-1])[0]
    file.write(
        f'{"Total":<90}{run_till_now}({wicket} wkts,{total_overs})'+'\n')

    file.write(f'{"did not play":<70}')
    file.writelines(did_not_play)

    file.write(3*'\n')
    file.writelines("Fall_of_Wickets"+"\n")
    file.write(1*'\n')

    file.writelines(Fall_of_Wickets)
    file.write(3*'\n')

    file.write(
        f'{"Bowler" :<60}{"O":<10}{"M":<10}{"R":<10}{"W":<10}{"NB":<10}{"WD":<10}{"ECO":<5}'+'\n')

    # # bolwers comtributions

    for com in pak_bolwer:
        bowler_list = []
        # com="Haris Rauf"
        for p in india:
            if (re.search(com.split()[0], re.split(',', p, 1)[0]) or re.search(com.split()[1], re.split(',', p, 1)[0])):
                bowler_list.append(p)

        extra_wide = 0
        # this for in a one wide ball how many runes a playes takes
        bowler_run = 0
        bowler_wide = 0
        bowler_wicket = 0
        bowler_bye = 0
        bowler_leg_bye = 0
        for p1 in range(0, len(bowler_list)):
            p = bowler_list[p1]
            if ((re.search('!!', p)) and (re.search('out', p))):
                bowler_wicket += 1
                continue

            # print(re.split(",", p, 2)[1],end=" ");
            runs = re.split(",", p, 3)[1]
            if (re.search("wide", runs)):
                bowler_wide += 1
                bowler_run += 1

            if (re.search("FOUR", runs)):
                bowler_run += 4
                continue
            if (re.search("SIX", runs)):
                bowler_run += 6
                continue

            # runs=re.split(",", p, 2)[1]
            runs = re.findall("\d", re.split(',', p, 3)[1])

            if (runs):
                if (re.search("wide", re.split(',', p, 3)[1])):
                    extra_wide += 1
                    bowler_run += int(runs[0])-1
                else:
                    bowler_run += int(runs[0])

        bo = (len(bowler_list)-bowler_wide) % 6
        bowler_overs = (len(bowler_list)-bowler_wide)//6
        Eco = round(bowler_run/(bowler_overs+bo/6), 1)
        bowler_overs += bo/10

        # because he took four run with a wide
        if (re.search("Dahani", com)):
            extra_wide += 1

        file.write(
            f'{com :<60}{bowler_overs:<10}{0:<10}{bowler_run:<10}{bowler_wicket:<10}{"0":<10}{bowler_wide+extra_wide:<10}{Eco:<5}'+'\n')

    file.write(2*'\n')
    file.write(f'{"Powerplays" :<60}{"Overs":<50}{"Runs":<5}'+'\n')
    file.write(f'{"Mandatory" :<60}{"0.1-6":<50}{ind_power_play_runs}'+'\n')

    file.close()




# Code
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


scorecard()


# This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
