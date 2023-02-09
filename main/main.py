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
import model.ModelDto
import view.View

# Driver method runs entire program
def main():

    # open dataset
    ds_name = "32100358.csv"
    ds_size = 10

    c = Controller(Model(), View())

    test_load_partial_ds = True
    if test_load_partial_ds:
        print('####### Test: Load partial dataset')
        c.load_partial_ds(ds_name, ds_size)
        c.show_dataset()
        print('The dataset size is {}'.format(len(potatoesList)))

if __name__ == '__main__':
    main()