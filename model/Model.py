###############################
# Practical Project Phase 02
# Amy Guo
# Student #041024888
# CST8333 350 Programming Language Research Project
################################

################################
# Model class contains data with record object
################################

# Importing csv
import csv
from collections import namedtuple
from typing import NamedTuple
from dataclasses import dataclass


################################
# Creating a record object/Data Transfer Object used for transferring data between layers of the application
@dataclass
class RecordObject:
    ref_date: int
    geo: str
    dguid: str
    apv: str
    uom: str
    uom_id: int
    scalar_id: int
    vtor: str
    coord: str
    value: str
    status: str
    sym: str
    terminated: str
    decimals: int


# ColumnNames holds the names of each attribute
columnNames = (
   'ref_date', 'geo', 'dguid', 'apv', 'uom', 'uom_id', 'scalar_id', 'vtor', 'coord', 'value', 'status', 'sym',
   'terminated',
   'decimals')

#columnNames = list()
# RecordObject = dict('RecordObject', columnNames)

# Creating a list to be used to store the dataset; stores the actual values. Each item in the list is a recordObject
# Save the 100 RecordObject objects into this list!
potatoesList = list()


################################
# Creating Model class
class Model:

    def __init__(self):
        self._item_type = 'potatoes production'

    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, new_item_type):
        self._item_type = new_item_type

    # Method to create partial dataset (10 records)
    @staticmethod
    def create_dataset_partial(dataset_name, dataset_size):
        try:
        #     # Iterate 100 times to save the first 100 records from 32100358.csv into 100 separate RecordObject() objects!
        #     with open(dataset_name, mode='r') as csvfile:
        #         filereader = csv.reader(csvfile)
        #         for row in enumerate(filereader):
        #             record_i = RecordObject(
        #                 ref_date=int(row[0]),
        #                 geo=row[1],
        #                 dguid=row[2],
        #                 apv=row[3],
        #                 uom=row[4],
        #                 uom_id=int(row[5]),
        #                 scalar_id=int(row[6]),
        #                 vtor=row[7],
        #                 coord=row[8],
        #                 value=row[9],
        #                 status=row[10],
        #                 sym=row[11],
        #                 terminated=row[12],
        #                 decimals=int(row[13])
        #             )
        #             potatoesList.append(record_i)
        #             if row == 99:
        #                 pass

            with open(dataset_name, mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)

                # Get columnn names
                global columnNames
                columnNames = csv_reader.fieldnames

                line_count = 0
# Look at this for enumerate() to use as a counter
#         https: // realpython.com / python - enumerate /
                for row in csv_reader:
                    if line_count == 0:
                        line_count += 1
                    elif line_count > dataset_size:
                        break

                    global RecordObject
                    RecordObject = row
                    potatoesList.append(RecordObject)
                    line_count += 1

        except Exception as e:
            print('The dataset cannot be opened')
            print(e)
            exit(1)

    # Method to create full dataset
    @staticmethod
    def create_dataset(dataset_name):
        try:
            with open(dataset_name, mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)

            # Get column names
            # global columnNames
            # columnNames = csv_reader.fieldnames
            line_count = 0

            for row in csv_reader:
                if line_count == 0:
                    line_count += 1

                    global RecordObject
                    RecordObject = row
                    potatoesList.append(RecordObject)
                    line_count += 1
                print(line_count)
        except Exception as e:
            print('The dataset cannot be opened')
            print(e)
            exit(1)

    # Method to save dataset
    @staticmethod
    def save_dataset(dataset_name):
        try:
            with open(dataset_name, mode='w') as csv_file:
                fieldnames = columnNames
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for row in potatoesList:
                    writer.writerow(row)
                csv_file.close()
        except Exception as e:
            print('The new dataset {} cannot be created'.format(dataset_name))
            print(e)
            exit(2)

    # Method to create record
    @staticmethod
    def create_new_record(newRecord):
        potatoesList.append(newRecord)

    # Method to update record
    @staticmethod
    def update_record(record_index):
        print('The {}th record has been selected, and is shown below:'.format(record_index))
        print(potatoesList[record_index - 1])
        while True:
            key = input('Type name of column to edit:')
            print(key + ' : ' + potatoesList[record_index - 1][key])
            v = input('Enter new value for column: ')
            potatoesList[record_index - 1][key] = v

            s = input('Do you want to edit another column (y/n)?')
            if s == 'n':
                break

    # Method to delete record
    @staticmethod
    def delete_record(record_index):
        record = potatoesList[record_index - 1]
        del potatoesList[record_index - 1]
        return record


# Method to print author name
def print_student_name():
    print('Program written by Amy Guo')
