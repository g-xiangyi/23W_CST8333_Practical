# ###############################
# # Practical Project Phase 02
# # Amy Guo
# # Student #041024888
# # CST8333 350 Programming Language Research Project
# ################################
#
# ################################
# # Controller class contains code for Controller portion of MVC
# ################################
#

####################################################################################################################
# TO DOS:
# implement switch case for selecting which operation to do

# Importing classes
from model.Model import recordObject, columnNames, potatoesList, ModelDto, print_student_name
from view.View import View


# Creating Controller class
class Controller:

    def __init__(self, cmodel: ModelDto(), cview: View()):
        self.cmodel: ModelDto() = cmodel
        self.cview: View() = cview

    # Load partial dataset
    def load_partial_ds(self, file_name, file_size):
        self.cmodel.create_dataset_partial(file_name, file_size)
        self.cview.view_load_partial_ds(file_name, file_size)

    # Load full dataset
    def load_full_ds(self, file_name):
        self.cmodel.create_dataset(file_name)
        self.cview.view_load_ds(file_name)

    # Reload partial dataset
    def reload_partial_ds(self, file_name, file_size):
        potatoesList.clear()
        self.cmodel.create_dataset_partial(file_name, file_size)

    # Reload full dataset
    def reload_full_ds(self, file_name):
        potatoesList.clear()
        self.cmodel.create_dataset(file_name)

    # Display full dataset
    def show_dataset(self):
        self.cview.show_dataset()

    # Show single record
    def show_single_ds(self, item_index):
        self.cview.show_partial_dataset(item_index, item_index)

    # Show a range of data
    def show_range_ds(self, start_point, end_point):
        self.cview.show_partial_dataset(start_point, end_point)

    # Persist to memory
    def persist_memory_ds(self, new_ds_name):
        self.cmodel.save_dataset(new_ds_name)
        self.cview.view_save_ds(new_ds_name)

    # Insert record
    def insert_record(self, new_record_item):
        self.cmodel.create_new_record(new_record_item)
        self.cview.view_insert_record(new_record_item)

    # Update/Edit record
    def update_record(self, ix_update_record):
        self.cmodel.update_record(ix_update_record)
        self.cview.view_edit_record(ix_update_record)

    # Delete record
    def delete_record(self, ix_delete_record):
        record = self.cmodel.delete_record(ix_delete_record)
        self.cview.view_delete_record(ix_delete_record, record)

    # Method Selector allows user to select which operation to enact based on user input
    def method_selector(self):
        ds_name = "32100358.csv"
        ds_size = len(potatoesList)
        while True:
            print('This program demonstrates basic CRUD operations on the 32100358.csv file.')
            print('Please ensure file 32100358.csv is filed under the main module to ensure program functionality')
            print('This program offers the following functionalities: ')
            print('Press 1 to reload data from the dataset')
            print('Press 2 to write to a new .csv file')
            print('Press 3 to select records to view')
            print('Press 4 to create and store a new record')
            print('Press 5 to edit an existing record')
            print('Press 6 delete an existing record')
            print_student_name()

            no = input('Please input a number from 1-6 (e.g. \'2\'): ')

            if no == '1':
                print('####### Test: reload data from the dataset')
                ds_size = int(input('How many data records to reload '))
                self.reload_partial_ds(ds_name, ds_size)
                self.show_dataset()

                print('test successful')

                while True:
                    test_again = input('Do another functionality (y/n)? ')
                    if test_again == 'n':
                        exit(0)
                    elif test_again == 'y':
                        break
                    else:
                        print('Choose y/n, please!')

            elif no == '2':
                print('####### Test: write to a new .csv file')
                new_ds_name = input('Enter name of new dataset (e.g. abc.csv): ')
                self.persist_memory_ds(new_ds_name)

                print('test successful')

                while True:
                    test_again = input('Do another functionality (y/n)? ')
                    if test_again == 'n':
                        exit(0)
                    elif test_again == 'y':
                        break
                    else:
                        print('Choose y/n, please!')

            elif no == '3':
                print('####### Test: select records to view')
                while True:
                    start_record = int(input('Enter the start record number of the records block: '))
                    end_record = int(input('Enter the end record number of the records block: '))
                    if 0 < start_record <= end_record <= ds_size:
                        self.show_range_ds(start_record, end_record)
                        print_student_name()

                        print('test successful')
                        break
                    else:
                        print('Invalid start and/or end record numbers! Try again!')

                while True:
                    test_again = input('Do another functionality (y/n)? ')
                    if test_again == 'n':
                        exit(0)
                    elif test_again == 'y':
                        break
                    else:
                        print('Choose y/n, please!')

            elif no == '4':
                print('####### Test: create and store a new record')
                new_record = dict()
                new_record[model.Model.columnNames[0]] = "2022"
                new_record[model.Model.columnNames[1]] = "Ontario"
                new_record[model.Model.columnNames[2]] = "2022A000235"
                new_record[model.Model.columnNames[3]] = "Production, potatoes"
                new_record[model.Model.columnNames[4]] = "Hundredweight"
                new_record[model.Model.columnNames[5]] = "156"
                new_record[model.Model.columnNames[6]] = "thousands"
                new_record[model.Model.columnNames[7]] = "3"
                new_record[model.Model.columnNames[8]] = "v47167"
                new_record[model.Model.columnNames[9]] = "7.3"
                new_record[model.Model.columnNames[10]] = "23456"
                new_record[model.Model.columnNames[11]] = ""
                new_record[model.Model.columnNames[12]] = ""
                new_record[model.Model.columnNames[13]] = ""
                new_record[model.Model.columnNames[14]] = "0"

                self.insert_record(new_record)
                self.cview.show_dataset()

                print('test successful')

                while True:
                    test_again = input('Do another functionality (y/n)? ')
                    if test_again == 'n':
                        exit(0)
                    elif test_again == 'y':
                        break
                    else:
                        print('Choose y/n, please!')

            elif no == '5':
                print('####### Test: edit an existing record')
                while True:
                    n_record = input('Enter record number to be edited(1:{}): '.format(len(potatoesList)))
                    ix_record_edited = int(n_record)
                    if 0 < ix_record_edited <= ds_size:
                        self.update_record(ix_record_edited)
                        self.cview.show_dataset()

                        print('test successful')

                while True:
                    test_again = input('Do another functionality (y/n)? ')
                    if test_again == 'n':
                        exit(0)
                    elif test_again == 'y':
                        break
                    else:
                        print('Choose y/n, please!')


            else:
                print('Please input a number from 1 to 6')
