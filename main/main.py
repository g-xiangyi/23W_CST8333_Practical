# ###############################
# # Practical Project Phase 02
# # Amy Guo
# # Student #041024888
# # CST8333 350 Programming Language Research Project
# ################################
#
# ################################
# Main driver method
# ################################
#

import controller.Controller
from model.ModelDto import Model, potatoesList, print_student_name
from view.View import View


# Driver method runs entire program
def main():
    # open dataset
    ds_name = "32100358.csv"
    ds_size = 10

    c = controller.Controller(Model(), View())

    test_load_partial_ds = True
    if test_load_partial_ds:
        print('####### Test: Load partial dataset')
        c.load_partial_ds(ds_name, ds_size)
        c.show_dataset()
        print('The dataset size is {}'.format(len(potatoesList)))

    test_persist_ds = False
    if test_persist_ds:
        print('####### Test: Save dataset')
        new_ds_name = input('Enter name of new dataset (e.g. abc.cvs): ')
        c.persist_memory_ds(new_ds_name)

    test_reload_ds = False
    if test_reload_ds:
        print('####### Test: Reload dataset')
        ds_size = 12
        c.reload_partial_ds(ds_name, ds_size)
        c.show_dataset

    test_select_single_ds = False
    if test_select_single_ds:
        print('####### Test: Select and show the 3rd record object')
        c.show_single_ds(3)
        print_student_name()

    test_select_show_multiple_ds = False
    if test_select_show_multiple_ds:
        print('####### Test: Select and show the 4th to 6th record objects')
        c.show_range_ds(4, 6)
        print_student_name()

    test_create_new_record = True
    if test_create_new_record:
        new_record = dict()
        new_record[column_names[0]] = '2022'
        new_record[column_names[1]] = 'Ontario'
        new_record[column_names[2]] = '2022A000235'
        new_record[column_names[3]] = 'Production, potatoes'
        new_record[column_names[4]] = 'Hundredweight'
        new_record[column_names[5]] = '156'
        new_record[column_names[6]] = 'thousands'
        new_record[column_names[7]] = '3'
        new_record[column_names[8]] = 'v47167'
        new_record[column_names[9]] = '7.3'
        new_record[column_names[10]] = '23456'
        new_record[column_names[11]] = ''
        new_record[column_names[12]] = ''
        new_record[column_names[13]] = ''
        new_record[column_names[14]] = '0'

        c.insert_record(new_record)
        c.view.show_dataset()

    test_select_edit_record = True
    if test_select_edit_record:
        print('####### Test: Select and edit a record object')
        n_record = input('Enter record number to be edited(1:{}): '.format(len(potatoesList)))
        ix_record_edited = int(n_record)
        assert ix_record_edited > 0
        assert ix_record_edited <= len(potatoesList)
        c.update_record(ix_record_edited)
        c.view.show_dataset()

    test_select_delete_record = False
    if test_select_delete_record:
        n_record = input('Enter record number to be deleted(1:{}): '.format(len(potatoesList)))
        ix_record_edited = int(n_record)
        assert ix_record_edited > 0
        assert ix_record_edited <= len(potatoesList)
        c.delete_record(ix_record_edited)
        c.view.show_dataset()

    print('####### End status:')
    print('The dataset size is {}. The program is finished.'.format(len(potatoesList)))


# Press the green button in the gutter to run the script
if __name__ == '__main__':
    main()
