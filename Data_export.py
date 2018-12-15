import csv
# ... is location file from your computer or notebook.
def read():
    with open('.../Data/Data_Player_Averager.csv') as csvfile:
        print("Start Program.")
        print("Loading.")
        print("Reading data.")
        reader = csv.reader(csvfile)
        pubg = []
        dota2 = []
        csgo = []
        poe = []
        rainbow6 = []
        for row in reader:
            pubg.append([row[0],row[1]])
            dota2.append([row[0],row[2]])
            csgo.append([row[0],row[3]])
            poe.append([row[0],row[4]])
            rainbow6.append([row[0],row[5]])

        print("Reading completed.")
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
    if name == 'pubg':
        writer = csv.writer(open(".../Data/PUBG.csv", 'w',  newline=''))
        for data in game:
            writer.writerow((data))
        print('"PUBG.csv" finished writing')

    if name == 'dota2':
        writer = csv.writer(open(".../Data/DOTA2.csv", 'w',  newline=''))
        for data in game:
            writer.writerow((data))
        print('"DOTA2.csv" finished writing')

    if name == 'csgo':
        writer = csv.writer(open(".../Data/CS_GO.csv", 'w',  newline=''))
        for data in game:
            writer.writerow((data))
        print('"CS_GO.csv" finished writing')

    if name == 'poe':
        writer = csv.writer(open(".../Data/POE.csv", 'w',  newline=''))
        for data in game:
            writer.writerow((data))
        print('"POE.csv" finished writing')

    if name == 'rainbow6':
        writer = csv.writer(open(".../Data/R6.csv", 'w',  newline=''))
        for data in game:
            writer.writerow((data))
        print('"R6.csv" finished writing')
read()
