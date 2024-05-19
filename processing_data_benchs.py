#!/bin/python3
import os
import sys

if len(sys.argv) != 3:
    print("Please, pass the path_to_data and path_to_csv_result\n" +
        "Using: python3 collect_data_benchs.py path_to_data path_to_csv_result")
    exit(1)

path_to_data = sys.argv[1]
path_to_csv_result = sys.argv[2]

result_log = open(path_to_csv_result, "w")
result_log.write("name,IPC,MPKI,L2C\n")
for root, dir, files in os.walk(path_to_data):
    for file in files:
        result_log.write(file + ",")
        file = open(root + "/" + file, "r")
        lines = file.readlines()
        for line in lines:
            if "CPU 0 cumulative IPC:" in line:
                data = line.split()[4]
                result_log.write(data + ",")
            if "CPU 0 Branch Prediction Accuracy:" in line:
                data = line.split()[7]
                result_log.write(data + ",")
            if "cpu0_L2C TOTAL" in line:
                data = line.split()
                result_log.write(str(int(data[5]) / int(data[3])) + ",")
        result_log.write("\n")
        file.close()

result_log.close()
