import csv
appids = set()
with open('session.csv', 'rb') as csvfile:
     spamreader = csv.DictReader(csvfile)
     for row in spamreader:
         appid = row['_c1']
         myappidlist = appid.split(',')
         for appid in myappidlist:
         	appids.add(appid)
         devid = row['deviceid']
print(appids)
with open('result.csv', 'wb') as result:
	fieldnames = ['deviceid']
	fieldnames.extend(appids)
	writer = csv.DictWriter(result, fieldnames=fieldnames)
	writer.writeheader()
	with open('session.csv', 'rb') as csvfile:
	     spamreader = csv.DictReader(csvfile)
	     for row in spamreader:
	     	myRow = {}
	        appid = row['_c1']
	        myappidlist = appid.split(',')
	        tempapplist = appids.copy()
	        for appid in myappidlist:
	         	myRow[appid] = 1;
	         	tempapplist.remove(appid)
	        for appid in tempapplist:
	         	myRow[appid] = 0;
	        devid = row['deviceid']
	        myRow['deviceid'] = devid
	        writer.writerow(myRow)