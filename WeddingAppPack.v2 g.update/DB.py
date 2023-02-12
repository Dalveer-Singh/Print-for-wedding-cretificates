import csv  
import os
import constants as CONST
      
# field names  # dont Change Order of Columns
fields = ['s_no', 'groomName', 'groomFather', 'groomAddress', 'groomId', 'brideName', 'brideFather', 'brideId', 'brideAddress', 'marriageDate', 'print date']

# name of csv file  
filename = "marriage_certificats_record.csv"

def readEntries():
    if not os.path.exists(filename): return
    rows = []
    with open(filename, 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            rows.append(row)
    if len(rows)>0 : rows.pop(0) # removing headder
    return rows

def writeEntry(data):
    # s_no=           data['s_no']
    # groomName=      data['groomName']
    # groomFather=    data['groomFather']
    # groomAddress=   data['groomAddress']
    # groomId=        data['groomId']
    # brideName=      data['brideName']
    # brideFather=    data['brideFather']
    # brideId=        data['brideId']
    # brideAddress=   data['brideAddress']
    # marriageDate=   data['marriageDate']

    row = [data['s_no'], data['groomName'], data['groomFather'], data['groomAddress'], data['groomId'], data['brideName'], data['brideFather'], data['brideId'], data['brideAddress'], data['marriageDate'], CONST.TODAY_DATE]
    rows = [row]

    fileOpenMode = ''
    isWriteHeader = False
    if os.path.exists(filename):
        fileOpenMode = 'ab'
    else:
        fileOpenMode = 'wb'
        isWriteHeader = True

    # with open(filename, 'wb') as outfile:
    #     writer = csv.writer(outfile)
    #     writer.writerows(rows)

    # writing to csv file  
    with open(filename, fileOpenMode) as csvfile:  
        # creating a csv writer object  
        csvwriter = csv.writer(csvfile)  
            
        # writing the fields  
        if isWriteHeader:
            csvwriter.writerow(fields)  
            
        # writing the data rows  
        csvwriter.writerows(rows)

def getLatestSNo():
    rows = readEntries()
    latestSNo = 0;
    for row in rows:
        no = int(row[0])
        if(no>latestSNo): latestSNo = no
    return latestSNo

# print(getLatestSNo());