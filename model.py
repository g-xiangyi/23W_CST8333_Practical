##########################################################
#  Create a record object
recordObject = dict()
column_names = list()

##########################################################
#  Create a list (table) that is used as the dataset
potatoesProduction = list()

##########################################################
#  Create class Model
import csv

class Model(object):

    def __init__(self):
        self._item_type = 'potatoes_production'

    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, new_item_type):
        self._item_type = new_item_type

    @staticmethod
    def create_dataset_partial(dataset_name, dataset_size):

        try:
            with open(dataset_name, mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)

                #### get the column names
                global column_names
                column_names = csv_reader.fieldnames

                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        line_count += 1
                    elif line_count > dataset_size:
                        break

                    global recordObject
                    recordObject = row
                    global potatoesProduction
                    potatoesProduction.append(recordObject)
                    line_count += 1

        except Exception as e:
            print('The Dateset cannot be opened')
            print(e)
            exit(1)

    @staticmethod
    def create_dataset_in_full(dataset_name):

        try:
            with open(dataset_name, mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)

                #### get the column names
                global column_names
                column_names = csv_reader.fieldnames

                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        line_count += 1

                    global recordObject
                    recordObject = row
                    global potatoesProduction
                    potatoesProduction.append(recordObject)
                    line_count += 1

                print(line_count)
        except Exception as e:
            print('The Dateset cannot be opened')
            print(e)
            exit(1)

    @staticmethod
    def save_dataset(dataset_name):
        try:
            with open(dataset_name, mode='w') as csv_file:
                fieldnames = column_names
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                writer.writeheader()
                global potatoesProduction
                for row in potatoesProduction:
                    writer.writerow(row)

                csv_file.close()

        except Exception as e:
            print('The new dateset {} cannot be created'.format(dataset_name))
            print(e)
            exit(2)

    @staticmethod
    def create_new_record(new_record):
        global potatoesProduction
        potatoesProduction.append(new_record)

    @staticmethod
    def update_record(record_index):
        print('The {}-th record has been selected and shown below'.format(record_index))
        print(potatoesProduction[record_index-1])
        while True:
            key = input('Which column of the record to be edit? ')
            print(key + " : " + potatoesProduction[record_index - 1][key])
            v = input('Enter the new value of the column: ')
            potatoesProduction[record_index - 1][key] = v

            s = input("Do you want to edit another column (y/n)? ")
            if s == "n":
                break

    @staticmethod
    def delete_record(record_index):
        a_record = potatoesProduction[record_index-1]
        del potatoesProduction[record_index-1]
        return a_record

