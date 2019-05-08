# This is an example of python using an api to get the exact snowfall for given places in the resorts.csv file
# Code will not run successfully because my key has expired for the weatcher api





import requests
import csv

csvRows = []
csvFileObj = open('resorts.csv')
readerObj = (csv.reader(csvFileObj))
for row in readerObj:
    if readerObj.line_num == 1:
        continue
    location = (row[1] + ',' + row[2])
    url = ('https://api.aerisapi.com/winter/snowdepth/' + location + '?client_id=V4dkjnzcNqWNrfuoFOACm&client_secret=9HfGxBzhEC291KUR45CQZN6RKF6DzsxHYH8d56Kf')
    r = requests.get(url)
    j = r.json()
    periods = j['response']['periods']
    snowddepth = periods[0]
    exactsnowdepth = snowddepth['snowDepthIN']
    print(row[0] + ', ' + row[1] + ', ' + row[2] + ' - ' + str(exactsnowdepth))
    csvRows.append({'resorts': row[0], 'depth': exactsnowdepth})

maxi = 0
maxResortName = ''
for row in csvRows:
    if row['depth'] > maxi:
        maxi = row['depth']
        maxResortName = row['resorts']


print('The maximum snow depth is ' + str(max) + ' and it is at this Ski Resort: ' + (maxResortName))