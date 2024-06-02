def flipped_dict(old_dict):
    return {value:key  
            for key,value in old_dict.items()}

print(flipped_dict({'a':1 , 'b':2}))