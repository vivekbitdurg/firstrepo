# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 15:54:37 2018

@author: SinhaV
"""


from tkinter import filedialog

import os
import hashlib
import datetime

dir = filedialog.askdirectory()

strttime = str(datetime.datetime.now()).ljust(27) + '\n'
        
print(strttime)


SRC_DIR = dir


print(SRC_DIR)

fout = open('C:/Vivek/Work/test_hash/checksums_archive.csv', 'w')
fout.close()
fout = open('C:/Vivek/Work/test_hash/checksums_archive.csv', 'a') 

print("start Hashing")
for root, subdirs, files in os.walk(SRC_DIR):
   
    for file in files:
        
        with open(os.path.join(root, file), 'rb') as _file:
            hashval = hashlib.md5(_file.read()).hexdigest()
            print(root + file + ',' + hashval + '\n')
            fout.write(hashval +'|' + file +'|'+ root + '\n')
    
    
fout.close()


endtime = str(datetime.datetime.now()).ljust(27) + '\n'
print(endtime)