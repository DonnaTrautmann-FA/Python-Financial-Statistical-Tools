import re
import numpy as np
import pprint

def GetNumbers():                                            
    the_nine_digits =""                                      
    get_nine_digits = input("Enter a sequence of nine digits 0-9 (input example 965452671): ")  
    the_nine_digits = re.sub(r'[^\d]', '', get_nine_digits)  
    return the_nine_digits

def Calculate(digit_list):
    digit_matrix = np.array(digit_list).reshape(3,3)        
                                            
    calc_dict = {
      'mean':[np.mean(digit_matrix, axis=0).tolist(),np.mean(digit_matrix, axis=1).tolist(),np.mean(digit_matrix).tolist()],
      'variance':[np.var(digit_matrix, axis=0).tolist(),np.var(digit_matrix, axis=1).tolist(),np.var(digit_matrix).tolist()],
      'standard deviation':[np.std(digit_matrix, axis=0).tolist(),np.std(digit_matrix, axis=1).tolist(),np.std(digit_matrix).tolist()],
      'max':[np.max(digit_matrix, axis=0).tolist(),np.max(digit_matrix, axis=1).tolist(),np.max(digit_matrix).tolist()],
      'min':[np.min(digit_matrix, axis=0).tolist(),np.min(digit_matrix, axis=1).tolist(),np.min(digit_matrix).tolist()],
      'sum':[np.sum(digit_matrix, axis=0).tolist(),np.sum(digit_matrix, axis=1).tolist(),np.sum(digit_matrix).tolist()]
                }
    return calc_dict
    

the_nine_digits = GetNumbers()                               
                                      

if len(the_nine_digits) != 9:                                
    raise ValueError("List must contain nine numbers")      
    
digit_list =  [int(i) for i in the_nine_digits]                                                         

calc_dict = Calculate(digit_list)                            
pprint.pprint(calc_dict, sort_dicts=False)                                            

