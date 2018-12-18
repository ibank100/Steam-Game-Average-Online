
import csv
import pygal
import re

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
        name = "PLAYERUNKNOWN'S BATTLEGROUNDS"
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
        name = "DOTA 2"
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
        name = "COUNTER-STRIKE: GLOBAL OFFENSIVE"
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
        name = 'PATH OF EXILE'
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
        name = 'TOM CLANCY\'S RAINBOW SIX SIEGE'
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
        name = 'ALL GAME LIST'
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
    if 'PLAYERUNKNOWN\'S BATTLEGROUNDS' in name:
        chart_horizontal.render_to_file("C:/Users/Meow Bank/Desktop/project_psit/graph/PLAYERUNKNOWN\'S BATTLEGROUNDS.svg")

    elif 'DOTA 2' in name:
        chart_horizontal.render_to_file("C:/Users/Meow Bank/Desktop/project_psit/graph/DOTA 2.svg")

    elif 'COUNTER-STRIKE: GLOBAL OFFENSIVE' in name:
        chart_horizontal.render_to_file("C:/Users/Meow Bank/Desktop/project_psit/graph/COUNTER-STRIKE GLOBAL OFFENSIVE.svg")

    elif 'PATH OF EXILE' in name:
        chart_horizontal.render_to_file("C:/Users/Meow Bank/Desktop/project_psit/graph/PATH OF EXILE.svg")

    elif 'TOM CLANCY\'S RAINBOW SIX SIEGE' in name:
        chart_horizontal.render_to_file("C:/Users/Meow Bank/Desktop/project_psit/graph/TOM CLANCY\'S RAINBOW SIX SIEGE.svg")

    elif 'ALL GAME LIST' in name:
        chart_horizontal.render_to_file("C:/Users/Meow Bank/Desktop/project_psit/graph/ALL GAME LIST.svg")

    if count != 5:
        count += 1
        main(count)

def pygal_line(all_day, name_game):
    ''' Make HorizontalBar chart from pygal '''
    line_chart = pygal.HorizontalBar()
    line_chart.title = '%s\'s average pre days.' %name_game
    day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for i in range(0,7):
        line_chart.add(day[i], all_day[i])
    return line_chart
main(0)
