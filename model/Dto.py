###############################
# Practical Project Phase 02
# Amy Guo
# Student #041024888
# CST8333 350 Programming Language Research Project
################################

################################
# Creating a record object
recordObject = dict()
columnNames = list()

# Creating a list to be used to store the dataset
potatoesList = list()

################################
# Creating Model class
class Model(object):
    def __init__(self):
    self._item_type='potatoes_production'

    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, new_item_type):
        self._item_type = new_item_type

# Method to create partial dataset (10 records)
    @staticmethod
    def create_dataset_partial(dataset_name, dataset_size):
        try:
            with open(dataset_name, mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)

                # Get columnn names
                global columnNames
                columnNames = csv_reader.fieldnames

                line_count = 0

                for row in csv_reader:
                    if line_count == 0
                        line_count += 1
                    elif line_count > dataset_size:
                        break

                    global recordObject
                    recordObject = row
                    potatoesList.append(recordObject)
                    line_count += 1

        except Exception as e:
            print('The dataset cannot be opened')
            print(e)
            exit(1)

    # Method to create full dataset
    @staticmethod
    def create_dataset(dataset_name):
        try:
            with open(dataset_name, mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)

            # Get column names
            global columnNames
            columnNames = csv_reader.fieldnames
            line_count = 0

            for row in csv_reader:
                if line_count == 0:
                    line_count += 1

                    global recordObject
                    recordObject = row
                    potatoesList.append(recordObject)
                    line_count += 1
                print(line_count)
        except Exception as e:
            print('The dataset cannot be opened')
            print(e)
            exit(1)

    # Method to save dataset
    @staticmethod
    def save_dataset(dataset_name):
        try:
            with open(dataset_name, mode='w') as csv_file:
                fieldNames = columnNames
                writer = csv.DictWriter(csv_file, fieldNames = fieldNames)
                writer.writeheader()
                for row in potatoesList:
                    writer.writerow(row)
                csv_file.close()
        except Exception as e:
            print('The new dataset {} cannot be created'.format(dataset_name))
            print(e)
            exit(2)

    # Method to create record
    @staticmethod
    def create_new_record(newRecord):
        potatoesList.append(newRecord)

    # Method to update record
    @staticmethod
    def update_record(record_index):
        print('The {}th record has been selected, and is shown below:').format(record_index)
        print(potatoesList[record_index-1])
        while True:
            key = input('Type name of column to edit:')
            print(key + ' : ' + potatoesList[record_index-1][key])
            v = input('Enter new value for column: ')
            potatoesList[record_index-1][key] = v

            s = input('Do you want to edit another column (y/n)?')
            if s== 'n':
                break

    # Method to delete record
    @staticmethod
    def delete_record(record_index):
        record = potatoesList[record_index-1]
        del potatoesList[record_index-1]
        return record
