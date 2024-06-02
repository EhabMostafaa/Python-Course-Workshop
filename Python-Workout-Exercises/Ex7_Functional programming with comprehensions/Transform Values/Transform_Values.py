def trasnsform_values(old_dict):
    return {key:int(value)*int(value)  
            for key,value in old_dict.items()}

print(trasnsform_values({'a':1 , 'b':2 , 'c':3}))