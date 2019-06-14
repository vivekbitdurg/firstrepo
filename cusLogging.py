# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 14:56:05 2017

@author: SinhaV
"""
import datetime

class cusLogging:
    
    def createlog(self,logname):
        self.logname = logname
        self.f_name = open(self.logname,'w')
        print('Logging has been enabled ')
#        head = '{:^28}'.format('Time') + ':' + '{:^10}'.format('Level')  + ':' + '{:^10}'.format('Level') 
        self.f_name.write('       Time                :   Level   :  Message \n========================================================================================================================================================== \n')
        
        
    def log(self, level, msg):
         
        self.f_name = open(self.logname,'a')
        msg = str(datetime.datetime.now()).ljust(27) + ':' +  '{:^10}'.format(level) + ' : ' + msg + '\n'
        self.f_name.write(msg)
        self.f_name.close()
        
    
    