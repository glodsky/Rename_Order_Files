# -*- coding: utf-8 -*-
# python version : 3.6

import os
import os.path
 
cur_dir = r"D:\do\deleteDoubleFiles_from_ChromeDownload" #input('Input DIR to Find :  ')

def handleQeote():
    for f in os.listdir(cur_dir):         
        basename = os.path.splitext(f)[0]
        extename = os.path.splitext(f)[1]
        if os.path.isfile(f)==False or extename != ".pdf" :
            continue
        if basename.find("（") > 0 :
            print("basename = %s"% basename)
            need1 = basename.split("（")[0]
            parts = basename.split("（")[1]        
            if parts.find("）") > 0 :
                HanZiNums_part = parts.split("）")[0]        # 避免这种情况  渗透的本质是信息搜集（第五十二课））   
                newname = "%s：%s%s"%(HanZiNums_part,need1,extename)
                os.rename(os.path.join(cur_dir,f),os.path.join(cur_dir,newname))
                print("Rename Successfully !   %s" % newname)
                
def handleRename():
    for f in os.listdir(cur_dir):         
        basename = os.path.splitext(f)[0]
        extename = os.path.splitext(f)[1]
        if os.path.isfile(f)==False or extename != ".pdf" :
            continue
        if basename.find("第") > 0 :
            print("basename = %s"% basename)          
            parts = basename.split("_")[1]     
            newname = "%s%s"%(parts,extename)
            os.rename(os.path.join(cur_dir,f),os.path.join(cur_dir,newname))
            print("Rename Successfully !   %s" % newname)
                
def handleOrder():  
    HanZiNums = ["零","一","二","三","四","五","六","七","八","九","十","百","千"]  
    for f in os.listdir(cur_dir):
        nums = ""
        result = 0
        basename = os.path.splitext(f)[0]
        extename = os.path.splitext(f)[1]
        cal  = [] 
        if os.path.isfile(f)==False or extename != ".pdf" :
            continue
        if basename.find("：") > 0 :
            front = basename.split("：")[0]
            HanZiNums_part = front[1:-1]
            print("%s\n%s"%(f,HanZiNums_part))
            result  = 0
            Others = ""
            if HanZiNums_part.find("百")>0:
                Bai = HanZiNums_part.split("百")[0]
                if len(HanZiNums_part) == 2:
                    pass
                else:
                    HanZiNums_part = HanZiNums_part.split("百")[1]
                result +=  HanZiNums.index(Bai) * 100                
            if HanZiNums_part.find("十") >= 0:
                if len(HanZiNums_part) == 1 :
                    result += 1 * 10
                if len(HanZiNums_part) == 2 :
                    if HanZiNums_part.index("十") == 0 :                        
                        Others2 = HanZiNums_part.split("十")[1]
                        result +=  1 * 10 + HanZiNums.index(Others2)
                    if HanZiNums_part.index("十") > 0 :
                        Others2 = HanZiNums_part.split("十")[0]
                        result += HanZiNums.index(Others2) * 10
                if len(HanZiNums_part) == 3 : 
                    Shi = HanZiNums_part.split("十")[0]
                    Ge  = HanZiNums_part.split("十")[1]                    
                    result +=  HanZiNums.index(Shi) * 10 + HanZiNums.index(Ge)
            elif HanZiNums_part.find("零")>=0:
                if len(HanZiNums_part) == 2 :
                    #print("Others = %s"%Others)
                    result +=  HanZiNums.index(HanZiNums_part[1:])                  
            else:               
                pass
            
            if len(HanZiNums_part) == 1 and HanZiNums_part !="十": # 个位数
                result  =   HanZiNums.index(HanZiNums_part)
            
            newname = "%004d_%s"%(result,f)
            os.rename(os.path.join(cur_dir,f),os.path.join(cur_dir,newname))
            print("Format Nums Ordered Successfully !   %s" % newname)
             
handleQeote()
#handleRename()            
handleOrder()

