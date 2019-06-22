import csv
import datetime

SATURDAY = 5;
inputFile = 'all-games.csv'
outputFile = 'session-counts.csv'
with open(outputFile, mode='w') as sessionCounts:
    sessionWriter = csv.writer(sessionCounts, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    sessionWriter.writerow(['Date', 'Count'])
    with open(inputFile) as csv_file:
        next(csv_file)
        csv_reader = csv.DictReader(csv_file)
        print(csv_reader.fieldnames)
        line_count = 0
        mentorSessions = dict()
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            if row["Game Time"]:
                gameDay = datetime.datetime.strptime(row["Game Time"], "%Y-%m-%d %H:%M:%S").date()
                gameTime = datetime.datetime.strptime(row["Game Time"], "%Y-%m-%d %H:%M:%S").time()
                if gameDay.weekday() == SATURDAY:
                    day = gameDay.strftime("%m%d")
                    time = gameTime.strftime("%H%M")
                    dayTime = day + ":" + time
                    if dayTime not in mentorSessions:
                        mentorSessions[dayTime] = 1
                    else:
                        mentorSessions[dayTime] += 1
        for key in mentorSessions:
            date =  key.split(':',2)[0]
            session = key.split(':', 2)[1]
            sessionWriter.writerow([date,session])





