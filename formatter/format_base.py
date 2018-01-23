import csv
import os
import sys
import glob


class Formatter:
    """Used to format the CSV into an easier-to-load format
        Name database provided by Kevin MacLeod"""

    def __init__(self):
        pass

    def format_names(self):
        csv_to_create = {}

        # analyze non-formatted file
        with open("..\\data\\name_db\\names.csv", 'r') as currentFile:
            reader = csv.reader(currentFile, delimiter=',')
            for row in reader:
                if row[1] not in csv_to_create:
                    csv_to_create[row[1]] = [(row[0], row[2])]
                else:
                    csv_to_create[row[1]].append((row[0], row[2])) # update dictionary
            print('Regions:')
            for key in csv_to_create.keys():
                print(key)
        self.create_csv(csv_to_create)
        
    def create_csv(self, name_dict):
        # create csv for each region
        self.delete_old_names() # delete previous names

        for key in name_dict.keys():
            region_multiple = ['African', 'Spanish', 'Indian', 'German', 'French', 'English', 'Gaelic']
            region = key

            if key == '?':
                continue
            for item in region_multiple:
                if item in region:
                    region = self.region_switcher(region)
                    break
                        
            if os.path.exists("..\\data\\names_formatted\\{}_names_formatted.csv".format(key)):
                # add to end of csv
                with open("..\\data\\names_formatted\\{}_names_formatted.csv".format(region), 'a', newline='') as newFile:
                    writer = csv.writer(newFile, delimiter=',', quoting=csv.QUOTE_NONE)
                    for item in name_dict[key]:
                        writer.writerow(item)
                print('Done formatting {} names'.format(key))
            else:
                # create new csv based on region
                with open("..\\data\\names_formatted\\{}_names_formatted.csv".format(region), 'w+', newline='') as newFile:
                    writer = csv.writer(newFile, delimiter=',', quoting=csv.QUOTE_NONE)
                    for item in name_dict[key]:
                        writer.writerow(item)
                print('Done formatting {} names'.format(key))

    def region_switcher(self, region):
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

    def delete_old_names(self):
        files = glob.glob(".\\data\\names_formatted\\*")
        for file in files:
            os.remove(file)


def main():
    format = Formatter()
    format.format_names()


if __name__ == '__main__':
    main()

