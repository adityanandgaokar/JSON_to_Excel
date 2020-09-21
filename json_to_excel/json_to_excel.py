import glob
import json
import objectpath
import datetime
import pandas as pd
import xlsxwriter

import csv
from csv import writer

filenames= glob.glob('C:/Users/i00504285/Desktop/Aditya/file/*.json')   

a = 1
 
def append_list_as_row(file_name, list_of_elem):
    global a    
    csv_writer = 0
    with open(file_name, 'a+', newline= '') as write_obj:
                
            csv_writer = writer(write_obj)
            if a != 0:
                csv_writer.writerow(['Date', 'EdgeConnctionStatus ', 'Health', 'PVPressure', 'QVTemperature', 'Timestamp', 'Time', 'timestamp'])
                a = 0
            csv_writer.writerow(list_of_elem)

                


for file in filenames:
    with open(file, 'r') as f:
        load_data = json.load(f)
        print(load_data)
        load_data['state']['reported']['tags']['Health'] = load_data['state']['reported']['tags'].pop('PIT.Health')
        load_data['state']['reported']['tags']['PVPressure'] = load_data['state']['reported']['tags'].pop('PIT.PVPressure')
        load_data['state']['reported']['tags']['QVTemperature'] = load_data['state']['reported']['tags'].pop('PIT.QVTemperature')
        load_data['state']['reported']['tags']['Timestamp'] = load_data['state']['reported']['tags'].pop('PIT.Timestamp')
                
        json_tree = objectpath.Tree(load_data['state'])
        
        result_Date = list(json_tree.execute('$..Date'))
        result_Diag = list(json_tree.execute('$..EdgeConnctionStatus'))

        result_Health = list(json_tree.execute('$..Health'))
        result_PVPressure = list(json_tree.execute('$..PVPressure'))
        result_QVTemperature = list(json_tree.execute('$..QVTemperature'))
        result_Timestamp = list(json_tree.execute('$..Timestamp'))                   
        result_Time = list(json_tree.execute('$..Time'))
        result_timestamp = list(json_tree.execute('$..timestamp'))

        result_timestamp = ([s.replace('T', ' ') for s in result_timestamp])

        result_timestamp = [datetime.datetime.strptime(str(i), '%Y-%m-%d %H:%M:%S.%fZ').strftime('%d-%m-%Y %H:%M:%S.%fZ') for i in result_timestamp]
                
        #result_timestamp = ([s.replace('Z', '') for s in result_timestamp])

        
        main_result = result_Date + result_Diag + result_Health + result_PVPressure + result_QVTemperature + result_Timestamp + result_Time + result_timestamp


    
        append_list_as_row('C:/Users/i00504285/Desktop/Aditya/json_to_excel/july_9.1.csv', main_result)
        print(result_Health)
        print(main_result)
