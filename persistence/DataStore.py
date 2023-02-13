# ###############################
# # Practical Project Phase 02
# # Amy Guo
# # Student #041024888
# # CST8333 350 Programming Language Research Project
# ################################
#
# ################################
# DataStore class stores data and handles file i-o
# ################################

import csv
# Importing DTO (RecordObject) and DTO storage list (potatoesList)
from model.Model import RecordObject, potatoesList

ds_name = "32100358.csv"
ds_size = 100


# Creating a class to store data accessed from the dataset
class DataStore:
    # Method to create partial dataset (10 records)
    @staticmethod
    def create_dataset_partial(dataset_name, dataset_size):
        try:
            with open(dataset_name, mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)

                # Get columnn names
                loc_columnNames = csv_reader.fieldnames
                line_count = 0

                for row in csv_reader:  # iterate 100 times for 100 rows
                    if line_count == 0:
                        line_count += 1
                    elif line_count > dataset_size:
                        break

                    record_i = RecordObject()
                    record_i.ref_date = int(row[loc_columnNames[0]])
                    record_i.geo = row[loc_columnNames[1]]
                    record_i.dguid = row[loc_columnNames[2]]
                    record_i.apv = row[loc_columnNames[3]]
                    record_i.uom = row[loc_columnNames[4]]
                    record_i.uom_id = int(row[loc_columnNames[5]])
                    record_i.scalar_f = row[loc_columnNames[6]]
                    record_i.scalar_id = int(row[loc_columnNames[7]])
                    record_i.vtor = row[loc_columnNames[8]]
                    record_i.coord = row[loc_columnNames[9]]
                    record_i.value = row[loc_columnNames[10]]
                    record_i.status = row[loc_columnNames[11]]
                    record_i.sym = row[loc_columnNames[12]]
                    record_i.terminated = row[loc_columnNames[13]]
                    record_i.decimals = int(row[loc_columnNames[14]])

                    potatoesList.append(record_i)
                    line_count += 1

                    if line_count > dataset_size:
                        break

        except Exception as e:
            print('The dataset cannot be opened')
            print(e)
            exit(1)
