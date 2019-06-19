# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 11:09:09 2019

@author: SinhaV
"""

   
def init():
    
    now = datetime.datetime.now()
    start_time = str(now.strftime("%Y-%m-%d %H:%M:%S"))
    
    strtlog = "Script triggered at " + start_time
    
############### Read Config File to get environment variables ###################################################
    rdcnfg = "Reading Config File to get environment variables "
    
    try:
#        Cnfg_Dir = str(sys.argv[1])
#        Cnfg_Dir = "C:/Vivek/Work/Projects/Gold_Care_Phase_1/03_Coding_Workspace/Config"
        
#        Cnfg_fname = str(sys.argv[2])

        Cnfg_Dir = "..\Config"
        Cnfg_fname= "config.txt"
        C_file = open(os.path.join(Cnfg_Dir,Cnfg_fname) ,'r')
        
        E_vars = C_file.readlines()
        var_list = dict()
        for i in range(len(E_vars)):
            E_vars[i] = E_vars[i].strip('\n')
            E_vars[i] = E_vars[i].strip('\t')
    
############################## Build the Variable Dictionary #################################################### 
            if not E_vars[i].lstrip().startswith('#'):
                var_line = E_vars[i].split("=")
                var_list[var_line[0].rstrip(" ")] = var_line[1].lstrip(" ").rstrip(" ")
                
        C_file.close()
                      

        Landing_Dir = var_list['Landing_Dir']
        Process_Dir = var_list['Process_Dir']
        Archiv_Dir = var_list['Archiv_Dir']
        Error_Dir = var_list['Error_Dir']
        Log_Dir = var_list['Log_Dir']
        
        print ("Start Logging the events")
        start_time = str(now.strftime("%Y_%m_%d_%H_%M_%S"))
        Log_fname = start_time + "_xmlparser.log"
        logname = os.path.join(Log_Dir,Log_fname)
        log = cusLogging()

        log.createlog(logname) 
        log.log('INFO', 'Logging has been enabled')
        log.log('INFO', strtlog)
        log.log('INFO', rdcnfg)
     
        log.log('INFO', 'Configuration loaded successfully.')

############################## call XML Parser ##################################################################    
        
        log.log('INFO', 'Calling XML Parser')

        tmp_data_file = parse_xml(Landing_Dir,Process_Dir,Archiv_Dir,Error_Dir,log)

#        tmp_data_file = 'xyz'

        log.log('Info', "Initiating database load module")
        
        ctd = CsvToDb()
        ctd.load_data(var_list, tmp_data_file, log)
        
     
       
    except Exception as e:
        print("A fatal error has occured which has terminated the program. Please look at the log file for more details.")
        log.log('ERROR',"A fatal error has occured which has terminated the program.")
        log.log('ERROR',str(e))

        
#################################################################################################################    
#%%    

init()
    
    
    
    
    