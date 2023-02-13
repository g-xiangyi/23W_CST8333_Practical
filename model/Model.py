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
from dataclasses import dataclass

# ColumnNames holds the names of each column name in the dataset in a list array
columnNames = (
    'ref_date', 'geo', 'dguid', 'apv', 'uom', 'uom_id', 'scalar_id', 'vtor', 'coord', 'value', 'status', 'sym',
    'terminated',
    'decimals')

# Creating a list to be used to store the dataset; stores the actual values. Each item in the list is a recordObject
# The dataset that the program will be working with is saved in this list - 100 DTOs will be instantiated and then saved
# into this list.
potatoesList = list()


################################
# Creating a Data Transfer Object dataclass object used for transferring data between layers of the application.
# 15 attributes are assigned, 1 for each column header/record attribute with assigned data types.
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

    # Constructor dunder method assigns 15 default values for RecordObject class, 1 for each record attribute
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


################################
# Creating Model class by Amy Guo
class Model:

    # Method creates and saves a new file with the same column headers as the dataset
    # Name of file is input by user.
    @staticmethod
    def save_dataset(dataset_name):
        try:
            with open(dataset_name, mode='w') as csv_file:
                fieldnames = columnNames
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                csv_file.close()
        except Exception as e:
            print('The new dataset {} cannot be created'.format(dataset_name))
            print(e)
            exit(2)

    # Method to create a new record and add it to the working dataset
    @staticmethod
    def create_new_record(new_record):
        potatoesList.append(new_record)

    # Method to update an existing record in the dataset that has been loaded
    @staticmethod
    def update_record(record_index):
        edit_record = potatoesList[record_index - 1]
        print('The {}th record has been selected, and is shown below:'.format(record_index))
        print(edit_record)
        while True:
            key = input('Type name of column to edit:')
            if key == 'ref_date':
                v = int(input('Enter new value for column: '))
                edit_record.ref_date = v

                s = input('Do you want to edit another column (y/n)?')
                if s.upper() == 'N':
                    potatoesList[record_index - 1] = edit_record
                    break

            elif key == 'geo':
                v = int(input('Enter new value for column: '))
                edit_record.geo = v

                s = input('Do you want to edit another column (y/n)?')
                if s.upper() == 'N':
                    potatoesList[record_index - 1] = edit_record
                    break

            elif key == 'dguid':
                v = int(input('Enter new value for column: '))
                edit_record.ref_date = v

                s = input('Do you want to edit another column (y/n)?')
                if s.upper() == 'N':
                    potatoesList[record_index - 1] = edit_record
                    break

            elif key == 'apv':
                v = int(input('Enter new value for column: '))
                edit_record.ref_date = v

                s = input('Do you want to edit another column (y/n)?')
                if s.upper() == 'N':
                    potatoesList[record_index - 1] = edit_record
                    break

            elif key == 'apv':
                v = int(input('Enter new value for column: '))
                edit_record.ref_date = v

                s = input('Do you want to edit another column (y/n)?')
                if s.upper() == 'N':
                    potatoesList[record_index - 1] = edit_record
                    break

            elif key == 'uom':
                v = int(input('Enter new value for column: '))
                edit_record.uom = v

                s = input('Do you want to edit another column (y/n)?')
                if s.upper() == 'N':
                    potatoesList[record_index - 1] = edit_record
                    break

            elif key == 'uom_id':
                v = int(input('Enter new value for column: '))
                edit_record.uom_id = v

                s = input('Do you want to edit another column (y/n)?')
                if s.upper() == 'N':
                    potatoesList[record_index - 1] = edit_record
                    break

            elif key == 'scalar_f':
                v = int(input('Enter new value for column: '))
                edit_record.scalar_f = v

                s = input('Do you want to edit another column (y/n)?')
                if s.upper() == 'N':
                    potatoesList[record_index - 1] = edit_record
                    break

            elif key == 'scalar_id':
                v = int(input('Enter new value for column: '))
                edit_record.ref_date = v

                s = input('Do you want to edit another column (y/n)?')
                if s.upper() == 'N':
                    potatoesList[record_index - 1] = edit_record
                    break

            elif key == 'vtor':
                v = int(input('Enter new value for column: '))
                edit_record.vtor = v

                s = input('Do you want to edit another column (y/n)?')
                if s.upper() == 'N':
                    potatoesList[record_index - 1] = edit_record
                    break

            elif key == 'coord':
                v = int(input('Enter new value for column: '))
                edit_record.coord = v

                s = input('Do you want to edit another column (y/n)?')
                if s.upper() == 'N':
                    potatoesList[record_index - 1] = edit_record
                    break

            elif key == 'value':
                v = int(input('Enter new value for column: '))
                edit_record.value = v

                s = input('Do you want to edit another column (y/n)?')
                if s.upper() == 'N':
                    potatoesList[record_index - 1] = edit_record
                    break

            elif key == 'status':
                v = int(input('Enter new value for column: '))
                edit_record.status = v

                s = input('Do you want to edit another column (y/n)?')
                if s.upper() == 'N':
                    potatoesList[record_index - 1] = edit_record
                    break

            elif key == 'sym':
                v = int(input('Enter new value for column: '))
                edit_record.sym = v

                s = input('Do you want to edit another column (y/n)?')
                if s.upper() == 'N':
                    potatoesList[record_index - 1] = edit_record
                    break

            elif key == 'terminated':
                v = int(input('Enter new value for column: '))
                edit_record.terminated = v

                s = input('Do you want to edit another column (y/n)?')
                if s.upper() == 'N':
                    potatoesList[record_index - 1] = edit_record
                    break

            elif key == 'decimals':
                v = int(input('Enter new value for column: '))
                edit_record.decimals = v

                s = input('Do you want to edit another column (y/n)?')
                if s.upper() == 'N':
                    potatoesList[record_index - 1] = edit_record
                    break

            else:
                print('Invalid column name. Please try again!')

    # Method to delete record
    @staticmethod
    def delete_record(record_index):
        record = potatoesList[record_index - 1]
        del potatoesList[record_index - 1]
        return record


# Method to print author name. Made at the global-level so that it can be called when needed. This method could be
# placed anywhere, but I felt Model was most appropriate since it is presented as application data in the requirements.
# Another place it could be placed is in View.
def print_student_name():
    print('Program written by Amy Guo')
