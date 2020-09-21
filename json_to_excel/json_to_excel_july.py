import glob
import json
import objectpath
import datetime
import pandas as pd
import xlsxwriter

import csv
from csv import writer

filenames= glob.glob('C:/Users/i00504285/Desktop/Aditya/files/*.json')   

a = 1
 
def append_list_as_row(file_name, list_of_elem):
    global a    
    csv_writer = 0
    with open(file_name, 'a+', newline= '') as write_obj:
                
            csv_writer = writer(write_obj)
            if a != 0:
                #csv_writer.writerow(['Date', 'EdgeConnctionStatus ', 'PrawnFarm.GlassImpedence_Status', 'PrawnFarm.GlassImpedence_Unit', 'PrawnFarm.GlassImpedence_Value ', 'PrawnFarm.pH_Diagnostic', 'PrawnFarm.pH_NE107Status', 'PrawnFarm.pH_Status','PrawnFarm.pH_Unit','PrawnFarm.pH_Value','PrawnFarm.Temperature_Status','PrawnFarm.Temperature_Unit','PrawnFarm.Temperature_Value','Time','timestamp'])
                a = 0
            csv_writer.writerow(list_of_elem)

def Data_Structure_1():
    load_data['state']['reported']['tags']['PrawnFarm_GlassImpedence_Status'] = load_data['state']['reported']['tags'].pop('PrawnFarm.GlassImpedence_Status')
    load_data['state']['reported']['tags']['PrawnFarm_GlassImpedence_Unit'] = load_data['state']['reported']['tags'].pop('PrawnFarm.GlassImpedence_Unit')
    load_data['state']['reported']['tags']['PrawnFarm_GlassImpedence_Value'] = load_data['state']['reported']['tags'].pop('PrawnFarm.GlassImpedence_Value')
    load_data['state']['reported']['tags']['PrawnFarm_pH_Diagnostic'] = load_data['state']['reported']['tags'].pop('PrawnFarm.pH_Diagnostic')
    load_data['state']['reported']['tags']['PrawnFarm_pH_NE107Status'] = load_data['state']['reported']['tags'].pop('PrawnFarm.pH_NE107Status')
    load_data['state']['reported']['tags']['PrawnFarm_pH_Status'] = load_data['state']['reported']['tags'].pop('PrawnFarm.pH_Status')
    load_data['state']['reported']['tags']['PrawnFarm_pH_Unit'] = load_data['state']['reported']['tags'].pop('PrawnFarm.pH_Unit')
    load_data['state']['reported']['tags']['PrawnFarm_pH_Value'] = load_data['state']['reported']['tags'].pop('PrawnFarm.pH_Value')
    load_data['state']['reported']['tags']['PrawnFarm_Temperature_Status'] = load_data['state']['reported']['tags'].pop('PrawnFarm.Temperature_Status')
    load_data['state']['reported']['tags']['PrawnFarm_Temperature_Unit'] = load_data['state']['reported']['tags'].pop('PrawnFarm.Temperature_Unit')
    load_data['state']['reported']['tags']['PrawnFarm_Temperature_Value'] = load_data['state']['reported']['tags'].pop('PrawnFarm.Temperature_Value')
                        
                                 
    json_tree = objectpath.Tree(load_data['state'])
                
    result_Date = list(json_tree.execute('$..Date'))
    result_EdgeConnctionStatus = list(json_tree.execute('$..EdgeConnctionStatus'))

    result_GlassImpedence_status = list(json_tree.execute('$..PrawnFarm_GlassImpedence_Status'))
    result_GlassImpedence_unit = list(json_tree.execute('$..PrawnFarm_GlassImpedence_Unit'))
    result_GlassImpedence_value = list(json_tree.execute('$..PrawnFarm_GlassImpedence_Value'))
    result_pH_Diagnostic = list(json_tree.execute('$..PrawnFarm_pH_Diagnostic'))                   
    result_pH_NE107Status = list(json_tree.execute('$..PrawnFarm_pH_NE107Status'))
    result_pH_status = list(json_tree.execute('$..PrawnFarm_pH_Status'))
    result_pH_unit = list(json_tree.execute('$..PrawnFarm_pH_Unit'))
    result_pH_value = list(json_tree.execute('$..PrawnFarm_pH_Value'))
    result_Temperature_status = list(json_tree.execute('$..PrawnFarm_Temperature_Status'))
    result_Temperature_unit = list(json_tree.execute('$..PrawnFarm_Temperature_Unit'))
    result_Temparature_value = list(json_tree.execute('$..PrawnFarm_Temperature_Value'))
    result_Time = list(json_tree.execute('$..Time'))
    result_timestamp = list(json_tree.execute('$..timestamp'))
                
    result_timestamp = ([s.replace('T', ' ') for s in result_timestamp])

    result_timestamp = [datetime.datetime.strptime(str(i), '%Y-%m-%d %H:%M:%S.%fZ').strftime('%d-%m-%Y %H:%M:%S.%fZ') for i in result_timestamp]
                    
    #result_timestamp = ([s.replace('Z', '') for s in result_timestamp])

                
    main_result = result_Date + result_EdgeConnctionStatus + result_GlassImpedence_status + result_GlassImpedence_unit + result_GlassImpedence_value + result_pH_Diagnostic + result_pH_NE107Status + result_pH_status + result_pH_unit + result_pH_value + result_Temperature_status + result_Temperature_unit + result_Temparature_value + result_Time + result_timestamp

            
    append_list_as_row('C:/Users/i00504285/Desktop/Aditya/json_to_excel/july_10.2.csv', main_result)
                
    print(main_result)
    print(result_GlassImpedence_value)


