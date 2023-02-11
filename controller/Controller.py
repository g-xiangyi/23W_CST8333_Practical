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

# Importing classes
from model.ModelDto import recordObject, columnNames, potatoesList, Model
from view.View import View


# Creating Controller class
class Controller:

    def __init__(self, cmodel, cview):
        self.cmodel = Model()
        self.cview = View()

    # Load partial dataset
    def load_partial_ds(self, file_name, file_size):
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
