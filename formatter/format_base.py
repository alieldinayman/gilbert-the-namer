import csv
import os
import sys
import glob

class Formatter():
    """Used to format the CSV into an easier-to-load format
        Name database provided by Kevin MacLeod"""

    def __init__(self):
        pass

    def FormatNames(self):
        csv_to_create = {}

        #analyze unformatted file
        with open(".\\data\\name_db\\names.csv", 'r') as currentFile:
            reader = csv.reader(currentFile, delimiter=',')
            for row in reader:
                if row[1] not in csv_to_create:
                    csv_to_create[row[1]] = [(row[0], row[2])]
                else:
                    csv_to_create[row[1]].append((row[0], row[2])) #update dictionary
            print('Regions:')
            for key in csv_to_create.keys():
                print(key)
        self.createCSV(csv_to_create)
        
    def createCSV(self, nameDict):
        #create csv for each region
        self.deleteOldNames() #delete previous names

        for key in nameDict.keys():
            region_multiple = ['African', 'Spanish', 'Indian', 'German', 'French', 'English', 'Gaelic']
            region = key

            if (key == '?'):   
                continue
            for item in region_multiple:
                if item in region:
                    region = self.regionSwitcher(region)
                    break
                        
            if os.path.exists(".\\data\\names_formatted\\{}_names_formatted.csv".format(key)):
                with open(".\\data\\names_formatted\\{}_names_formatted.csv".format(region), 'a', newline='') as newFile: #create new csv based on region
                    writer = csv.writer(newFile, delimiter=',', quoting=csv.QUOTE_NONE)
                    for item in nameDict[key]:
                        writer.writerow(item)
                print('Done formatting {} names'.format(key))
            else:
                with open(".\\data\\names_formatted\\{}_names_formatted.csv".format(region), 'w+', newline='') as newFile: #create new csv based on region
                    writer = csv.writer(newFile, delimiter=',', quoting=csv.QUOTE_NONE)
                    for item in nameDict[key]:
                        writer.writerow(item)
                print('Done formatting {} names'.format(key))

    def regionSwitcher(self, region):
        if 'African' in region:
            return 'African'
        if 'Spanish' in region:
            return 'Spanish'
        if 'Indian' in region:
            return 'Indian'
        if 'German' in region:
            return 'German'
        if 'French' in region:
            return 'French'
        if 'English' in region:
            return 'English'
        if 'Gaelic' in region:
            return 'Gaelic'
        return 'none'

    def deleteOldNames(self):
        files = glob.glob(".\\data\\names_formatted\\*")
        for file in files:
            os.remove(file)
                
def main():
    format = Formatter()
    format.FormatNames()

if __name__ == '__main__':
    main()    