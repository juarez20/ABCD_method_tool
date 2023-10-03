# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import easygui
import os, decimal
import master_functions_file_ABCD as master_functions
import processing_sNp_files_dEm as processing_sp_files
import pandas as pd
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("ABCD Method Processing Tool")
        MainWindow.resize(880, 415)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.board_ser_label = QtWidgets.QLabel(self.centralwidget)
        self.board_ser_label.setGeometry(QtCore.QRect(40, 20, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.board_ser_label.setFont(font)
        self.board_ser_label.setObjectName("board_ser_label")
        self.board_ser_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.board_ser_entry.setGeometry(QtCore.QRect(40, 70, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.board_ser_entry.setFont(font)
        self.board_ser_entry.setText("")
        self.board_ser_entry.setObjectName("board_ser_entry")
        self.port_selection_label = QtWidgets.QLabel(self.centralwidget)
        self.port_selection_label.setGeometry(QtCore.QRect(250, 20, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.port_selection_label.setFont(font)
        self.port_selection_label.setObjectName("port_selection_label")
        self.port_selection_box = QtWidgets.QComboBox(self.centralwidget)
        self.port_selection_box.setGeometry(QtCore.QRect(250, 70, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.port_selection_box.setFont(font)
        self.port_selection_box.setObjectName("port_selection_box")
        self.port_selection_box.addItem("")
        self.port_selection_box.addItem("")
        self.port_selection_box.addItem("")
        self.port_selection_box.addItem("")
        self.port_selection_box.addItem("")
        self.port_selection_box.addItem("")
        self.band_freq_label = QtWidgets.QLabel(self.centralwidget)
        self.band_freq_label.setGeometry(QtCore.QRect(460, 20, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.band_freq_label.setFont(font)
        self.band_freq_label.setObjectName("band_freq_label")
        self.band_freq_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.band_freq_entry.setGeometry(QtCore.QRect(460, 70, 120, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.band_freq_entry.setFont(font)
        self.band_freq_entry.setText("")
        self.band_freq_entry.setObjectName("band_freq_entry")
        self.data_matrix_label = QtWidgets.QLabel(self.centralwidget)
        self.data_matrix_label.setGeometry(QtCore.QRect(40, 130, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.data_matrix_label.setFont(font)
        self.data_matrix_label.setObjectName("data_matrix_label")
        self.data_matrix_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.data_matrix_entry.setGeometry(QtCore.QRect(40, 170, 771, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.data_matrix_entry.setFont(font)
        self.data_matrix_entry.setObjectName("data_matrix_entry")
        self.data_matrix_search = QtWidgets.QToolButton(self.centralwidget)
        self.data_matrix_search.setGeometry(QtCore.QRect(820, 170, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(21)
        self.data_matrix_search.setFont(font)
        self.data_matrix_search.setObjectName("data_matrix_search")
        self.save_path_label = QtWidgets.QLabel(self.centralwidget)
        self.save_path_label.setGeometry(QtCore.QRect(40, 230, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.save_path_label.setFont(font)
        self.save_path_label.setObjectName("save_path_label")
        self.save_path_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.save_path_entry.setGeometry(QtCore.QRect(40, 280, 771, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.save_path_entry.setFont(font)
        self.save_path_entry.setObjectName("save_path_entry")
        self.processing_data_button = QtWidgets.QPushButton(self.centralwidget)
        self.processing_data_button.setGeometry(QtCore.QRect(670, 350, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.processing_data_button.setFont(font)
        self.processing_data_button.setObjectName("processing_data_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 886, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.data_matrix_search.clicked.connect(self.open_abcd_data_file)
        self.processing_data_button.clicked.connect(self.processing_data_files)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ABCD Processing Data Tool"))
        self.board_ser_label.setText(_translate("MainWindow", "Board/Serial Number"))
        self.port_selection_label.setText(_translate("MainWindow", "Port Number Selection"))
        self.band_freq_label.setText(_translate("MainWindow", "Frequency (Mhz)"))
        self.port_selection_box.setItemText(0, _translate("MainWindow", "RF1"))
        self.port_selection_box.setItemText(1, _translate("MainWindow", "RF2"))
        self.port_selection_box.setItemText(2, _translate("MainWindow", "RF3"))
        self.port_selection_box.setItemText(3, _translate("MainWindow", "RF4"))
        self.port_selection_box.setItemText(4, _translate("MainWindow", "RF5"))
        self.port_selection_box.setItemText(5, _translate("MainWindow", "RF6"))
        self.data_matrix_label.setText(_translate("MainWindow", "ABCD File - Data File Matrix File"))
        self.data_matrix_search.setText(_translate("MainWindow", "..."))
        self.save_path_label.setText(_translate("MainWindow", "Save Data Path"))
        self.processing_data_button.setText(_translate("MainWindow", "Process Data"))
        
    
    def open_abcd_data_file(self):
        data_matrix_file = easygui.fileopenbox(None, title="Select Data Matrix File", default='*', filetypes=["*"])
        if data_matrix_file == None:
            pass
        else:
            self.data_matrix_entry.setText(data_matrix_file)    
    
    
    def converting_freq_entry_to_match_hz_baseline(self, freq_value):
        if "." in str(freq_value):        
            how_many_decimals = decimal.Decimal(str(freq_value))
            how_many_decimals =abs(how_many_decimals.as_tuple().exponent)
        
            freq_value = str(freq_value)
            freq_value = freq_value.replace(".", "")
            freq_value = str(freq_value.ljust(6-int(how_many_decimals) + len(freq_value), '0'))
            
            return freq_value
        else:
            freq_value = str(freq_value) + "000000"
            
            return freq_value
    
    
    def processing_data_files(self):
        get_board_serial_number = self.board_ser_entry.text()
        get_port_selection_number = self.port_selection_box.currentIndex()
        get_RF_port_format = self.port_selection_box.currentText()
        get_freq_band_in_MHZ = self.band_freq_entry.text()
        get_data_matrix_file = self.data_matrix_entry.text()
        get_data_saving_path = self.save_path_entry.text()
                
        search_freq = self.converting_freq_entry_to_match_hz_baseline(get_freq_band_in_MHZ)
        
        
        if len(get_board_serial_number) <= 0 or len(get_data_matrix_file) <= 0 or len(get_data_saving_path)<= 0:
            print("You are missing one or more of the conditions and cannot continue")
        else:
            #Extract the conditions from the matrix data file.
            start_time = time.time()
            get_data_master_container_list = master_functions.build_data_container_from_matrix_file(get_data_matrix_file)
            
            buffer_abcd_sp_file_data_container = []
            buffer_freq_simulation_voltage_data_container = []
            
            for each_data_holder in get_data_master_container_list:
                state_value = each_data_holder[0]
                abcd_sp_file = each_data_holder[1]
                rfbd_datalog = each_data_holder[2]
                
                is_abcd_sp_file_a_path = os.path.exists(abcd_sp_file)
                is_rfbd_datalog_a_path = os.path.exists(rfbd_datalog)
                
                if is_abcd_sp_file_a_path == True and is_rfbd_datalog_a_path == True:
                    if abcd_sp_file not in buffer_abcd_sp_file_data_container:
                        buffer_abcd_sp_file_data_container.append(abcd_sp_file)
                        freq_list_dataContainer, recorded_freqeuncy_index, matching_frequency = processing_sp_files.frequency_search_indexes(abcd_sp_file, search_freq)
                        get_voltage_value = processing_sp_files.get_frequency_port_voltage_simulation(abcd_sp_file, search_freq, freq_list_dataContainer, recorded_freqeuncy_index, matching_frequency, get_port_selection_number+1)
                        buffer_freq_simulation_voltage_data_container.append(get_voltage_value)
                        
                    else:
                       index_value_of_file =  buffer_abcd_sp_file_data_container.index(abcd_sp_file)
                       get_voltage_value = buffer_freq_simulation_voltage_data_container[index_value_of_file]
                       
                    pow_incident, third_harmonics, ivio_at_beginning, ivio_before_breakdown = master_functions.get_csv_file_to_extract_data_conditions(rfbd_datalog)
                    
                    # =============================================================================
                    # Perfoming ABCD Method Calculation
                    # =============================================================================
                    vbd_calculated_value = 0
                    vbd_calculated_value = 10**((round(float(pow_incident), 3)-30)/20) * float(get_voltage_value)
                    vbd_calculated_value  = round(vbd_calculated_value, 3)
                    
                    #Condtions to add to the last row of the file
                    calucation_value_dict_1 = ["Power Incident" , pow_incident]
                    calucation_value_dict_2 = ["Simulation Voltage Value", get_voltage_value ]
                    
                    
                    value1 = "ABCD Calculation"
                    calucation_value_dict = [value1, vbd_calculated_value]
                    
                    get_file_name_daseline = os.path.basename(rfbd_datalog)
                    get_file_name_daseline = os.path.splitext(get_file_name_daseline)[0]
                    #New FILE NAME 
                    get_file_name_daseline = get_board_serial_number + "_" + "ABCDMethod" + "_" + get_RF_port_format + "_" + state_value + "_" +  get_file_name_daseline + ".csv"
                    new_path_to_save_file = os.path.join(get_data_saving_path, get_file_name_daseline)
                    
                    dataframe = pd.read_csv(rfbd_datalog)
                    dataframe = dataframe.append(pd.Series(calucation_value_dict_1, index=dataframe.columns[:len(calucation_value_dict_1)]), ignore_index=True)
                    dataframe = dataframe.append(pd.Series(calucation_value_dict_2, index=dataframe.columns[:len(calucation_value_dict_2)]), ignore_index=True)
                    dataframe = dataframe.append(pd.Series(calucation_value_dict, index=dataframe.columns[:len(calucation_value_dict)]), ignore_index=True)
                    blankIndex=[''] * len(dataframe)
                    dataframe.index = blankIndex
                    dataframe.to_csv(new_path_to_save_file)
             
            completion_time = time.time()
            completion_time = completion_time - start_time
            easygui.msgbox(msg=f"Program terminated in {round(completion_time, 4)} seconds", title="Successfully Terminated", ok_button="OK")
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    if app == None:
        app = QtWidgets.QApplication(sys.argv)
    app.setStyle('fusion')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
