# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 15:15:04 2023

@author: juarez
"""
import re
import math
import os
import pathlib
import numpy as np
import pandas as pd
import csv

def frequency_search_indexes(file_to_screen, search_freq):
    file_extension = pathlib.Path(file_to_screen).suffix   
    result = re.search("\.\S\d\S", file_extension)
    # print(f'result is {result}')
    perfect_freq_match = False
    visited_freq_list = []
    recorded_freq_line = []
    if result:        
        line_counter = 0    
        with open(file_to_screen) as csv_file:
            for line in csv_file:
                line_counter+=1
                line_data = re.split('\s+', line)
                if line_data[0] != "":
                    try:
                        visited_freq_list.append(int(float(line_data[0])))
                        recorded_freq_line.append(line_counter)
                        if int(float(line_data[0])) == int(search_freq):
                            perfect_freq_match = True
                            break
                        if int(float(line_data[0])) > int(search_freq):
                            break
                        
                    except:
                        pass
    return visited_freq_list, recorded_freq_line, perfect_freq_match
    

def get_frequency_port_voltage_simulation(file_to_screen, target_frequency, freq_list_dataContainer, recorded_freqeuncy_index, matching_frequency, port_under_test):
    if len(freq_list_dataContainer) > 0 and len(recorded_freqeuncy_index) > 0:
        if matching_frequency == True:
            get_index_freq = recorded_freqeuncy_index[-1]
            get_index_freq = get_index_freq + port_under_test - 1
            index_to_get_the_sim_voltage = (2*(port_under_test - 1)) + 1
            line_counter = 0    
            with open(file_to_screen) as csv_file:
                for line in csv_file:
                    line_counter+=1
                    line_data = re.split('\s+', line)
                    if line_counter == get_index_freq:
                        voltage_simulation_for_port = line_data[index_to_get_the_sim_voltage]
                        return voltage_simulation_for_port
                    
        if matching_frequency == False:
            before_target_frequency = freq_list_dataContainer[-2]
            after_terget_frequency = freq_list_dataContainer[-1]
            before_freq_steps = int(target_frequency) - int(before_target_frequency)
            after_freq_steps =   int(after_terget_frequency) - int(target_frequency)    
            
            if before_freq_steps < after_freq_steps:
                get_index_freq = recorded_freqeuncy_index[-2]
                get_index_freq = get_index_freq + port_under_test - 1
            else:
                get_index_freq = recorded_freqeuncy_index[-1]
                get_index_freq = get_index_freq + port_under_test - 1
            
            index_to_get_the_sim_voltage = (2*(port_under_test - 1)) + 1
            line_counter = 0    
            
            with open(file_to_screen) as csv_file:
                for line in csv_file:
                    line_counter+=1
                    line_data = re.split('\s+', line)
                    
                    if line_counter == get_index_freq:
                        voltage_simulation_for_port = line_data[index_to_get_the_sim_voltage]
                        return voltage_simulation_for_port
                    
                    
# file_to_screen  = r"C:\Users\juarez\OneDrive - Qualcomm\Desktop\ABCD_Method_tool\ABCD_SP_Files\BA528129_ALL_OFF_CT15_ACTIVE_RFFE9_0_1-8_ABCD2VBD_Vpk30dBm_CommMode.s6p"
# search_freq = "900000000"

# freq_list_dataContainer, recorded_freqeuncy_index, matching_frequency = frequency_search_indexes(file_to_screen, search_freq)

# print(freq_list_dataContainer)
# print(recorded_freqeuncy_index)
# print(matching_frequency)

# # #TABLE VALUES
# # ########
# RF1 = 1
# RF2 = 2
# RF3 = 3
# RF4 = 4
# RFC = 5
# RFC_B = 6 
# # ########

# get_voltage_value = get_frequency_port_voltage_simulation(file_to_screen, search_freq, freq_list_dataContainer, recorded_freqeuncy_index, matching_frequency, 1)
# print(f"simulation voltage value {get_voltage_value}")