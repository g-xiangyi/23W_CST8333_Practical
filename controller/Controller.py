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
from model.ModelDto import potatoesList


# Creating Controller class
class Controller(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view

    # Load partial dataset
    def load_partial_ds(self, file_name, file_size):
        self.model.create_dataset_partial(file_name, file_size)
        self.view.view_load_partial_ds(file_name, file_size)

    # Load full dataset
    def load_full_ds(self, file_name):
        self.model.create_dataset(file_name)
        self.view.view_load_ds(file_name)

    # Reload partial dataset
    def reload_partial_ds(self, file_name, file_size):
        potatoesList.clear()
        self.model.create_dataset_partial()

    # Reload full dataset
    def reload_full_ds(self, file_name):
        potatoesList.clear()
        self.model.create_dataset(file_name)

    # Display full dataset
    def show_dataset(self):
        self.view.show_dataset()

    # Show single record
    def show_single_ds(self, item_index):
        self.view.view_load_partial_ds(item_index, item_index)

    # Show a range of data
    def show_range_ds(self, start_point, end_point):
        self.view.show_partial_dataset(start_point, end_point)

    # Persist to memory
    def persist_memory_ds(self, new_ds_name):
        self.model.save_dataset(new_ds_name)
        self.view.view_save_ds(new_ds_name)

    # Insert record
    def insert_record(self, new_record_item):
        self.model.create_new_record(new_record_item)
        self.view.view_insert_record(new_record_item)

    # Update/Edit record
    def update_record(self, ix_update_record):
        self.model.update_record(ix_update_record)
        self.view.view_edit_record(ix_update_record)

    # Delete record
    def delete_record(self, ix_delete_record):
        record = self.model.delete_record(ix_delete_record)
        self.view.view_delete_record(ix_delete_record, record)
