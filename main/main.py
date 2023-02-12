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
import model.Model
import view.View
import controller.Controller
#from model.Model import columnNames, potatoesList, ModelDto, print_student_name
#from view.View import View
#from controller.Controller import Controller


# Driver method runs entire program
def main():
    # open dataset
    ds_name = "32100358.csv"
    ds_size = 10

    mmodel = model.Model.ModelDto()
    mview = view.View.View()

    c = controller.Controller.Controller(mmodel, mview)

    test_load_partial_ds = True
    if test_load_partial_ds:
        print('####### Test: Load partial dataset')
        c.load_partial_ds(ds_name, ds_size)
        c.show_dataset()
        print('The dataset size is {}'.format(len(model.Model.potatoesList)))

    c.method_selector()


# Press the green button in the gutter to run the script
if __name__ == '__main__':
    main()
