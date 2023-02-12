# ###############################
# # Practical Project Phase 02
# # Amy Guo
# # Student #041024888
# # CST8333 350 Programming Language Research Project
# ################################
#
# ################################
# # View class contains code for View portion of MVC
# ################################
#

# Importing dto
from model.Model import potatoesList


# Creating View class
class View:

    # Method to display full dataset
    @staticmethod
    def show_dataset():

        ix_print_name = 0
        for item in potatoesList:
            print(item)
            ix_print_name += 1
            # Check to see if need to print student name
            if ix_print_name % 10 == 0:
                print_student_name()

    # Method to display partial dataset
    @staticmethod
    def show_partial_dataset(start_point, end_point):
        ix = 0
        ix_print_name = 0
        for item in potatoesList:
            ix += 1
            if ix < start_point:
                continue
            elif ix >= start_point:
                ix_print_name += 1
                print(item)
                # Check to see if need to print student name
                if ix_print_name % 10 == 0:
                    print_student_name()
                if ix == end_point:
                    ix += 1
                    break

    # Load partial dataset
    @staticmethod
    def view_load_partial_ds(file_name, file_size):
        print("Dataset is partially loaded from " + file_name + ' with {} recirds'.format(file_size))
        print_student_name()

    # Reload partial dataset
    @staticmethod
    def view_reload_partial_ds(file_name, file_size):
        print('Dataset is partially reloaded from ' + file_name + ' with {} records'.format(file_size))
        print_student_name()

    # Load full dataset
    @staticmethod
    def view_load_ds(file_name):
        print('Dataset is fully loaded from ' + file_name)
        print_student_name()

    # Save dataset
    @staticmethod
    def view_save_ds(file_name):
        print('Saving dataset {}'.format(file_name))
        print_student_name()

    # Insert record
    @staticmethod
    def view_insert_record(new_record_item):
        print('A new record (shown below) has been created and added to the dataset')
        print(new_record_item)
        print_student_name()

    # Edit record
    @staticmethod
    def view_edit_record(record_index):
        print('The []th record has been edited and is shown below:'.format(record_index))
        print(potatoesList[record_index - 1])
        print_student_name()

    # Delete record
    @staticmethod
    def view_delete_record(record_index, deleted_record):
        print('The []th record shown below has been deleted from the dataset:'.format(record_index))
        print(deleted_record)
        print_student_name()

# Method to print author name
def print_student_name():
    print('Program written by Amy Guo')
