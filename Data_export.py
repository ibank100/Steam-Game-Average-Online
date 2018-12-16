import csv # <<< import for reading and writing data.
import time # <<< import for delay time, makes it look more realistic.
# ... is location file from your computer or notebook.

def read():
    ''' Open the csv file and then extract the data into the list. '''
    with open('.../Data/Data_Player_Averager.csv') as csvfile:
        print("Start Program.")
        print("Loading.")
        time.sleep(1)
        print("Reading data.")
        reader = csv.reader(csvfile) # <<< make data from csvfile to list but it's all data.
        pubg = []
        dota2 = []
        csgo = []
        poe = []
        rainbow6 = []
        for row in reader: # <<< make loop to extract the data into the list.
            pubg.append([row[0],row[1],row[2]])
            dota2.append([row[0],row[1],row[3]])
            csgo.append([row[0],row[1],row[4]])
            poe.append([row[0],row[1],row[5]])
            rainbow6.append([row[0],row[1],row[6]])
            time.sleep(0.05)

        print("Reading completed.")
        time.sleep(1)
        print("Start writing data.")
        print("loading.")

        write('pubg', pubg)
        write('dota2', dota2)
        write('csgo', csgo)
        write('poe', poe)
        write('rainbow6', rainbow6)

        print("Writing completed.")
        print("Finish Program.")

def write(name, game):
    ''' get infomation form read function and write to file csv. '''
    if name == 'pubg':
        writer = csv.writer(open(".../Data/PUBG.csv", 'w',  newline=''))
        for data in game:
            writer.writerow((data))
            time.sleep(0.05)
        print('"PUBG.csv" finished writing')

    if name == 'dota2':
        writer = csv.writer(open(".../Data/DOTA2.csv", 'w',  newline=''))
        for data in game:
            writer.writerow((data))
            time.sleep(0.05)
        print('"DOTA2.csv" finished writing')

    if name == 'csgo':
        writer = csv.writer(open(".../Data/CS_GO.csv", 'w',  newline=''))
        for data in game:
            writer.writerow((data))
            time.sleep(0.05)
        print('"CS_GO.csv" finished writing')

    if name == 'poe':
        writer = csv.writer(open(".../Data/POE.csv", 'w',  newline=''))
        for data in game:
            writer.writerow((data))
            time.sleep(0.05)
        print('"POE.csv" finished writing')

    if name == 'rainbow6':
        writer = csv.writer(open(".../Data/R6.csv", 'w',  newline=''))
        for data in game:
            writer.writerow((data))
            time.sleep(0.05)
        print('"R6.csv" finished writing')
read()