def Data_Structure_2():
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


        
    append_list_as_row('C:/Users/i00504285/Desktop/Aditya/json_to_excel/july_10.1.csv', main_result)
    print(result_Health)
    print(main_result)

def Data_Structure_3():
    load_data['state']['reported']['tags']['PrawnFarm_Sensor1_pH_GlassImpedence_Status'] = load_data['state']['reported']['tags'].pop('PrawnFarm_Sensor1_pH.GlassImpedence_Status')
    load_data['state']['reported']['tags']['PrawnFarm_Sensor1_pH_GlassImpedence_Unit'] = load_data['state']['reported']['tags'].pop('PrawnFarm_Sensor1_pH.GlassImpedence_Unit')
    load_data['state']['reported']['tags']['PrawnFarm_Sensor1_pH_GlassImpedence_Value'] = load_data['state']['reported']['tags'].pop('PrawnFarm_Sensor1_pH.GlassImpedence_Value')
    load_data['state']['reported']['tags']['PrawnFarm_Sensor1_pH_pH_Diagnostic'] = load_data['state']['reported']['tags'].pop('PrawnFarm_Sensor1_pH.pH_Diagnostic')
    load_data['state']['reported']['tags']['PrawnFarm_Sensor1_pH_pH_NE107Status'] = load_data['state']['reported']['tags'].pop('PrawnFarm_Sensor1_pH.pH_NE107Status')
    load_data['state']['reported']['tags']['PrawnFarm_Sensor1_pH_pH_Status'] = load_data['state']['reported']['tags'].pop('PrawnFarm_Sensor1_pH.pH_Status')
    load_data['state']['reported']['tags']['PrawnFarm_Sensor1_pH_pH_Unit'] = load_data['state']['reported']['tags'].pop('PrawnFarm_Sensor1_pH.pH_Unit')
    load_data['state']['reported']['tags']['PrawnFarm_Sensor1_pH_pH_Value'] = load_data['state']['reported']['tags'].pop('PrawnFarm_Sensor1_pH.pH_Value')
    load_data['state']['reported']['tags']['PrawnFarm_Sensor1_pH_Temperature_Status'] = load_data['state']['reported']['tags'].pop('PrawnFarm_Sensor1_pH.Temperature_Status')
    load_data['state']['reported']['tags']['PrawnFarm_Sensor1_pH_Temperature_Unit'] = load_data['state']['reported']['tags'].pop('PrawnFarm_Sensor1_pH.Temperature_Unit')
    load_data['state']['reported']['tags']['PrawnFarm_Sensor1_pH_Temperature_Value'] = load_data['state']['reported']['tags'].pop('PrawnFarm_Sensor1_pH.Temperature_Value')
                        
                                 
    json_tree = objectpath.Tree(load_data['state'])
                
    result_Date = list(json_tree.execute('$..Date'))
    result_EdgeConnctionStatus = list(json_tree.execute('$..EdgeConnctionStatus'))

    result_GlassImpedence_status = list(json_tree.execute('$..PrawnFarm_Sensor1_pH_GlassImpedence_Status'))
    result_GlassImpedence_unit = list(json_tree.execute('$..PrawnFarm_Sensor1_pH_GlassImpedence_Unit'))
    result_GlassImpedence_value = list(json_tree.execute('$..PrawnFarm_Sensor1_pH_GlassImpedence_Value'))
    result_pH_Diagnostic = list(json_tree.execute('$..PrawnFarm_Sensor1_pH_pH_Diagnostic'))                   
    result_pH_NE107Status = list(json_tree.execute('$..PrawnFarm_Sensor1_pH_pH_NE107Status'))
    result_pH_status = list(json_tree.execute('$..PrawnFarm_Sensor1_pH_pH_Status'))
    result_pH_unit = list(json_tree.execute('$..PrawnFarm_Sensor1_pH_pH_Unit'))
    result_pH_value = list(json_tree.execute('$..PrawnFarm_Sensor1_pH_pH_Value'))
    result_Temperature_status = list(json_tree.execute('$..PrawnFarm_Sensor1_pH_Temperature_Status'))
    result_Temperature_unit = list(json_tree.execute('$..PrawnFarm_Sensor1_pH_Temperature_Unit'))
    result_Temparature_value = list(json_tree.execute('$..PrawnFarm_Sensor1_pH_Temperature_Value'))
    result_Time = list(json_tree.execute('$..Time'))
    result_timestamp = list(json_tree.execute('$..timestamp'))
                
    result_timestamp = ([s.replace('T', ' ') for s in result_timestamp])

    result_timestamp = [datetime.datetime.strptime(str(i), '%Y-%m-%d %H:%M:%S.%fZ').strftime('%d-%m-%Y %H:%M:%S.%fZ') for i in result_timestamp]
                    
    #result_timestamp = ([s.replace('Z', '') for s in result_timestamp])

                
    main_result = result_Date + result_EdgeConnctionStatus + result_GlassImpedence_status + result_GlassImpedence_unit + result_GlassImpedence_value + result_pH_Diagnostic + result_pH_NE107Status + result_pH_status + result_pH_unit + result_pH_value + result_Temperature_status + result_Temperature_unit + result_Temparature_value + result_Time + result_timestamp

            
    append_list_as_row('C:/Users/i00504285/Desktop/Aditya/json_to_excel/july_10.3.csv', main_result)
                
    print(main_result)
    print(result_GlassImpedence_value)
                    



for file in filenames:
    with open(file, 'r') as f:
        load_data = json.load(f)

        try :
            Data_Structure_1()

        except KeyError:
            try:
                Data_Structure_2()

            except KeyError:
                Data_Structure_3()

    
        
