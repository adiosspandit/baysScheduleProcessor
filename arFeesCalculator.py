import csv
import datetime



inputFile = '/Users/adi/Downloads/all-games.csv'
outputFile = '2019-spring-ar-fees.csv'
gameCountFile = 'ar-game-count.csv'
with open(outputFile, mode='w') as ar_fees:
    game_writer = csv.writer(ar_fees, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    game_writer.writerow(['G', 'Grd', 'D','S','Home','Team','Away','Team',
                              'Game Time','Field','AR1','AR2'])
    with open(inputFile) as csv_file:
        next(csv_file)
        csv_reader = csv.DictReader(csv_file)
        print(csv_reader.fieldnames)
        line_count = 0
        ar_games = {}
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            if row["Game Time"]:
                if row["Grade"] == "5" or row["Grade"] == "6":
                    if row["Sr. Assistant Ref"] in ar_games:
                        ar_games[row["Sr. Assistant Ref"]] = ar_games[row["Sr. Assistant Ref"]] + 1
                    else:
                        ar_games[row["Sr. Assistant Ref"]] = 1

                    if row["Jr. Assistant Ref"] in ar_games:
                        ar_games[row["Jr. Assistant Ref"]] = ar_games[row["Jr. Assistant Ref"]] + 1
                    else:
                        ar_games[row["Jr. Assistant Ref"]] = 1

                    game_writer.writerow([row["Gender"],row["Grade"],row["Division"],row["Section"],'NYSA',
                                          row["Home Team"].split(' ',1)[0],row["Away Organization"].split(' ',1)[0],row["Away Team"].split(' ',1)[0],
                                          row["Game Time"],row["Field"].split(' ',3)[2], row["Sr. Assistant Ref"],
                                          row["Jr. Assistant Ref"]])
with open(gameCountFile, mode='w') as ar_games_file:
    count_writer = csv.writer(ar_games_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    count_writer.writerow(['Assistant Referee', 'Game Count'])
    for ar, gameCount in ar_games.items():
        count_writer.writerow([ar,gameCount])
