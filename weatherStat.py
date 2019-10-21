import csv 
import re
import datetime

#def getADD(startDate, endDate):
    #make API calls for dates in range
    #for date in range(startDate, endDate)

def parseDateAndDonor(fileString):
    #print("filestring: ", fileString)
    dateStr = re.search(r'(\d{2})_(\d{2})_(\d{4})', fileString)
    donorStr = re.search(r'.*Photo/(.{4}-.{3})_', fileString)
    retDate = ""
    donorID = ""
    

    if(dateStr != None):
        #print(dateStr.group(1), " ", dateStr.group(2), " ",dateStr.group(3), " ")
        retDate = datetime.date(int(dateStr.group(3)),int(dateStr.group(1)),int(dateStr.group(2)))
    if(donorStr != None):
        donorID = donorStr.group(1)
        #print ("donorStr: ", donorStr.group(1))
        #print ("donorStr: ", donorStr)        
        #donorID = 
        
    return retDate, donorID
        #day = re.search(r'')
        #print(m)


def getTagsandDates(filename):  
    # csv file name 
    
    # initializing the titles and rows list 
    fields = [] 
    rows = [] 

    tagMatches = ["maggot", "larvae", "egg mass", "flies", "insect"]
    
    # reading csv file 
    with open(filename, 'r') as csvfile: 
        # creating a csv reader object 
        csvreader = csv.reader(csvfile) 
        
        # extracting field names through first row 
        fields = next(csvreader) 
    
        # extracting each data row one by one 
        for row in csvreader: 
            rows.append(row) 
    
        # get total number of rows 
        print("Total no. of rows: %d"%(csvreader.line_num)) 
    
    # printing the field names 
    print('Field names are:' + ', '.join(field for field in fields)) 
    
    #  printing first 5 rows 
    print('\nFirst 5 rows are:\n') 
    for row in rows[:5]: 
        # parsing each column of a row 
        #print(row[3], " ", row[4])
        #print(type(row[3]))
        # for col in row: 
        #     print("%10s"%col), 
        # print('\n')
        picDate, donorID = parseDateAndDonor(row[3])
        print(picDate)
        print(donorID)
        

def main():
    #for a given dataset
    getTagsandDates(r"tags.csv.20190821")
    

if __name__ == "__main__":
    main()