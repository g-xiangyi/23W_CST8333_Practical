################################################
#    define the class Controller

import model
import view

class Controller(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def load_partial_dataset(self, file_name, file_size):
        self.model.create_dataset_partial(file_name, file_size)
        self.view.display_load_partial_dataset(file_name, file_size)

    def load_full_dataset(self, file_name):
        self.model.create_dataset_in_full(file_name)
        self.view.display_load_dataset(file_name)

    def reload_partial_dataset(self, file_name, file_size):
        model.potatoesProduction.clear()
        self.model.create_dataset_partial(file_name, file_size)
        self.view.display_reload_partial_dataset(file_name, file_size)

    def reload_full_dataset(self, file_name):
        model.potatoesProduction.clear()
        self.model.create_dataset_in_full(file_name)

    def show_full_dataset(self):
        self.view.show_full_dataset()

    def show_single_dataset(self, item_index):
        self.view.show_partial_dataset(item_index, item_index)

    def show_multiple_dataset(self, start_point, end_point):
        self.view.show_partial_dataset(start_point, end_point)

    def persist_in_memory_dataset(self, new_dataset_name):
        self.model.save_dataset(new_dataset_name)
        self.view.display_save_dataset(new_dataset_name)

    def insert_record(self, new_record_item):
        self.model.create_new_record(new_record_item)
        self.view.display_insert_record(new_record_item)

    def select_edit_record(self, ix_of_record_to_be_edited):
        self.model.update_record(ix_of_record_to_be_edited)
        self.view.display_select_edit_record(ix_of_record_to_be_edited)

    def select_delete_record(self, ix_of_record_to_be_edited):
        record = self.model.delete_record(ix_of_record_to_be_edited)
        self.view.display_select_delete_record(ix_of_record_to_be_edited, record)

