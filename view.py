##########################################################
# Print name
def print_student_name():
    print("Done by Amy Guo")


#############################################################
#    Define class Viw

from model import potatoesProduction
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

        print('The Dataset size is {}'.format(len(potatoesProduction)))

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
        print(model.potatoesProduction[record_index-1])
        print_student_name()

    @staticmethod
    def display_select_delete_record(record_index, deleted_record):
        print('The {}-th record has been deleted and shown below'.format(record_index))
        print(deleted_record)
        print_student_name()

