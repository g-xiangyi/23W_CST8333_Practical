# ###############################
# # Practical Project Phase 02
# # Amy Guo
# # Student #041024888
# # CST8333 350 Programming Language Research Project
# ################################
#
# ################################
# DataStore class stores data and handles file i-i
# ################################

import csv
# Importing DTO
from model import Model

ds_name = "32100358.csv"
ds_size = 100

#
# def get_records():
#     with open('32100358.csv', newline='') as csvfile:
#         filereader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#         for row in filereader:
