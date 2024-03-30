import csv
from datetime import date, datetime, timedelta

today = date.today()
delta = timedelta((7 + 5 - today.weekday()) % 7)
saturday = today + delta
sunday = saturday + timedelta(days=1)
inputFile = '/Users/adi/Downloads/game_management_extract.csv'
outputFile = saturday.strftime('%Y-%m-%d') + '-games.csv'
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
                gameday = datetime.strptime(row["Game Time"], "%Y-%m-%d %H:%M:%S").date()
                if gameday == saturday or gameday == sunday:
                    if row["Referee"] == "TBD":
                        row["Referee"] = ""
                    if row["AR #1"] == "TBD":
                        row["AR #1"] = ""
                    if row["AR #2"] == "TBD":
                        row["AR #2"] = ""
                    game_writer.writerow([row["Gender"],row["Grade"],row["Division"],row["Section"],'NYSA',
                                          row["Home Team"].split(' ',1)[0],row["Away Organization"].split(' ',1)[0],
                                          row["Away Team"].split(' ',1)[0],row["Game Time"],row["Field"].split(' ',3)[2],
                                          row["Referee"], row["AR #1"],row["AR #2"]])