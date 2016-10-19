# -*- coding: utf-8 -*-

from distutils.core import setup  
  
import py2exe,sys,os  
  

sys.argv.append('py2exe')
includes = ["encodings", "encodings.*"]     

  
options = {"py2exe":  
  
    {"compressed": 1, 
     "optimize": 2,  
     "ascii": 1,  
     "includes":includes,  
     "bundle_files": 1,
     "dll_excludes": "MSVCP90.dll"  
     }  
    }  
setup(      
    options = options,       
    zipfile=None,   
    windows=[{"script": "QBSpiderApp.py" }]
    )   