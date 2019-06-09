import csv
import datetime


saturday = datetime.date(2019,6,8)
sunday = datetime.date(2019,6,9)
inputFile = ''
outputFile = 'june-08-2019-games.csv'
with open(outputFile, mode='w') as weekend_games:
    game_writer = csv.writer(weekend_games, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    game_writer.writerow(['G', 'Grd', 'D','S','Home','Team','Away','Team',
                              'Game Time','Field','Referee','AR1','AR2'])
    with open(inputFile) as csv_file:
        next(csv_file)
        csv_reader = csv.DictReader(csv_file)
        print(csv_reader.fieldnames)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            if row["Game Time"]:
                gameday = datetime.datetime.strptime(row["Game Time"], "%Y-%m-%d %H:%M:%S").date()
                if gameday == saturday or gameday == sunday:
                    game_writer.writerow([row["Gender"],row["Grade"],row["Division"],row["Section"],'NYSA',
                                          row["Home Team"],row["Away Organization"],row["Away Team"],
                                          row["Game Time"],row["Field"], row["Referee"], row["Sr. Assistant Ref"],
                                          row["Jr. Assistant Ref"]])