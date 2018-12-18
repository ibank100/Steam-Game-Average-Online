
import csv
import pygal as pg
import re

print("|START PROGRAM|")
print("|>>> Change data into chart <<<|")
print("| 1.) PLAYERUNKNOWN'S BATTLEGROUNDS")
print("| 2.) DOTA 2")
print("| 3.) COUNTER-STRIKE: GLOBAL OFFENSIVE")
print("| 4.) PATH OF EXILE")
print("| 5.) TOM CLANCY'S RAINBOW SIX SIEGE")
print("| 6.) ALL GAME LIST")
print("Loading.")
def main(count):

    monday, mon_count = 0, 0
    tuesday, tue_count = 0, 0
    wednesday, wed_count = 0, 0
    thursday, thu_count = 0, 0
    friday, fri_count = 0, 0
    saturday, sat_count = 0, 0
    sunday, sun_count = 0, 0

    name = ""

    if count == 0:
        print("-----------------------------------------------")
        print("| 1.) PLAYERUNKNOWN'S BATTLEGROUNDS")
        name = "PLAYERUNKNOWN'S BATTLEGROUNDS"
        time.sleep(0.5)
        print("Reading data.")
        with open('C:/Users/Meow Bank/Desktop/project_psit/Data/PUBG.csv') as csvfile:
            pubgfile = csv.reader(csvfile)
            for data in pubgfile:
                if data[1] == 'day':
                    continue
                elif data[1] == 'Mon':
                    monday += int(data[2])
                    mon_count += 1
                elif data[1] == 'Tue':
                    tuesday += int(data[2])
                    tue_count += 1
                elif data[1] == 'Wed':
                    wednesday += int(data[2])
                    wed_count += 1
                elif data[1] == 'Thu':
                    thursday += int(data[2])
                    thu_count += 1
                elif data[1] == 'Fri':
                    friday += int(data[2])
                    fri_count += 1
                elif data[1] == 'Sat':
                    saturday += int(data[2])
                    sat_count += 1
                elif data[1] == 'Sun':
                    sunday += int(data[2])
                    sun_count += 1


    elif count == 1:
        print("-----------------------------------------------")
        print("| 2.) DOTA 2")
        name = "DOTA 2"
        time.sleep(0.5)
        print("Reading data.")
        with open('C:/Users/Meow Bank/Desktop/project_psit/Data/DOTA2.csv') as csvfile:
            dotafile = csv.reader(csvfile)
            for data in dotafile:
                if data[1] == 'day':
                    continue
                elif data[1] == 'Mon':
                    monday += int(data[2])
                    mon_count += 1
                elif data[1] == 'Tue':
                    tuesday += int(data[2])
                    tue_count += 1
                elif data[1] == 'Wed':
                    wednesday += int(data[2])
                    wed_count += 1
                elif data[1] == 'Thu':
                    thursday += int(data[2])
                    thu_count += 1
                elif data[1] == 'Fri':
                    friday += int(data[2])
                    fri_count += 1
                elif data[1] == 'Sat':
                    saturday += int(data[2])
                    sat_count += 1
                elif data[1] == 'Sun':
                    sunday += int(data[2])
                    sun_count += 1

    elif count == 2:
        print("-----------------------------------------------")
        print("| 3.) COUNTER-STRIKE: GLOBAL OFFENSIVE")
        name = "COUNTER-STRIKE: GLOBAL OFFENSIVE"
        time.sleep(0.5)
        print("Reading data.")
        with open('C:/Users/Meow Bank/Desktop/project_psit/Data/CS_GO.csv') as csvfile:
            csgofile = csv.reader(csvfile)
            for data in csgofile:
                if data[1] == 'day':
                    continue
                elif data[1] == 'Mon':
                    monday += int(data[2])
                    mon_count += 1
                elif data[1] == 'Tue':
                    tuesday += int(data[2])
                    tue_count += 1
                elif data[1] == 'Wed':
                    wednesday += int(data[2])
                    wed_count += 1
                elif data[1] == 'Thu':
                    thursday += int(data[2])
                    thu_count += 1
                elif data[1] == 'Fri':
                    friday += int(data[2])
                    fri_count += 1
                elif data[1] == 'Sat':
                    saturday += int(data[2])
                    sat_count += 1
                elif data[1] == 'Sun':
                    sunday += int(data[2])
                    sun_count += 1

    elif count == 3:
        print("-----------------------------------------------")
        print("| 4.) PATH OF EXILE")
        name = 'PATH OF EXILE'
        time.sleep(0.5)
        print("Reading data.")
        with open('C:/Users/Meow Bank/Desktop/project_psit/Data/POE.csv') as csvfile:
            poefile = csv.reader(csvfile)
            for data in poefile:
                if data[1] == 'day':
                    continue
                elif data[1] == 'Mon':
                    monday += int(data[2])
                    mon_count += 1
                elif data[1] == 'Tue':
                    tuesday += int(data[2])
                    tue_count += 1
                elif data[1] == 'Wed':
                    wednesday += int(data[2])
                    wed_count += 1
                elif data[1] == 'Thu':
                    thursday += int(data[2])
                    thu_count += 1
                elif data[1] == 'Fri':
                    friday += int(data[2])
                    fri_count += 1
                elif data[1] == 'Sat':
                    saturday += int(data[2])
                    sat_count += 1
                elif data[1] == 'Sun':
                    sunday += int(data[2])
                    sun_count += 1

    elif count == 4:
        print("-----------------------------------------------")
        print("| 5.) TOM CLANCY'S RAINBOW SIX SIEGE")
        name = 'TOM CLANCY\'S RAINBOW SIX SIEGE'
        time.sleep(0.5)
        print("Reading data.")
        with open('C:/Users/Meow Bank/Desktop/project_psit/Data/R6.csv') as csvfile:
            rsixfile = csv.reader(csvfile)
            for data in rsixfile:
                if data[1] == 'day':
                    continue
                elif data[1] == 'Mon':
                    monday += int(data[2])
                    mon_count += 1
                elif data[1] == 'Tue':
                    tuesday += int(data[2])
                    tue_count += 1
                elif data[1] == 'Wed':
                    wednesday += int(data[2])
                    wed_count += 1
                elif data[1] == 'Thu':
                    thursday += int(data[2])
                    thu_count += 1
                elif data[1] == 'Fri':
                    friday += int(data[2])
                    fri_count += 1
                elif data[1] == 'Sat':
                    saturday += int(data[2])
                    sat_count += 1
                elif data[1] == 'Sun':
                    sunday += int(data[2])
                    sun_count += 1

    elif count == 5:
        print("-----------------------------------------------")
        print("| 6.) ALL GAME LIST")
        name = 'ALL GAME LIST'
        time.sleep(0.5)
        print("Reading data.")
        with open('C:/Users/Meow Bank/Desktop/project_psit/Data/Data_Player_Averager.csv') as csvfile:
            allgamefile = csv.reader(csvfile)
            for data in allgamefile:
                if data[1] == 'day':
                    continue
                elif data[1] == 'Mon':
                    monday += int(data[2])+int(data[3])+int(data[4])+int(data[5])+int(data[6])
                    mon_count += 1
                elif data[1] == 'Tue':
                    tuesday += int(data[2])+int(data[3])+int(data[4])+int(data[5])+int(data[6])
                    tue_count += 1
                elif data[1] == 'Wed':
                    wednesday += int(data[2])+int(data[3])+int(data[4])+int(data[5])+int(data[6])
                    wed_count += 1
                elif data[1] == 'Thu':
                    thursday += int(data[2])+int(data[3])+int(data[4])+int(data[5])+int(data[6])
                    thu_count += 1
                elif data[1] == 'Fri':
                    friday += int(data[2])+int(data[3])+int(data[4])+int(data[5])+int(data[6])
                    fri_count += 1
                elif data[1] == 'Sat':
                    saturday += int(data[2])+int(data[3])+int(data[4])+int(data[5])+int(data[6])
                    sat_count += 1
                elif data[1] == 'Sun':
                    sunday += int(data[2])+int(data[3])+int(data[4])+int(data[5])+int(data[6])
                    sun_count += 1

    print("Reading completed.")

    mon_player = int(monday / mon_count)
    tue_player = int(tuesday / tue_count)
    wed_player = int(wednesday / wed_count)
    thu_player = int(thursday / thu_count)
    fri_player = int(friday / fri_count)
    sat_player = int(saturday / sat_count)
    sun_player = int(sunday / sun_count)


    all_day = [mon_player, tue_player, wed_player, thu_player, fri_player, sat_player, sun_player]
    chart_horizontal = pygal_line(all_day, name)
    name = name + '\' average graph.svg'
    chart_horizontal.render_to_file(name)
    if count != 5:
        count += 1
        main(count)

def pygal_line(all_day, name_game):
    ''' Make HorizontalBar chart from pygal '''
    line_chart = pg.HorizontalBar()
    line_chart.title = '%s\'s average pre days.' %name
    day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for i in range(0,7):
        line_chart.add(day[i], all_day[i])
    return line_chart
main(0)
