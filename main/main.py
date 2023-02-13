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

from persistence.DataStore import DataStore
import model.Model
from model.Model import potatoesList, Model
from view.View import View
from controller.Controller import Controller

# Driver method runs entire program
def main():
    # open dataset
    ds_name = "32100358.csv"
    ds_size = 10

    mmodel = Model()
    mview = View()
    mstore = DataStore()

    c = Controller(mmodel, mview, mstore)
    c.method_selector()

    test_create_new_record = True
    if test_create_new_record:
        print("####### Test: Create a new record")
        print(model.Model.columnNames)
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

        c.insert_record(new_record)
        c.cview.show_dataset()

    test_select_edit_record = False
    if test_select_edit_record:
        print('####### Test: Select and edit a record object')
        n_record = input('Enter record number to be edited(1:{}): '.format(len(potatoesList)))
        ix_record_edited = int(n_record)
        assert ix_record_edited > 0
        assert ix_record_edited <= len(potatoesList)
        c.update_record(ix_record_edited)
        c.cview.show_dataset()

    test_select_delete_record = False
    if test_select_delete_record:
        n_record = input('Enter record number to be deleted(1:{}): '.format(len(potatoesList)))
        ix_record_edited = int(n_record)
        assert ix_record_edited > 0
        assert ix_record_edited <= len(potatoesList)
        c.delete_record(ix_record_edited)
        c.cview.show_dataset()

    print('####### End status:')
    print('The dataset size is {}. The program is finished.'.format(len(potatoesList)))


# YOU NEED TO COMMENT THIS!!! Marks which methods to run upon clicking run program
if __name__ == '__main__':
    main()
   # unittest.main()
