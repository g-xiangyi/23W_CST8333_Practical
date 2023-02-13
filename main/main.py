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

from persistence.DataStore import ds_size, ds_name, DataStore
import model.Model
from model.Model import potatoesList, Model, print_student_name
from view.View import View
from controller.Controller import Controller
import unittest

# Driver method runs entire program
def main():
    # open dataset
    ds_name = "32100358.csv"
    ds_size = 10

    mmodel = Model()
    mview = View()
    mstore = DataStore()
#    mstore.create_dataset_partial(ds_name, ds_size)

    c = Controller(mmodel, mview, mstore)


# THIS MUST BE LOADED BEFORE ANYTHING ELSE IN ORDER TO LOAD THE DATASET
    test_load_partial_ds = True
    if test_load_partial_ds:
        print('####### Test: Load initial dataset')
        c.load_100_records(ds_name, ds_size)
        c.show_dataset()
        print('success')

    c.method_selector()



# YOU NEED TO COMMENT THIS!!! Marks which methods to run upon clicking run program
if __name__ == '__main__':
    main()
   # unittest.main()
