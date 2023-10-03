# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 14:59:53 2022

@author: juarez
"""
import sys
from cx_Freeze import setup, Executable

company_name=  "QUALCOMM"
product_name = "ABCD Method DataProcessing Tool"

options = {"build_exe":{"includes": 'atexit'}}

base = None 
#if sys.platform  == "Win32":
 #   base = "Win32GUI"
    
exe = Executable(script = r"ABCD_processing_UI.py",
                 base = "Win32GUI",
                 icon = "ABCD_L.ico",
                )

setup(name="ABCD MODE Processing Tool",
      version='1.0.0',
      description='Proccesing data logs from RFBD StandAlone Bench',
      executables = [exe],
      )