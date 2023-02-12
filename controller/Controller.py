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
from model.Model import RecordObject, columnNames, potatoesList, Model, print_student_name
from view.View import View


# Creating Controller class
class Controller:

    def __init__(self, cmodel: Model(), cview: View()):
        self.cmodel: Model() = cmodel
        self.cview: View() = cview

    # Load partial dataset
    def load_100_records(self, file_name, file_size):
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
        print('This program demonstrates basic CRUD operations on the 32100358.csv file.')
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
            print('test successful')

        else:
            print('Please input a number from 1 to 6')