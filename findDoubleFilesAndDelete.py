# -*- coding: utf-8 -*-
# python version : 3.6

import os
import win32con,win32api 
import argparse
import subprocess
import os.path

def main():   
    cur_dir = r"D:\do\deleteDoubleFiles_from_ChromeDownload" #input('Input DIR to Find :  ')
    while  os.path.isdir(cur_dir) !=True:
        cur_dir = input('Input DIR to Find : ')
    check_files = []
    need_delete = []
    watch_files = []
    for f in os.listdir(cur_dir):         
        basename = os.path.splitext(f)[0]       
        if basename.find("(") > 0 :
            parts = basename.split("(")[1]           
            if parts.find(")") > 0 :
                mid_part = parts[:1]            
                if mid_part.isnumeric() == True:
                    check_files.append(f)                    
        else:
            watch_files.append(f)
 
    for f in watch_files: 
         for check in check_files:
             f_basename = os.path.splitext(f)[0]
             check_basename = os.path.splitext(check)[0]
             if check_basename.find(f_basename)== 0:
                 need_delete.append(check)
                 print("%s\n%s"%(f,check))                  
             else:
                 pass
    if len(need_delete)<= 0 :
        exit(0)
    do = input("You need to delete ? Key any to go on , except n to exit : ")
    if do == "n":
        exit(0)
    print("\n\nStart to Delete Files .....\n")
    for target in need_delete:        
        os.unlink(os.path.join(cur_dir,target))
        print("Delete File : %s"%target)
         

 
if __name__ == '__main__':    
    main()
