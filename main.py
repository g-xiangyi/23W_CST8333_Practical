# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import model
import view
import control

def main():

    # open the dataset
    dataset_name = "32100358.csv"
    size_of_ds = 10

    c = control.Controller(model.Model(), view.View())

    test_load_partial_dataset = True
    if test_load_partial_dataset:
        print("############# test: load partial dataset")
    c.load_partial_dataset(dataset_name, size_of_ds)
    c.show_full_dataset()
    print('The Dataset size is {}'.format(len(model.potatoesProduction)))

    test_persist_dataset = False
    if test_persist_dataset:
        print("############# test: save dataset")
        new_dataset_name = input("Enter the name of the new dataset(e.g. abc.csv): ")
        c.persist_in_memory_dataset(new_dataset_name)

    test_reload_dataset = True
    if test_reload_dataset:
        print("############# test: reload dataset")
        size_of_ds = 12
        c.reload_partial_dataset(dataset_name, size_of_ds)
        c.show_full_dataset()

    test_select_show_single_item = False
    if test_select_show_single_item:
        print("############# test: select and show the 3-th record object")
        c.show_single_dataset(3)
        view.print_student_name()

    test_select_show_multiple_item = False
    if test_select_show_multiple_item:
        print("############# test: select and show the 4th to 6th record objects")
        c.show_multiple_dataset(4, 6)
        view.print_student_name()

    test_create_a_new_record = False
    if test_create_a_new_record:
        print("############# test: create a new record object and store in the dataset")
        new_record = dict()
        new_record[model.column_names[0]] = "2022"
        new_record[model.column_names[1]] = "Ontario"
        new_record[model.column_names[2]] = "2022A000235"
        new_record[model.column_names[3]] = "Production, potatoes"
        new_record[model.column_names[4]] = "Hundredweight"
        new_record[model.column_names[5]] = "156"
        new_record[model.column_names[6]] = "thousands"
        new_record[model.column_names[7]] = "3"
        new_record[model.column_names[8]] = "v47167"
        new_record[model.column_names[9]] = "7.3"
        new_record[model.column_names[10]] = "23456"
        new_record[model.column_names[11]] = ""
        new_record[model.column_names[12]] = ""
        new_record[model.column_names[13]] = ""
        new_record[model.column_names[14]] = "0"

        c.insert_record(new_record)
        c.view.show_full_dataset()

    test_select_edit_a_record = False

    if test_select_edit_a_record:
        print("############# test: select and edit a record object")
        no_of_record = input(
            'Enter the no. of record to be edited(1:{}): '.format(len(model.potatoesProduction)))
        ix_of_record_to_be_edited = int(no_of_record)
        assert ix_of_record_to_be_edited > 0
        assert ix_of_record_to_be_edited <= len(model.potatoesProduction)
        c.select_edit_record(ix_of_record_to_be_edited)
        c.view.show_full_dataset()

    test_select_delete_a_record = False
    if test_select_delete_a_record:
        print("############# test: select and delete a record object")
        no_of_record = input(
            'Enter the no. of record to be deleted(1:{}): '.format(len(model.potatoesProduction)))
        ix_of_record_to_be_edited = int(no_of_record)
        assert ix_of_record_to_be_edited > 0
        assert ix_of_record_to_be_edited <= len(model.potatoesProduction)
        c.select_delete_record(ix_of_record_to_be_edited)
        c.view.show_full_dataset()

    print("############# status at the end")
    print('The Dataset size is {} at the end.'.format(len(model.potatoesProduction)))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

