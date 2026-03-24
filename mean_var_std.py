import numpy as np



def calculate(digit_list):
    if len(digit_list) != 9:                                
        raise ValueError("List must contain nine numbers.")  
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