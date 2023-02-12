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
#from model.Model import recordObject, columnNames, potatoesList, ModelDto, print_student_name
#from view.View import View
import model.Model
import view.View

# Creating Controller class
class Controller:

    def __init__(self, cmodel, cview):
        self.cmodel = cmodel
        self.cview = cview

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
        model.Model.potatoesList.clear()
        self.cmodel.create_dataset_partial(file_name, file_size)

    # Reload full dataset
    def reload_full_ds(self, file_name):
        model.Model.potatoesList.clear()
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
        dataset_size = len(model.Model.potatoesList)

        while True:
            print('#########################################################################')
            print('This program demonstrates basic CRUD operations on the 32100358.csv file.')
            print('Please ensure file 32100358.csv is filed under the main module to ensure program functionality')
            print('This program offers the following functionalities: ')
            print('Press 1 to reload data from the dataset')
            print('Press 2 to write to a new .csv file')
            print('Press 3 to select records to view')
            print('Press 4 to create and store a new record')
            print('Press 5 to edit an existing record')
            print('Press 6 delete an existing record')
            view.View.print_student_name()
            no = input('Please input a number from 1-6 (e.g. \'2\'): ')

            if no == '1':
                print('####### Test: Reload dataset')
                ds_name = "32100358.csv"
                ds_size = 12
                self.reload_partial_ds(ds_name, ds_size)
                self.show_dataset()

                test_again = input('Test another functionality (y/n)? ')
                if test_again == "n":
                    view.View.print_student_name()
                    exit(0)

            elif no == '2':
                print('####### Test: Save dataset')
                new_ds_name = input('Enter name of new dataset (e.g. abc.csv): ')
                self.persist_memory_ds(new_ds_name)

                test_again = input('Test another functionality (y/n)? ')
                if test_again == "n":
                    view.View.print_student_name()
                    exit(0)

            elif no == '3':
                print('####### Test: select records to view from the following records')
                self.cview.show_dataset()
                while True:
                    start_record = int(input('Enter the start record number to view: '))
                    end_record = int(input('Enter the start record number to view: '))
                    if 1 <= start_record <= end_record <= dataset_size:
                        self.show_range_ds(start_record, end_record)
                        view.View.print_student_name()

                        test_again = input('Test another functionality (y/n)? ')
                        if test_again == "n":
                            view.View.print_student_name()
                            exit(0)
                        else:
                            break
                    else:
                        print('Invalid numbers. Try again!')

            elif no == '4':
                print("####### Test: Create a new record")
                print('The following is an example:')
                self.show_range_ds(1, 1)
                new_record = dict()
                while True:
                    in_value = input(
                        'Enter the value to {} (e.g. 2022): '.format(model.Model.columnNames[0]))
                    new_record[model.Model.columnNames[0]] = in_value
                    break

                while True:
                    in_value = input(
                        'Enter the value to {} (e.g. Ontario): '.format(model.Model.columnNames[1]))
                    new_record[model.Model.columnNames[1]] = in_value
                    break

                while True:
                    in_value = input(
                        'Enter the value to {} (e.g. 2022A000235): '.format(model.Model.columnNames[2]))
                    new_record[model.Model.columnNames[2]] = in_value
                    break

                while True:
                    in_value = input(
                        'Enter the value to {} (e.g. Production, potatoes): '.format(model.Model.columnNames[3]))
                    new_record[model.Model.columnNames[3]] = in_value
                    break

                while True:
                    in_value = input(
                        'Enter the value to {} (e.g. Hundredweight): '.format(model.Model.columnNames[4]))
                    new_record[model.Model.columnNames[4]] = in_value
                    break

                while True:
                    in_value = input(
                        'Enter the value to {} (e.g. 156): '.format(model.Model.columnNames[5]))
                    new_record[model.Model.columnNames[5]] = in_value
                    break

                while True:
                    in_value = input(
                        'Enter the value to {} (e.g. thousands): '.format(model.Model.columnNames[6]))
                    new_record[model.Model.columnNames[6]] = in_value
                    break

                while True:
                    in_value = input(
                        'Enter the value to {} (e.g. 3): '.format(model.Model.columnNames[7]))
                    new_record[model.Model.columnNames[7]] = in_value
                    break

                new_record[model.Model.columnNames[8]] = "v47167"
                new_record[model.Model.columnNames[9]] = "7.3"
                new_record[model.Model.columnNames[10]] = "23456"
                new_record[model.Model.columnNames[11]] = ""
                new_record[model.Model.columnNames[12]] = ""
                new_record[model.Model.columnNames[13]] = ""
                new_record[model.Model.columnNames[14]] = "0"

                self.insert_record(new_record)
                self.cview.show_dataset()

                test_again = input('Test another functionality (y/n)? ')
                if test_again == "n":
                    view.View.print_student_name()
                    exit(0)

            elif no == '5':
                print('####### Test: Select and edit a record object')
                self.cview.show_dataset()
                while True:
                    n_record = input('Enter record number to be edited(1:{}): '.format(dataset_size))
                    ix_record_edited = int(n_record)
                    if 1 <= ix_record_edited <= dataset_size:
                        self.update_record(ix_record_edited)
                        self.cview.show_dataset()

                        test_again = input('Test another functionality (y/n)? ')
                        if test_again == "n":
                            view.View.print_student_name()
                            exit(0)
                        else:
                            break
                    else:
                        print('Invalid number. Try again!')

            elif no == '6':
                print('####### Test: Select and delete a record object')
                self.cview.show_dataset()
                while True:
                    n_record = input('Enter record number to be deleted(1:{}): '.format(len(model.Model.potatoesList)))
                    ix_record_edited = int(n_record)
                    if 0 < ix_record_edited <= len(model.Model.potatoesList):
                        self.delete_record(ix_record_edited)
                        self.cview.show_dataset()

                        test_again = input('Test another functionality (y/n)? ')
                        if test_again == "n":
                            view.View.print_student_name()
                            exit(0)
                        else:
                            break
                    else:
                        print('Invalid number. Try again!')
            else:
                print('Invalid number!')


