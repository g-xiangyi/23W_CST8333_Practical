# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

##########################################################
# Print name
def print_student_name():
    print("Done by Amy Guo")

##########################################################
#  Create a record object
recordObject = dict()
column_names = list()

##########################################################
#  Create a list (table) that is used as the dataset
potatoesProduction = list()


#import csv

from model import Model

class View(object):

    @staticmethod
    def show_full_dataset():

        ix_of_print_name = 0
        for item in potatoesProduction:
            print(item)
            ix_of_print_name += 1
            #######################
            # check if need to print student name
            if ix_of_print_name % 10 == 0:
                print_student_name()

#        print('The Dataset size is {}'.format(len(potatoesProduction)))

    @staticmethod
    def show_partial_dataset(start_point, end_point):

        ix = 0
        ix_of_print_name = 0
        for item in potatoesProduction:
            ix += 1
            if ix < start_point:
                continue

            elif ix >= start_point:
                ix_of_print_name += 1
                print(item)
                #######################
                # check if need to print student name
                if ix_of_print_name % 10 == 0:
                    print_student_name()
                if ix == end_point:
                    ix += 1
                    break

    @staticmethod
    def display_load_partial_dataset(file_name, file_size):
        print("Dataset is partially loaded from " + file_name + ' with {} records'.format(file_size))
        print_student_name()

    @staticmethod
    def display_reload_partial_dataset(file_name, file_size):
        print("Dataset is partially reloaded from " + file_name + ' with {} records'.format(file_size))
        print_student_name()

    @staticmethod
    def display_load_dataset(file_name):
        print("Dataset is fully loaded from " + file_name)
        print_student_name()

    @staticmethod
    def display_save_dataset(file_name):
        print('New dataset {} is saved'.format(file_name))
        print_student_name()

    @staticmethod
    def display_insert_record(new_record_item):
        print('A new record (as in the next line):')
        print(new_record_item)
        print('has been created and added to the dataset.')
        print_student_name()

    @staticmethod
    def display_select_edit_record(record_index):
        print('The {}-th record has been edited and shown below'.format(record_index))
        print(potatoesProduction[record_index-1])
        print_student_name()

    @staticmethod
    def display_select_delete_record(record_index, deleted_record):
        print('The {}-th record has been deleted and shown below'.format(record_index))
        print(deleted_record)
        print_student_name()


class Controller(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def load_partial_dataset(self, file_name, file_size):
        self.model.create_dataset_partial(file_name, file_size)
        self.view.display_load_partial_dataset(file_name, file_size)

    def load_full_dataset(self, file_name):
        self.model.create_dataset_in_full(file_name)
        self.view.display_load_dataset(file_name)

    def reload_partial_dataset(self, file_name, file_size):
        potatoesProduction.clear()
        self.model.create_dataset_partial(file_name, file_size)
        self.view.display_reload_partial_dataset(file_name, file_size)

    def reload_full_dataset(self, file_name):
        potatoesProduction.clear()
        self.model.create_dataset_in_full(file_name)

    def show_full_dataset(self):
        self.view.show_full_dataset()

    def show_single_dataset(self, item_index):
        self.view.show_partial_dataset(item_index, item_index)

    def show_multiple_dataset(self, start_point, end_point):
        self.view.show_partial_dataset(start_point, end_point)

    def persist_in_memory_dataset(self, new_dataset_name):
        self.model.save_dataset(new_dataset_name)
        self.view.display_save_dataset(new_dataset_name)

    def insert_record(self, new_record_item):
        self.model.create_new_record(new_record_item)
        self.view.display_insert_record(new_record_item)

    def select_edit_record(self, ix_of_record_to_be_edited):
        self.model.update_record(ix_of_record_to_be_edited)
        self.view.display_select_edit_record(ix_of_record_to_be_edited)

    def select_delete_record(self, ix_of_record_to_be_edited):
        record = self.model.delete_record(ix_of_record_to_be_edited)
        self.view.display_select_delete_record(ix_of_record_to_be_edited, record)


def main():

    # open the dataset
    dataset_name = "32100358.csv"
    size_of_ds = 10

    c = Controller(Model(), View())

    test_load_partial_dataset = True
    if test_load_partial_dataset:
        print("############# test: load partial dataset")
    c.load_partial_dataset(dataset_name, size_of_ds)
    c.show_full_dataset()
    print('The Dataset size is {}'.format(len(potatoesProduction)))

    test_persist_dataset = False
    if test_persist_dataset:
        print("############# test: save dataset")
        new_dataset_name = input("Enter the name of the new dataset(e.g. abc.cvs): ")
        c.persist_in_memory_dataset(new_dataset_name)

    test_reload_dataset = False
    if test_reload_dataset:
        print("############# test: reload dataset")
        size_of_ds = 12
        c.reload_partial_dataset(dataset_name, size_of_ds)
        c.show_full_dataset()

    test_select_show_single_item = False
    if test_select_show_single_item:
        print("############# test: select and show the 3-th record object")
        c.show_single_dataset(3)
        print_student_name()

    test_select_show_multiple_item = False
    if test_select_show_multiple_item:
        print("############# test: select and show the 4th to 6th record objects")
        c.show_multiple_dataset(4, 6)
        print_student_name()

    test_create_a_new_record = True
    if test_create_a_new_record:
        print("############# test: create a new record object and store in the dataset")
        new_record = dict()
        new_record[column_names[0]] = "2022"
        new_record[column_names[1]] = "Ontario"
        new_record[column_names[2]] = "2022A000235"
        new_record[column_names[3]] = "Production, potatoes"
        new_record[column_names[4]] = "Hundredweight"
        new_record[column_names[5]] = "156"
        new_record[column_names[6]] = "thousands"
        new_record[column_names[7]] = "3"
        new_record[column_names[8]] = "v47167"
        new_record[column_names[9]] = "7.3"
        new_record[column_names[10]] = "23456"
        new_record[column_names[11]] = ""
        new_record[column_names[12]] = ""
        new_record[column_names[13]] = ""
        new_record[column_names[14]] = "0"

        c.insert_record(new_record)
        c.view.show_full_dataset()

    test_select_edit_a_record = True

    if test_select_edit_a_record:
        print("############# test: select and edit a record object")
        no_of_record = input(
            'Enter the no. of record to be edited(1:{}): '.format(len(potatoesProduction)))
        ix_of_record_to_be_edited = int(no_of_record)
        assert ix_of_record_to_be_edited > 0
        assert ix_of_record_to_be_edited <= len(potatoesProduction)
        c.select_edit_record(ix_of_record_to_be_edited)
        c.view.show_full_dataset()

    test_select_delete_a_record = False
    if test_select_delete_a_record:
        print("############# test: select and delete a record object")
        no_of_record = input(
            'Enter the no. of record to be deleted(1:{}): '.format(len(potatoesProduction)))
        ix_of_record_to_be_edited = int(no_of_record)
        assert ix_of_record_to_be_edited > 0
        assert ix_of_record_to_be_edited <= len(potatoesProduction)
        c.select_delete_record(ix_of_record_to_be_edited)
        c.view.show_full_dataset()

    print("############# status at the end")
    print('The Dataset size is {} at the end.'.format(len(potatoesProduction)))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

