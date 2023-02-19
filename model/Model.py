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
import dataclasses
from collections import namedtuple
from typing import NamedTuple
from dataclasses import dataclass, fields
from operator import itemgetter, attrgetter

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
    scalar_f: str
    scalar_id: int
    vtor: str
    coord: str
    value: str
    status: str
    sym: str
    terminated: str
    decimals: int

    def __init__(self):
        ref_date: int = 1900
        geo: str = 'Canada'
        dguid: str = "2016A000011124"
        apv: str = 'Seeded area, potatoes'
        uom: str = 'Acres'
        uom_id: int = 28
        scalar_f: str = 'units'
        scalar_id: int = 0
        vtor: str = 'v47140'
        coord: str = '1.1'
        value: str = '503600'
        status: str = ''
        sym: str = ''
        terminated: str = ''
        decimals: int = 0


# ColumnNames holds the names of each attribute
columnNames = (
    'ref_date', 'geo', 'dguid', 'apv', 'uom', 'uom_id', 'scalar_id', 'vtor', 'coord', 'value', 'status', 'sym',
    'terminated',
    'decimals')

# columnNames = list()
#RecordObject = dict('RecordObject', columnNames)

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

    # Method to save dataset
    @staticmethod
    def save_dataset(dataset_name):
        try:
            with open(dataset_name, mode='w') as csv_file:
                fieldnames = columnNames
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                # for row in potatoesList:
                #     writer.writerow(row)
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
        edited_record = potatoesList[record_index - 1]
        print(edited_record)
        while True:
            key = input('Type name of column to edit: ')
            edited_filed = fields(RecordObject)
            if columnNames.__contains__(key):
                print('{} = {}'.format(key, getattr(edited_record , key)))
                v = input('Enter new value for column: ')
                if key == 'ref_date' or key == 'uom_id' or key == 'scalar_id' or key == 'decimals':
                    v = int(v)

                setattr(edited_record , key , v)

                s = input('Do you want to edit another column (y/n)?')
                if s == 'n':
                    potatoesList[record_index - 1] = edited_record
                    break

    # Method to delete record
    @staticmethod
    def delete_record(record_index):
        record = potatoesList[record_index - 1]
        del potatoesList[record_index - 1]
        return record

    @staticmethod
    def sort_dataset(sort_keys):
        # perform sorting potatoesList and creating the sorted list
        sorted_dataset = sorted(potatoesList, key=attrgetter(sort_keys))

        # change the potatoesList
        potatoesList.clear()
        for item in sorted_dataset:
            potatoesList.append(item)

# Method to print author name
def print_student_name():
    print('Program written by Amy Guo')
