import csv
import time
print("|START PROGRAM|")
def main():
    print("|>>> INPUT GAME TOPICS <<<|")
    time.sleep(1)
    print("| 1.) PLAYERUNKNOWN'S BATTLEGROUNDS")
    print("| 2.) DOTA 2")
    print("| 3.) COUNTER-STRIKE: GLOBAL OFFENSIVE")
    print("| 4.) PATH OF EXILE")
    print("| 5.) TOM CLANCY'S RAINBOW SIX SIEGE")
    print("| 6.) ALL GAME LIST")
    name = input()
    print("Loading.")
    time.sleep(1)

    monday, mon_count = 0, 0
    tuesday, tue_count = 0, 0
    wednesday, wed_count = 0, 0
    thursday, thu_count = 0, 0
    friday, fri_count = 0, 0
    saturday, sat_count = 0, 0
    sunday, sun_count = 0, 0


    if 'PLAYERUNKNOWN\'S BATTLEGROUNDS' in name.upper() or '1' in name.upper():
        print("-----------------------------------------------")
        print("| 1.) PLAYERUNKNOWN'S BATTLEGROUNDS")
        name = "PLAYERUNKNOWN'S BATTLEGROUNDS"
        time.sleep(0.5)
        print("Reading data.")
        with open('.../Data/PUBG.csv') as csvfile:
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
                time.sleep(0.05)


    elif 'DOTA 2' in name.upper() or '2' in name.upper():
        print("-----------------------------------------------")
        print("| 2.) DOTA 2")
        name = "DOTA 2"
        time.sleep(0.5)
        print("Reading data.")
        with open('.../Data/DOTA2.csv') as csvfile:
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
                time.sleep(0.05)

    elif 'COUNTER-STRIKE: GLOBAL OFFENSIVE' in name.upper() or '3' in name.upper():
        print("-----------------------------------------------")
        print("| 3.) COUNTER-STRIKE: GLOBAL OFFENSIVE")
        name = "COUNTER-STRIKE: GLOBAL OFFENSIVE"
        time.sleep(0.5)
        print("Reading data.")
        with open('.../Data/CS_GO.csv') as csvfile:
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
                time.sleep(0.05)

    elif 'PATH OF EXILE' in name.upper() or '4' in name.upper():
        print("-----------------------------------------------")
        print("| 4.) PATH OF EXILE")
        name = 'PATH OF EXILE'
        time.sleep(0.5)
        print("Reading data.")
        with open('.../Data/POE.csv') as csvfile:
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
                time.sleep(0.05)

    elif 'TOM CLANCY\'S RAINBOW SIX SIEGE' in name.upper() or '5' in name.upper():
        print("-----------------------------------------------")
        print("| 5.) TOM CLANCY'S RAINBOW SIX SIEGE")
        name = 'TOM CLANCY\'S RAINBOW SIX SIEGE'
        time.sleep(0.5)
        print("Reading data.")
        with open('.../Data/R6.csv') as csvfile:
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
                time.sleep(0.05)

    elif 'ALL GAME LIST' in name.upper() or '6' in name.upper():
        print("-----------------------------------------------")
        print("| 6.) ALL GAME LIST")
        name = 'ALL GAME LIST'
        time.sleep(0.5)
        print("Reading data.")
        with open('.../Data/Data_Player_Averager.csv') as csvfile:
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
                time.sleep(0.05)

    else:
        print("-----------------------------------------------")
        print("| 7.) ...")
        time.sleep(2)
        print('| SORRY, PROGRAM CAN\'T READ. PLEASE TRY AGAIN |')
        main()

    print("Reading completed.")
    time.sleep(2)

    mon_player = int(monday / mon_count)
    tue_player = int(tuesday / tue_count)
    wed_player = int(wednesday / wed_count)
    thu_player = int(thursday / thu_count)
    fri_player = int(friday / fri_count)
    sat_player = int(saturday / sat_count)
    sun_player = int(sunday / sun_count)

    all_day = [mon_player, tue_player, wed_player, thu_player, fri_player, sat_player, sun_player]
    show(all_day, name)

def show(all_day, name_game):
    mon_player = all_day[0]
    tue_player = all_day[1]
    wed_player = all_day[2]
    thu_player = all_day[3]
    fri_player = all_day[4]
    sat_player = all_day[5]
    sun_player = all_day[6]
    day = ['mon_player', 'tue_player', 'wed_player', 'thu_player', 'fri_player', 'sat_player', 'sun_player']
    print('|>>> WHAT\'S YOU WANT TO KNOW? <<<|')
    time.sleep(1)
    print('| 1.) MOST PLAYER PLAY GAME ON OCTOBER.')
    print('| 2.) LESS PLAYER PLAY GAME ON OCTOBER.')
    print('| 3.) ALL DAYS PLAYER AVERAGE')
    name = input()
    print("Loading.")
    time.sleep(1)
    print("| %s |" %name_game)

    if 'MOST PLAYER PLAY GAME ON OCTOBER.' in name.upper() or '1' in name.upper():
        max_day = max(mon_player, tue_player, wed_player, thu_player, fri_player, sat_player, sun_player)
        print('%s: %i' %(day[all_day.index(max_day)], max_day))
    elif 'LESS PLAYER PLAY GAME ON OCTOBER.' in name.upper() or '2' in name.upper():
        min_day = min(mon_player, tue_player, wed_player, thu_player, fri_player, sat_player, sun_player)
        print('%s: %i' %(day[all_day.index(mix_day)], min_day))
    elif 'ALL DAYS PLAYER AVERAGE' in name.upper() or '3' in name.upper():
        print("Monday average: %i" %mon_player)
        print("Tuesday average: %i" %tue_player)
        print("Wednesday average: %i" %wed_player)
        print("Thursday average: %i" %thu_player)
        print("Friday average: %i" %fri_player)
        print("Saturday average: %i" %sat_player)
        print("Sunday average: %i" %sun_player)
    else:
        print('| SORRY, PROGRAM CAN\'T READ. PLEASE TRY AGAIN |')
        show(all_day, name)
    time.sleep(3)
main()
print("|END PROGRAM|")
